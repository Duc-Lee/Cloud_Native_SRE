from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    SERVICE_NAME: str = "User Service"
    POSTGRES_HOST: str = "postgres"
    POSTGRES_DB: str = "cloud_sre"
    POSTGRES_USER: str = "sre_user"
    POSTGRES_PASSWORD: str = "password"
    JWT_SECRET_KEY: str = "your-secret-key-keep-it-safe"
    ALGORITHM: str = "HS256"
    AUTH_SERVICE_URL: str = "http://auth:3000"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

if __name__ == "__main__":
    settings = Settings()
