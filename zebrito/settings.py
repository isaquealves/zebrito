from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    APP_TITLE: str
    DATABASE_HOST: str
    DATABASE_NAME: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: str
    DATABASE_USER: str
    BROKER_PORT: str
    BROKER_URL: str

    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8',
    )

    @property
    def db_url(self):
        return (
            f"postgresql://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}"
            f"@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}")

settings = AppSettings()