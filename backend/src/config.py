from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=True,
    )

    APP_ENV: str = 'development'
    APP_DEBUG: bool = True
    APP_HOST: str = 'localhost'
    APP_PORT: int = 8000

    DB_USER: str = 'postgres'
    DB_PASSWORD: str = '456123'
    DB_NAME: str = 'food_locator'
    DB_HOST: str = 'localhost'
    DB_PORT: int = 5432

    SECRET_KEY: str = "secret_key"
    
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

config = Config()

