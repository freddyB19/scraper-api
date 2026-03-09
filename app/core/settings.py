from typing import Annotated

from pydantic import field_validator

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, NoDecode

load_dotenv()

class Config(BaseSettings):
	url: str
	cors_origins: Annotated[list[str], NoDecode]
	
	@field_validator('cors_origins', mode='before')
	@classmethod
	def decode_cors_origins(cls, domains: str) -> list[str]:
		return [domain for domain in domains.split(',') if domain]

config = Config()

__all__ = ["config"]