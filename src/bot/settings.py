from pydantic_settings import BaseSettings
from pydantic import validator

class Settings(BaseSettings):
    OPENAI_API_KEY: str = ""
    TELEGRAM_BOT_TOKEN: str = ""
    VECTORSHIFT_API_KEY: str = ""
    ALLOWED_CHAT_IDS: list[int] = []

    @validator('ALLOWED_CHAT_IDS', pre=True)
    def parse_allowed_chat_ids(cls, v):
        if isinstance(v, str):
            return [int(i) for i in v.split(',')]
        elif isinstance(v, int):
            return [v]
        return v

    class Config:
        env_file = ".env"


settings = Settings()
