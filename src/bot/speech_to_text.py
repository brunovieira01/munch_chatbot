from openai import OpenAI

from .settings import settings


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
