"""Programmatic end-to-end smoke test: transcribe a local audio file and analyse a local image.
Run with: .venv\Scripts\python.exe scripts\test_e2e.py
"""
from dotenv import load_dotenv
import os, sys, time

# Ensure project root is on sys.path so imports of sibling modules work when run from scripts/
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

load_dotenv()

from brain_of_the_doctor import encode_image, analyse_image_with_query
from voice_of_the_patient import transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts

GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
IMAGE_MODEL = os.environ.get('GROQ_IMAGE_MODEL') or os.environ.get('FALLBACK_GROQ_MODEL')

if not GROQ_API_KEY:
    print('ERROR: GROQ_API_KEY not set')
    sys.exit(2)

print('Using GROQ_IMAGE_MODEL=', IMAGE_MODEL)

# Pick example files from project
AUDIO_FILE = 'final_output.mp3' if os.path.exists('final_output.mp3') else None
IMAGE_FILE = 'ai-doc.png' if os.path.exists('ai-doc.png') else None

if not AUDIO_FILE:
    print('No sample audio file found (final_output.mp3). Aborting test.')
    sys.exit(3)
if not IMAGE_FILE:
    print('No sample image found (ai-doc.png). Aborting test.')
    sys.exit(4)

print('Audio:', AUDIO_FILE)
print('Image:', IMAGE_FILE)

# 1) Transcribe
print('\n1) Transcribing audio...')
text = transcribe_with_groq(audio_filepath=AUDIO_FILE, stt_model='whisper-large-v3', GROQ_API_KEY=GROQ_API_KEY)
print('Transcription result:')
print(text)

# 2) Encode image and call image analysis
print('\n2) Encoding image and querying Groq image model...')
enc = encode_image(IMAGE_FILE)
query = 'Summarize the image and relate to the following text: "' + (text[:400] if text else '') + '"'
print('Query:', query[:200])
resp = analyse_image_with_query(query=query, encoded_image=enc, model=IMAGE_MODEL)
print('\nModel response:')
print(resp)

# 3) Synthesize response audio
print('\n3) Synthesizing TTS...')
outfile = f'test_output_{int(time.time()*1000)}.mp3'
text_to_speech_with_gtts(input_text=resp or 'No response', output_filepath=outfile)
print('Wrote TTS to', outfile, 'exists=', os.path.exists(outfile))

print('\nE2E test completed.')
