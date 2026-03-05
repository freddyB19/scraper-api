from typing import Iterable
from pydantic import BaseModel


class LOLChampion(BaseModel):
	name: str | None
	url: str | None
	images: Iterable[str] | None


class LOLArticle(BaseModel):
	url: str | None
	date: str | None
	title: str | None
	detail: str | None
	category: str | None


class EasportNews(BaseModel):
	tag: str | None
	date: str | None
	image: str | None
	title: str | None
	detail: str | None


class EasportGame(BaseModel):
	url: str | None
	logo: str | None
	image: str | None
	title: str | None


class VideoGameMetadata(BaseModel):
	url: str | None
	type: str | None


class EasportSoon(BaseModel):
	title: str | None
	date: str | None
	console: Iterable[VideoGameMetadata] | None
	genre: Iterable[VideoGameMetadata] | None


class EasportUpdate(BaseModel):
	url: str | None
	info: str | None
	date: str | None
	image: str | None
	title: str | None
	detail: str | None


class IracingCars(BaseModel):
	url: str | None
	type: str | None
	image: str | None
	is_new: bool | None


class IracingTracks(BaseModel):
	url: str | None
	track: str | None
	image: str | None
	is_new: bool | None
	included: bool | None


class IracingSeasons(BaseModel):
	image: str | None
	season: str | None
	season_url: str | None
	season_date: str | None
	is_latest: bool | None


class SeriesCup(BaseModel):
	url: str | None
	name: str | None
	image: str | None


class IracingSeries(BaseModel):
	name: str | None
	type: Iterable[SeriesCup] | None


class Author(BaseModel):
	name: str | None
	url: str | None


class IracingNews(BaseModel):
	url: str | None
	date: str | None
	title: str | None
	image: str | None
	detail: str | None
	author: Author | None
