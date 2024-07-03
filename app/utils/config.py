from pydantic_settings import BaseSettings, SettingsConfigDict
import logging
import os

class Settings(BaseSettings):
    database_url: str
    app_name: str
    ## jwt settings
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    ## scw provider settings
    scw_access_key_id: str
    scw_secret_key: str
    scw_organization_id: str
    scw_project_id: str

    class Config:
        env_file = ".env"

class TestSettings(Settings):
    debug: bool = True

    class Config:
        env_file = "test.env"

def get_settings(env: str) -> Settings:
    if env == "test":
        return TestSettings()
    else:
        return Settings()

env = os.getenv("ENVIRONMENT", "prod")
settings = get_settings(env)
