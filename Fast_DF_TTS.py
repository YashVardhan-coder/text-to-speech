import os
import subprocess
import tempfile
from playsound import playsound
import threading

def speak(text:str,voice: str = "en-IN-NeerjaNeural") -> None:
    try:
        with tempfile.NamedTemporaryFile(delete=False,suffix=".mp3") as tmpfile:
            output_file = tmpfile.name

        command = f'python -m edge_tts --voice {voice} --text "{text}" --write-media {output_file}'
        subprocess.run(command,shell=True, check=True)

        threading.Thread(target=playsound,args=(output_file,)).start()

    except Exception as e:
        print(e)

# while True:
    # x = input("enter: ")
speak("hello sir, i am jarvis ")
speak("how can i help you today?")
