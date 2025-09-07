import os
import gradio as gr
from brain_of_the_doctor import encode_image, analyse_image_with_query
from voice_of_the_patient import transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts

# Define system prompt
system_prompt = """You have to act as a professional doctor..."""

def process_inputs(audio_filepath, image_filepath):
    print(f"Audio Filepath: {audio_filepath}")
    print(f"Image Filepath: {image_filepath}")

    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
    if not GROQ_API_KEY:
        return "Error: Missing GROQ API Key", "Error: Missing API Key", None

    # Speech-to-text processing
    speech_to_text_output = transcribe_with_groq(
        audio_filepath=audio_filepath, stt_model="whisper-large-v3", GROQ_API_KEY=GROQ_API_KEY
    )
    
    if image_filepath:
        doctor_response = analyse_image_with_query(
            query=system_prompt + speech_to_text_output,
            encoded_image=encode_image(image_filepath),
            model="llama-3.2-11b-vision-preview"
        )
    else:
        doctor_response = "No image provided for analysis."

    # Generate voice output
    voice_output = "final_output.mp3"
    text_to_speech_with_gtts(input_text=doctor_response, output_filepath=voice_output)

    # Ensure the file exists before returning
    if not os.path.exists(voice_output):
        return speech_to_text_output, doctor_response, None

    return speech_to_text_output, doctor_response, voice_output

# Gradio Interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(type="filepath", label="Upload Audio"),
        gr.Image(type="filepath", label="Upload Image")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(type="filepath", label="Doctor's Voice")
    ],
    title="AI Doctor with Vision and Voice"
)

iface.launch(debug=True)