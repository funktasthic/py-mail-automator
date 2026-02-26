from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import EmailStr, Field

class Settings(BaseSettings):
    email_user: EmailStr = Field(alias="EMAIL_USER")
    email_pass: str = Field(alias="EMAIL_PASSWORD")
    smtp_server: str = Field(default="smtp.gmail.com", alias="SMTP_SERVER")
    smtp_port: int = Field(default=587, alias="SMTP_PORT")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

try:
    settings = Settings()
except Exception as e:
    print(f"Config Error: {e}")
    raise