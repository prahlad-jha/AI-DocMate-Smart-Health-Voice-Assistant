#Step1a: Setup Text to Speech–TTS–model with gTTS
import os
from gtts import gTTS
from dotenv import load_dotenv
import pygame
import time
load_dotenv()
def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


input_text="Hi this is Ai with Anand!"
#text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

#Step1b: Setup Text to Speech–TTS–model with ElevenLabs
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")
def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice= "Aria",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
#text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3")

#s-2 use model for text output to voice

import subprocess
import platform

def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            pygame.mixer.init()
            pygame.mixer.music.load(output_filepath)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            #subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
            #subprocess.run(['powershell', '-c', f'(New-Object WMPLib.WindowsMediaPlayer).controls.play()'])
            #subprocess.run(['powershell', '-c', f'(New-Object -ComObject WMPlayer.OCX).controls.play()'])
            #subprocess.run(['powershell', '-c', f'$player = New-Object -ComObject WMPlayer.OCX; $player.URL = "{output_filepath}"; $player.controls.play();'])
            #subprocess.run(['powershell', '-c', f'Start-Process wmplayer -ArgumentList "{output_filepath}"'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


input_text="Hi this is Ai with Anand, autoplay testing !"
#text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client=ElevenLabs(api_key=os.environ.get("ELEVENLABS_API_KEY"))
    audio_bytes=client.generate( # audio the pehle
        text= input_text,
        voice= "Aria",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    #elevenlabs.save(audio, output_filepath)
    audio_data = b"".join(audio_bytes)
    with open(output_filepath, "wb") as f:
         f.write(audio_data)
    #play_audio(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            pygame.mixer.init()
            pygame.mixer.music.load(output_filepath)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            #subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
            #subprocess.run(['powershell', '-c', f'(New-Object WMPLib.WindowsMediaPlayer).controls.play()'])
            #subprocess.run(['powershell', '-c', f'(New-Object -ComObject WMPlayer.OCX).controls.play()'])
            #subprocess.run(['powershell', '-c', f'$player = New-Object -ComObject WMPlayer.OCX; $player.URL = "{output_filepath}"; $player.controls.play();'])
            #subprocess.run(['powershell', '-c', f'Start-Process wmplayer -ArgumentList "{output_filepath}"'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")
#text_to_speech_with_elevenlabs(input_text, output_filepath="final_output.mp3")
