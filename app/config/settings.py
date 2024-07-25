from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    x_list_key: str
    x_add_key: str

    class Config:
        env_file = ".env"


settings = Settings()
settings.database_url = str(settings.database_url)
settings.x_list_key = str(settings.x_list_key)
settings.x_add_key = str(settings.x_add_key)