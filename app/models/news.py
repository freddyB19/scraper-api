from typing import Iterable

from pydantic import BaseModel


class MarcaVideogames(BaseModel):
	url: str | None
	meta: str | None
	author: str | None
	title: str | None
	image: str | None


class WiredArticle(BaseModel):
	url: str | None
	title: str | None
	image: str | None
	detail: str | None

class LaNacionArticle(BaseModel):
	url: str | None
	date: str | None
	image: str | None
	title: str | None