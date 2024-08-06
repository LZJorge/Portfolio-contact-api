from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    x_list_key: str
    x_add_key: str

    app_url: str

    resend_api_key: str
    from_email: str
    to_email: str

    class Config:
        env_file = ".env"


settings = Settings()
settings.database_url = str(settings.database_url)
settings.x_list_key = str(settings.x_list_key)
settings.x_add_key = str(settings.x_add_key)
settings.app_url = str(settings.app_url)
settings.resend_api_key = str(settings.resend_api_key)
settings.from_email = str(settings.from_email)
settings.to_email = str(settings.to_email)
