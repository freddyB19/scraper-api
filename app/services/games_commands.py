from typing import Any, Iterable, Literal

from pydantic import validate_call

from models import games
from .games_services import get_data_game

type Response = list[dict[str, Any]]


@validate_call
def get_lol_champions(data: Response) -> Iterable[games.LOLChampion]:
	if not data:
		return []

	game = "lol"
	detail = "champions"
	champions = get_data_game(data = data, game = game, detail_game = detail)

	return [
		games.LOLChampion(
			name = champion.get("champion"),
			url = champion.get("url"),
			images = champion.get("images"),
		)
		for champion in champions
	]

type LOLTypeArticle = Literal["notas", "noticias"]

@validate_call
def get_lol_articles(data: Response, detail: LOLTypeArticle) -> Iterable[games.LOLArticle]:
	if not data:
		return []
		
	game = "lol"
	articles = get_data_game(data = data, game = game, detail_game = detail)
	
	return [
		games.LOLArticle(
			url = article.get("url"),
			date = article.get("fecha"),
			title = article.get("titulo"),
			detail = article.get("detalle"),
			category = article.get("categoria"),
		)
		for article in articles
	]

@validate_call
def get_iracing_cars(data: Response) -> Iterable[games.IracingCars]:
	if not data:
		return []

	game = "iracing"
	detail = "cars"

	cars = get_data_game(data = data, game = game, detail_game = detail)

	return [games.IracingCars(**car) for car in cars]

@validate_call
def get_iracing_tracks(data: Response) -> Iterable[games.IracingTracks]:
	if not data:
		return []

	game = "iracing"
	detail = "tracks"

	tracks = get_data_game(data = data, game = game, detail_game = detail)

	return [games.IracingTracks(**track) for track in tracks]

@validate_call
def get_iracing_seasons(data: Response) -> Iterable[games.IracingSeasons]:
	if not data:
		return []
	
	game = "iracing"
	detail = "seasons"

	seasons = get_data_game(data = data, game = game, detail_game = detail)

	return [games.IracingSeasons(**season) for season in seasons]

@validate_call
def get_iracing_series(data: Response) -> Iterable[games.IracingSeries]:
	if not data:
		return []

	game = "iracing"
	detail = "series"

	series = get_data_game(data = data, game = game, detail_game = detail)

	return [
		games.IracingSeries(
			type = serie.pop("data"),
			**serie
		) 
		for serie in series
	]

@validate_call
def get_iracing_news(data: Response) -> Iterable[games.IracingNews]:
	if not data:
		return []

	game = "iracing"
	detail = "news"

	news = get_data_game(data = data, game = game, detail_game = detail)

	return [games.IracingNews(**article) for article in news]

type EasportGameDetail = Literal["gratuitos", "novedades"]

@validate_call
def get_easport_games(data: Response, detail: EasportGameDetail) -> Iterable[games.EasportGame]:
	if not data:
		return []

	game = "easport"

	details_game = get_data_game(data = data, game = game, detail_game = detail)

	return [
		games.EasportGame(
			url = game.get("url"),
			logo = game.get("logo"),
			image = game.get("imagen"),
			title = game.get("titulo")
		)

		for game in details_game
	]

@validate_call
def get_easport_news(data: Response) -> Iterable[games.EasportNews]:
	if not data:
		return []

	game = "easport"
	detail = "noticias"

	articles = get_data_game(data = data, game = game, detail_game = detail)

	return [
		games.EasportNews(
			tag = article.get("etiqueta"),
			date = article.get("fecha"),
			image = article.get("imagen"),
			title = article.get("titulo"),
			detail = article.get("descripcion"),
		)
		for article in articles
	]

@validate_call
def get_easport_soon(data: Response) -> Iterable[games.EasportSoon]:
	if not data:
		return []

	game = "easport"
	detail = "proximamente"

	articles = get_data_game(data = data, game = game, detail_game = detail)

	return [
		games.EasportSoon(
			title = game.get("titulo"),
			date = game.get("fecha"),
			console = [
				games.VideoGameMetadata(
					url = metadata.get("url"),
					type = metadata.get("tipo"),
				)
				for metadata in game.get("plataformas")
			],
			genre = [
				games.VideoGameMetadata(
					url = metadata.get("url"),
					type = metadata.get("tipo"),
				) 
				for metadata in game.get("genero")
			],
		)

		for game in articles
	]

@validate_call
def get_easport_updates(data: Response) -> Iterable[games.EasportUpdate]:
	if not data:
		return []

	game = "easport"
	detail = "actualizaciones"

	updates = get_data_game(data = data, game = game, detail_game = detail)

	return [
		games.EasportUpdate(
			url = note.get("url"),
			info = note.get("informacion"),
			date = note.get("fecha"),
			image = note.get("imagen"),
			title = note.get("titulo"),
			detail = note.get("detalle"),
		)
		for note in updates
	]
