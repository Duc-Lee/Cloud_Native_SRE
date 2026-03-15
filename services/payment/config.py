from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    SERVICE_NAME: str = "Payment Service"
    JWT_SECRET_KEY: str
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
