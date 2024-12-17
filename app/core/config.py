from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    secret_jwt: str
    algorithm_jwt: str
    access_token_expire_minutes: int

    currency_data_api_key: str

    @property
    def get_database_url(self):
        return "sqlite:///test02.db"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
