import os
from dotenv import load_dotenv
from pydantic import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()


class Config(BaseSettings):
    ENV: str = os.getenv('APP_ENV')
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = os.getenv('APP_PORT')
    JWT_SECRET_KEY: str = "fastapi"
    JWT_ALGORITHM: str = "HS256"
    JWT_TIME_TO_EXPIRATION: int = 3600
  


AppConfig = Config()