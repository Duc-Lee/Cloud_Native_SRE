from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    SERVICE_NAME: str = "Notification Service"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

if __name__ == "__main__":
    settings = Settings()
