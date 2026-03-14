from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    SERVICE_NAME: str = "Order Service"
    USER_SERVICE_URL: str
    PAYMENT_SERVICE_URL: str
    RABBIT_URL: str
    REDIS_HOST: str
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

if __name__ ==   "__main__":
    settings = Settings()

