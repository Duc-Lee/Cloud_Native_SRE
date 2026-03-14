from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    SERVICE_NAME: str = "Product Service"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
