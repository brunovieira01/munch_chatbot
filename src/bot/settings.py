from pydantic_settings import BaseSettings
from pydantic import validator
from loguru import logger

class Settings(BaseSettings):
    OPENAI_API_KEY: str = ""
    TELEGRAM_BOT_TOKEN: str = ""
    VECTORSHIFT_API_KEY: str = ""
    ALLOWED_CHAT_IDS: list[int] = []

    @validator('ALLOWED_CHAT_IDS', pre=True)
    def parse_allowed_chat_ids(cls, v) -> list[int]:
        logger.debug(f"Parsing ALLOWED_CHAT_IDS: {v}")
        if isinstance(v, str):
            try:
                return [int(i) for i in v.split(',')]
            except ValueError as e:
                logger.error(f"Error parsing ALLOWED_CHAT_IDS: {e}")
                raise
        elif isinstance(v, int):
            return [v]
        return v

    class Config:
        env_file = ".env"


settings = Settings()
