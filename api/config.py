from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENVIRONMENT: str = "dev"
    DATABASE_URL: str
    REDIS_URL: str = "regis://localhost:6379"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()