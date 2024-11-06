import os
from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# 프로젝트 루트 디렉토리 경로 설정
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# 환경 변수 로딩
env = os.environ.get("ENV_TYPE", "dev")

def get_env(env_type: str):
    assert env_type in ["dev", "main", "alpha", "test"]
    if env_type == "main":
        return "main.env"
    elif env_type == "dev":
        return f"dev.env"
    elif env_type == "alpha" or env_type == "test":
        return f"alpha.env"
    
    
# .env 파일 로드
# env_file = BASE_DIR / get_env(env)
env_file = os.path.join(BASE_DIR, "env", get_env(env))
load_dotenv(env_file, override=True)

class Settings(BaseSettings):
    # App
    version: str = Field(os.environ.get("VERSION", "0.0.1"))
    dev: bool = Field(os.environ.get("DEV", "True").lower() == "true")
    port: int = Field(int(os.environ.get("PORT", "8000")))
    # Database
    db_url: str = Field(os.environ.get("DB_URL"))
    # Security
    secret_key: str = Field(os.environ.get("SECRET_KEY"))
    algorithm: str = Field(os.environ.get("ALGORITHM", "HS256"))
    access_token_expire_minutes: int = Field(
        int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", "180"))
    )

# 설정 인스턴스 생성
settings = Settings()
