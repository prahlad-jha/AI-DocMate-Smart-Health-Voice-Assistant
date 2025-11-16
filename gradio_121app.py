import os
import gradio as gr
import subprocess
from brain_of_the_doctor import encode_image, analyse_image_with_query
import brain_of_the_doctor as bod
import traceback
from voice_of_the_patient import transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts
import sys

# Startup status: helpful info printed when app starts
print("=== Startup status ===")
print("Python executable:", sys.executable)
print("GROQ_API_KEY set:", bool(os.environ.get('GROQ_API_KEY') or getattr(__import__('brain_of_the_doctor'), 'GROQ_API_KEY', None)))
print("GROQ image model override:", os.environ.get('GROQ_IMAGE_MODEL') or os.environ.get('FALLBACK_GROQ_MODEL'))
print("======================")

# Define system prompt
system_prompt = """You have to act as a professional doctor..."""

def convert_audio_to_wav(input_path):
    """Convert any audio format to WAV using ffmpeg (if needed)."""
    if not input_path:
        return None
    
    output_path = "converted_audio.wav"
    try:
        # Check if file is already wav
        if input_path.lower().endswith('.wav'):
            return input_path
        
        # Convert to wav using ffmpeg with error output captured
        result = subprocess.run(
            ['ffmpeg', '-i', input_path, '-ar', '16000', '-ac', '1', output_path, '-y'],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if result.returncode == 0 and os.path.exists(output_path):
            print(f"✓ Audio converted successfully to {output_path}")
            return output_path
        else:
            print(f"ℹ Using original audio file (conversion optional)")
            return input_path
            
    except FileNotFoundError:
        print("ℹ ffmpeg not found. Using original audio file.")
        return input_path
    except subprocess.TimeoutExpired:
        print("ℹ Conversion timed out. Using original audio file.")
        return input_path
    except Exception as e:
        print(f"ℹ Conversion info: {e}. Using original audio file.")
        return input_path

def process_inputs(audio_filepath, image_filepath):
    print(f"Audio Filepath: {audio_filepath}")
    print(f"Image Filepath: {image_filepath}")

    # prefer environment variable, fall back to value loaded by brain_of_the_doctor
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY") or getattr(bod, "GROQ_API_KEY", None)
    if not GROQ_API_KEY:
        return "Error: Missing GROQ API Key", "Error: Missing API Key", None

    # wrap processing in try/except so Gradio shows readable errors instead of generic "Error"
    try:

        # Convert audio to WAV format if needed
        converted_audio = convert_audio_to_wav(audio_filepath)
        if not converted_audio:
            return "Error: Could not process audio file", "", None

        # Speech-to-text processing
        speech_to_text_output = transcribe_with_groq(
            audio_filepath=converted_audio, stt_model="whisper-large-v3", GROQ_API_KEY=GROQ_API_KEY
        )
        
        if image_filepath:
            # choose model: prefer environment override, then brain_of_the_doctor default
            model_to_use = os.environ.get('GROQ_IMAGE_MODEL') or getattr(bod, 'model', 'llama-3.2-90b-vision-preview')
            doctor_response = analyse_image_with_query(
                query=system_prompt + speech_to_text_output,
                encoded_image=encode_image(image_filepath),
                model=model_to_use
            )
        else:
            doctor_response = "No image provided for analysis."

        # Generate voice output to a unique filename to avoid permission conflicts
        import time
        voice_output = f"final_output_{int(time.time()*1000)}.mp3"
        try:
            text_to_speech_with_gtts(input_text=doctor_response, output_filepath=voice_output)
        except PermissionError as pe:
            # Try a fallback filename if permission denied
            voice_output = f"final_output_fallback_{int(time.time()*1000)}.mp3"
            try:
                text_to_speech_with_gtts(input_text=doctor_response, output_filepath=voice_output)
            except Exception as e:
                return speech_to_text_output, f"Error: {e}", None
        except Exception as e:
            return speech_to_text_output, f"Error: {e}", None

        # Ensure the file exists before returning
        if not os.path.exists(voice_output):
            return speech_to_text_output, doctor_response, None

        return speech_to_text_output, doctor_response, voice_output
    except Exception as exc:
        tb = traceback.format_exc()
        print("Error in process_inputs:\n", tb)
        # Return the exception message and stack trace summary in the UI so user can see what's wrong
        return f"Error: {exc}", f"Traceback (first 400 chars): {tb[:400]}", None

# Gradio Interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(type="filepath", label="Record Audio", sources=["microphone"]),
        gr.Image(type="filepath", label="Upload Image")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(type="filepath", label="Doctor's Voice")
    ],
    title="AI Doctor with Vision and Voice"
)

iface.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)), debug=True)