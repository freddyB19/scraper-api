from typing import Any
from itertools import chain


type Response = list[dict[str, Any]]
type GameData = list[dict[str, str | list[str]]]


def get_data_game(data: Response, game: str, detail_game: str) -> GameData:
	if not data:
		return []

	ATTR_PAGE = "page"
	ATTR_NAME = "name"
	ATTR_DATA = "data"

	format_game = game.lower()
	format_detail_game = detail_game.lower()

	result_game = filter(lambda page: page[ATTR_PAGE][ATTR_NAME] == format_game, data)
	result_detail_game = [
		detail[ATTR_PAGE][ATTR_DATA][format_detail_game]
		for detail in result_game
		if format_detail_game in detail[ATTR_PAGE][ATTR_DATA]
	]

	details = list(chain.from_iterable(result_detail_game))
	return details if details else []
