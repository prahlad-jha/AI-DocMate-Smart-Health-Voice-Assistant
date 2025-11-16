"""End-to-end test: transcribe an existing audio file and run image analysis on `ai-doc.png`.
Run with the project's venv Python:
.venv\Scripts\python.exe scripts\e2e_test.py
"""
import os, traceback, sys
from dotenv import load_dotenv
load_dotenv()

# Ensure repo root is on sys.path so imports work when running from `scripts/`
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

print("Using Python:", os.sys.executable)
print("GROQ_API_KEY present:", 'GROQ_API_KEY' in os.environ)
print("GROQ_IMAGE_MODEL:", os.environ.get('GROQ_IMAGE_MODEL'))

# Import helpers
try:
    from brain_of_the_doctor import encode_image, analyse_image_with_query
    from voice_of_the_patient import transcribe_with_groq
except Exception as e:
    print("Import error:", e)
    traceback.print_exc()
    raise

# Paths
here = os.path.dirname(__file__)
image_path = os.path.join(here, '..', 'ai-doc.png')
image_path = os.path.normpath(image_path)
# Use an existing audio file in the repo if available
audio_path = os.path.join(here, '..', 'final_output.mp3')
audio_path = os.path.normpath(audio_path)

print('\nImage path:', image_path)
print('Audio path:', audio_path)

# Encode image
try:
    encoded = encode_image(image_path)
    print('Encoded image length:', len(encoded))
except Exception as e:
    print('Failed to encode image:', e)
    traceback.print_exc()
    encoded = None

# Run image analysis
if encoded:
    try:
        model = os.environ.get('GROQ_IMAGE_MODEL') or os.environ.get('FALLBACK_GROQ_MODEL') or 'llama-3.3-70b-versatile'
        print('Calling analyse_image_with_query with model:', model)
        result = analyse_image_with_query('Please describe any visible skin issues in the image.', model, encoded)
        print('\nImage analysis result:\n', result)
    except Exception as e:
        print('Image analysis failed:', e)
        traceback.print_exc()

# Run transcription
if os.path.exists(audio_path):
    try:
        stt_model = 'whisper-large-v3'
        print('\nCalling transcribe_with_groq with model:', stt_model)
        transcription = transcribe_with_groq(audio_path, stt_model, os.environ.get('GROQ_API_KEY'))
        print('\nTranscription:\n', transcription)
    except Exception as e:
        print('Transcription failed:', e)
        traceback.print_exc()
else:
    print('\nNo audio file found to transcribe at', audio_path)
