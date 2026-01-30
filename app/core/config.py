from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    llm_mode: str = "local"

    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "phi3:mini"

    chroma_dir: str = "./data/chroma"
    upload_dir: str = "./data/uploads"

    top_k: int = 4
    chunk_size: int = 900
    chunk_overlap: int = 150

settings = Settings()
