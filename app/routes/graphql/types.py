from typing import Iterable
import strawberry
from strawberry import relay

type Article = dict[str, str]
type Champions = dict[str, str | list[str]]

@strawberry.type
class NodeConnection(relay.Node):
	code: relay.NodeID[int]


@strawberry.type
class LOLChampion(NodeConnection):
	name: str | None
	url: str | None
	images: list[str] | None


@strawberry.type
class LOLNewsNotes(NodeConnection):
	title: str | None
	url: str | None
	category: str | None
	date: str | None
	detail: str | None


def format_articles(articles: list[Article]) -> Iterable[LOLNewsNotes]:
	return [
		LOLNewsNotes(
			code = index,
			title = article.get("titulo"),
			url = article.get("url"),
			category = article.get("categoria"),
			date = article.get("fecha"),
			detail = article.get("detalle"),
		)
		for index, article in enumerate(articles)
	]

def format_champions(champions: list[Champions]) -> Iterable[LOLChampion]:
	return [
		LOLChampion(
			code = index,
			name = champion.get("champion"),
			url = champion.get("url"),
			images = champion.get("images"),
		) 
		for index, champion in enumerate(champions)
	]


@strawberry.type
class LOL:

	@relay.connection(relay.ListConnection[LOLNewsNotes])
	def notes(self) -> Iterable[LOLNewsNotes]:
		return format_articles(articles = self.get("notes"))

	@relay.connection(relay.ListConnection[LOLNewsNotes])
	def news(self) -> Iterable[LOLNewsNotes]:
		return format_articles(articles = self.get("news"))

	@relay.connection(relay.ListConnection[LOLChampion])
	def champions(self) -> Iterable[LOLChampion]:
		return format_champions(self.get("champions"))


@strawberry.type
class EasportNews(NodeConnection):
	tag: str | None
	date: str | None
	image: str | None
	title: str | None
	detail: str | None


@strawberry.type
class EasportGame(NodeConnection):
	url: str | None
	logo: str | None
	image: str | None
	title: str | None


@strawberry.type
class VideoGameMetadata:
	url: str | None
	type: str | None

@strawberry.type
class EasportSoon(NodeConnection):
	title: str | None
	date: str | None
	console: list[VideoGameMetadata] | None
	genre: list[VideoGameMetadata] | None

@strawberry.type
class EasportUpdate(NodeConnection):
	url: str | None
	info: str | None
	date: str | None
	image: str | None
	title: str | None
	detail: str | None

@strawberry.type
class Easport:
	@relay.connection(relay.ListConnection[EasportNews])
	def news(self) -> Iterable[EasportNews]:
		return [
			EasportNews(
				code = index,
				tag = article.get("etiqueta"),
				date = article.get("fecha"),
				image = article.get("imagen"),
				title = article.get("titulo"),
				detail = article.get("descripcion"),
			)
			for index, article in enumerate(self.get("news"))
		]

	@relay.connection(relay.ListConnection[EasportSoon])
	def soon(self) -> Iterable[EasportSoon]:
		return [
			EasportSoon(
				code = index,
				title = game.get("titulo"),
				date = game.get("fecha"),
				console = [
					VideoGameMetadata(
						url = metadata.get("url"),
						type = metadata.get("tipo"),
					)
					for metadata in game.get("plataformas")
				],
				genre = [
					VideoGameMetadata(
						url = metadata.get("url"),
						type = metadata.get("tipo"),
					) 
					for metadata in game.get("genero")
				],
			)
			for index, game in enumerate(self.get("soon"))
		]

	@relay.connection(relay.ListConnection[EasportGame])
	def novelties(self) -> Iterable[EasportGame]:
		return [
			EasportGame(
				code = index,
				url = game.get("url"),
				logo = game.get("logo"),
				image = game.get("imagen"),
				title = game.get("titulo"),
			)
			for index, game in enumerate(self.get("novelties"))
		]

	@relay.connection(relay.ListConnection[EasportGame])
	def free(self) -> Iterable[EasportGame]:
		return [
			EasportGame(
				code = index,
				url = game.get("url"),
				logo = game.get("logo"),
				image = game.get("imagen"),
				title = game.get("titulo"),
			)
			for index, game in enumerate(self.get("free"))
		]

	@relay.connection(relay.ListConnection[EasportUpdate])
	def updates(self) -> Iterable[EasportUpdate]:
		return [
			EasportUpdate(
				code = index,
				url = update.get("url"),
				info = update.get("informacion"),
				date = update.get("fecha"),
				image = update.get("imagen"),
				title = update.get("titulo"),
				detail = update.get("detalle"),
			)
			for index, update in enumerate(self.get("updates"))
		]


@strawberry.type
class IracingCars(NodeConnection):
	url: str | None
	type: str | None
	image: str | None
	is_new: bool | None

