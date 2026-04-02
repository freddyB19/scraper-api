from typing import Iterable, Literal

from pydantic import validate_call

from models import news
from .news_services import get_data_news

type Response = list[dict]
type NewsData = list[dict[str, str]]
type LaNacionPage = Literal['juegos', 'tecnologia']
type WiredPage = Literal['espacio', 'robots', 'neurociencia', 'biotecnologia']



@validate_call
def get_marca_videogames(data: Response) -> Iterable[news.MarcaVideogames]:
	news_name = "marca"
	notes = get_data_news(data, name = news_name)
	return [
		news.MarcaVideogames(
			url = note.get("url"),
			meta = note.get("meta"),
			author = note.get("autor"),
			title = note.get("titulo"),
			image = note.get("imagen")
		)
		for note in notes
	]

@validate_call
def get_wired_articles(data: Response, page: WiredPage) -> Iterable[news.WiredArticle]:
	type_pages = {
		'espacio': 'wired espacio', 
		'robots': 'wired robots', 
		'neurociencia': 'wired neurociencia', 
		'biotecnologia': 'wired biotecnología'
	}

	news_name = "wired"
	notes = get_data_news(data, name = news_name, page = type_pages[page])


	return [
		news.WiredArticle(
			url = note.get("url"),
			title = note.get("title"),
			image = note.get("image"),
			detail = note.get("summary"),
		)
		for note in notes
	]


@validate_call
def get_lanacion_articles(data: Response, page: LaNacionPage) -> Iterable[news.LaNacionArticle]:
	type_pages = {
		'juegos': '',
		'tecnologia': 'la nación tecnología', 
	}

	news_name = "la nación"
	notes = get_data_news(data, name = news_name, page = type_pages[page])

	return [
		news.LaNacionArticle(
			url = note.get("url"),
			date = note.get("fecha"),
			image = note.get("imagen"),
			title = note.get("titulo"),
		)
		for note in notes
	]
