from pydantic_settings import BaseSettings

class Config(BaseSettings):
    database_url: str
    secret_key: str

    class Config:
        env_file = ".env"  # Load variables from a .env file

# Assume `.env` file contains:
# DATABASE_URL=mysql://user:pass@localhost/db
# SECRET_KEY=supersecret

config = Config()
print(config.database_url)  # mysql://user:pass@localhost/db
print(config.secret_key)    # supersecret
