import base64
from openai import OpenAI
import requests

from settings import settings
import io

google_key = "bleh"
openai_key = "bleh"

def speech_to_text_google(file_data, lang="en-US"):
    data = {
        "audio": {"content": base64.b64encode(file_data)},
        "config": {
            "enableAutomaticPunctuation": True,
            "encoding": "MP3",
            "languageCode": lang,
            "model": "video",
        },
    }

    payload = {
        "key": settings.GOOGLE_API_KEY,
    }

    url = "https://speech.googleapis.com/v1p1beta1/speech:recognize"
    response = requests.post(url, params=payload, json=data)

    try:
        data = response.json()
        return data["results"][0]["alternatives"][0]["transcript"]
    except Exception as ex:
        print("Exception:", ex)
        print("response:", response.text)

def speech_to_text_whisper(file_path, lang="en"):
    client = OpenAI(api_key=settings.OPENAI_API_KEY)

    audio_file = open(file_path, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        language=lang,
    )

    try:
        return transcription.text
    except Exception as ex:
        print("Exception:", ex)
        print("transcription:", transcription)
