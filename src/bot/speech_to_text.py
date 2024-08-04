import logging

from openai import OpenAI

from .settings import settings

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


class SpeechToTextWhisper:
    def __init__(self, api_key: str = settings.OPENAI_API_KEY) -> None:
        """
        Initialize the SpeechToTextWhisper class with the given API key.

        Parameters
        ----------
        api_key : str, optional
            The API key for OpenAI, by default settings.OPENAI_API_KEY
        """
        self.client = OpenAI(api_key=api_key)

    def transcribe(self, file_path: str, lang: str = "en") -> str:
        """
        Transcribe the audio file at `file_path` using the whisper model.

        Parameters
        ----------
        file_path : str
            The path to the audio file to transcribe.
        lang : str, optional
            The language of the audio, by default "en".

        Returns
        -------
        str
            The transcription of the audio file.

        Raises
        ------
        Exception
            If there is an error transcribing the audio.
        """
        try:
            with open(file_path, "rb") as audio_file:
                transcription = self.client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                    language=lang,
                )
            return transcription.text
        except Exception as ex:
            logging.exception("Exception raised while transcribing audio:")
            return "Sorry, there was an error transcribing your audio. Please try again later."
