from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=True,
    )

    app_env: str = 'development'
    app_debug: bool = True
    app_host: str = 'localhost'
    app_port: int = 8000
    
    database_url: str = 'sqlite:///./test.db'
    
config = Config()