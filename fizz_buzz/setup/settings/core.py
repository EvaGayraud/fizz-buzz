from pydantic_settings import BaseSettings


class CoreSettings(BaseSettings):
    MODEL: str = "LLMClient"
    ENVIRONMENT: str = "dev"


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "fizz-buzz"
    CORS_ALLOW_ORIGIN_REGEX: str = r"^https?://(localhost|.+\.localhost|127\.0\.0\.1|.+)(:[0-9]+)?$"
    MONGODB_URI: str = ""