@strawberry.type
class IracingTracks(NodeConnection):
	url: str | None
	track: str | None
	image: str | None
	is_new: bool | None
	included: bool | None

@strawberry.type
class IracingSeasons(NodeConnection):
	image: str | None
	season: str | None
	season_url: str | None
	season_date: str | None
	is_latest: bool | None

@strawberry.type
class SeriesCup:
	url: str | None
	name: str | None
	image: str | None

@strawberry.type
class IracingSeries(NodeConnection):
	name: str | None
	type: list[SeriesCup] | None

@strawberry.type
class Author:
	name: str | None
	url: str | None

@strawberry.type
class IracingNews(NodeConnection):
	url: str | None
	date: str | None
	title: str | None
	image: str | None
	detail: str | None
	author: Author | None


@strawberry.type
class Iracing:
	
	@relay.connection(relay.ListConnection[IracingCars])
	def cars(self) -> Iterable[IracingCars]:
		return [
			IracingCars(code = index, **car) 
			for index, car in enumerate(self.get("cars"))
		]

	@relay.connection(relay.ListConnection[IracingTracks])
	def tracks(self) -> Iterable[IracingTracks]:
		return [
			IracingTracks(code = index, **track) 
			for index, track in enumerate(self.get("tracks"))
		] 

	@relay.connection(relay.ListConnection[IracingSeasons])
	def seasons(self) -> Iterable[IracingSeasons]:
		return [
			IracingSeasons(code = index, **season) 
			for index, season in enumerate(self.get("seasons"))
		]

	@relay.connection(relay.ListConnection[IracingSeries])
	def series(self) -> Iterable[IracingSeries]:
		return [
			IracingSeries(
				code = index,
				type = [SeriesCup(**type_serie) for type_serie in serie.get("data")],
				name = serie.get("name"),
			)
			for index, serie in enumerate(self.get("series"))
		]

	@relay.connection(relay.ListConnection[IracingNews])
	def news(self) -> Iterable[IracingNews]:
		return [
			IracingNews(
				code = index,
				url = article.get("url"),
				date = article.get("date"),
				title = article.get("title"),
				image = article.get("image"),
				detail = article.get("detail"),
				author = Author(**article.get("author")),
			) 
			for index, article in enumerate(self.get("news"))
		]


@strawberry.type
class MarcaVideogames(NodeConnection):
	url: str | None
	meta: str | None
	autor: str | None
	title: str | None
	image: str | None

@strawberry.type
class Marca:
	@relay.connection(relay.ListConnection[MarcaVideogames])
	def games(self) -> Iterable[MarcaVideogames]:
		return [
			MarcaVideogames(
				code = index,
				url = article.get("url"),
				meta = article.get("meta"),
				autor = article.get("autor"),
				title = article.get("titulo"),
				image = article.get("imagen")
			)
			for index, article in enumerate(self.get("marca"))
		]


@strawberry.type
class LaNacionArticle(NodeConnection):
	url: str | None
	date: str | None
	image: str | None
	title: str | None

@strawberry.type
class LaNacion:
	@relay.connection(relay.ListConnection[LaNacionArticle])
	def games(self) -> Iterable[LaNacionArticle]:
		return [
			LaNacionArticle(
				code = index,
				url = article.get("url"),
				date = article.get("fecha"),
				image = article.get("imagen"),
				title = article.get("titulo"),
			)
			for index, article in enumerate(self.get("games"))
		]
	@relay.connection(relay.ListConnection[LaNacionArticle])
	def tecnology(self) -> Iterable[LaNacionArticle]:
		return [
			LaNacionArticle(
				code = index,
				url = article.get("url"),
				date = article.get("fecha"),
				image = article.get("imagen"),
				title = article.get("titulo"),
			)
			for index, article in enumerate(self.get("tecnology"))
		]

@strawberry.type
class WiredArticle(NodeConnection):
	url: str | None
	title: str | None
	image: str | None
	detail: str | None

def wired_format_articles(articles: list[Article]) -> list[Article]:
	return [
		WiredArticle(
			code = index,
			url = article.get("url"),
			title = article.get("titulo"),
			image = article.get("imagen"),
			detail = article.get("resum"),
		)
		for index, article in enumerate(articles)
	]

@strawberry.type
class Wired:
	
	@relay.connection(relay.ListConnection[WiredArticle])
	def space(self) -> Iterable[WiredArticle]:
		return wired_format_articles(self.get("space"))

	@relay.connection(relay.ListConnection[WiredArticle])
	def biotechnology(self) -> Iterable[WiredArticle]:
		return wired_format_articles(self.get("biotechnology"))

	@relay.connection(relay.ListConnection[WiredArticle])
	def neuroscience(self) -> Iterable[WiredArticle]:
		return wired_format_articles(self.get("neuroscience"))

	@relay.connection(relay.ListConnection[WiredArticle])
	def robots(self) -> Iterable[WiredArticle]:
		return wired_format_articles(self.get("robots"))
