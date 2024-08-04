from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    GOOGLE_API_KEY: str = ""
    OPENAI_API_KEY: str = ""
    TELEGRAM_BOT_TOKEN: str = ""
    VECTORSHIFT_API_KEY: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
