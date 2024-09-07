from pydantic import BaseConfig

# ngrok http http://localhost:8000
class Settings(BaseConfig):
    DB_port: int = 5433
    DB_user: str = "postgres"
    DB_pass: str = "postgres"
    DB_name: str = "the_best_team"
    DB_host: str = '127.0.0.1'


    server_host: str = '127.0.0.1'
    server_port: int = 8000

    database_url: str= 'postgresql+psycopg://postgres:postgres@127.0.0.1:5433/the_best_team'
    # database_url: str= f"postgresql+asyncpg://{DB_user}:{DB_pass}@{DB_host}:{DB_port}/{DB_name}"

    jwt_secret: str="qwerty"
    jwt_algorithm: str = 'HS256'
    jwt_expires_s: int = 43200


# settings = Settings(
#     _env_file='.env',
#     _env_file_encoding='utf-8',
# )
