import pytest

from pydantic import ValidationError
from app.services import games_commands

from tests.fixtures import (
	RESPONSE_JSON_GAMES,
	RESPONSE_EMPTY_JSON_GAMES
)

@pytest.fixture
def response_json():
	return RESPONSE_JSON_GAMES

@pytest.fixture
def response_empty_json():
	return RESPONSE_EMPTY_JSON_GAMES


class TestCommandLol:

	def test_command_get_lol_champions(self, response_json):
		champions = games_commands.get_lol_champions(response_json)

		assert champions
		assert len(champions) > 0
		
		champion = champions[0].model_dump()
		assert "name" in champion
		assert "url" in champion
		assert "images" in champion

	def test_command_get_lol_champions_with_empty_values(self, response_empty_json):
		without_values = 0
		champions = games_commands.get_lol_champions(response_empty_json)

		assert not champions
		assert len(champions) == without_values


	@pytest.mark.parametrize(
		"detail",
		[
			"noticias",
			"notas"
		]
	)
	def test_command_get_lol_articles(self, response_json, detail):
		articles = games_commands.get_lol_articles(response_json, detail = detail)

		assert articles
		assert len(articles) > 0

		article = articles[0].model_dump()
		assert "url" in article
		assert "date" in article
		assert "title" in article
		assert "detail" in article
		assert "category" in article

	@pytest.mark.parametrize(
		"detail",
		[
			"noticias",
			"notas"
		]
	)
	def test_command_get_lol_articles_with_empty_values(self, response_empty_json, detail):
		without_values = 0
		articles = games_commands.get_lol_articles(response_empty_json, detail = detail)

		assert not articles
		assert len(articles) == without_values


class TestCommandIracing:

	def test_command_get_iracing_cars(self, response_json):

		cars = games_commands.get_iracing_cars(response_json)

		assert cars
		assert len(cars) > 0

		car = cars[0].model_dump()

		assert "url" in car
		assert "type" in car
		assert "image" in car
		assert "is_new" in car

	def test_command_get_iracing_cars_with_empty_values(self, response_empty_json):
		without_values = 0
		cars = games_commands.get_iracing_cars(response_empty_json)

		assert not cars
		assert len(cars) == without_values

	def test_command_get_iracing_series(self, response_json):
		series = games_commands.get_iracing_series(response_json)

		assert series
		assert len(series) > 0

		serie = series[0].model_dump()

		assert "name" in serie
		assert "type" in serie

	def test_command_get_iracing_series_with_empty_values(self, response_empty_json):
		without_values = 0
		series = games_commands.get_iracing_series(response_empty_json)

		assert not series
		assert len(series) == without_values

	def test_command_get_iracing_tracks(self, response_json):
		tracks = games_commands.get_iracing_tracks(response_json)

		assert tracks
		assert len(tracks) > 0

		track = tracks[0].model_dump()

		assert "track" in track
		assert "image" in track
		assert "is_new" in track
		assert "included" in track
		assert "url" in track

	def test_command_get_iracing_tracks_with_empty_values(self, response_empty_json):
		without_values = 0
		tracks = games_commands.get_iracing_tracks(response_empty_json)

		assert not tracks
		assert len(tracks) == without_values

	def test_command_get_iracing_news(self, response_json):
		news = games_commands.get_iracing_news(response_json)

		assert news
		assert len(news) > 0

		article = news[0].model_dump()

		assert "date" in article
		assert "title" in article
		assert "image" in article
		assert "detail" in article
		assert "author" in article
		assert "url" in article

	def test_command_get_iracing_news_with_empty_values(self, response_empty_json):
		without_values = 0
		news = games_commands.get_iracing_news(response_empty_json)

		assert not news
		assert len(news) == without_values

	def test_command_get_iracing_seasons(self, response_json):
		seasons = games_commands.get_iracing_seasons(response_json)

		assert seasons
		assert len(seasons) > 0

		season = seasons[0].model_dump()

		assert "season" in season
		assert "season_url" in season
		assert "season_date" in season
		assert "is_latest" in season
		assert "image" in season

	def test_command_get_iracing_seasons_with_empty_values(self, response_empty_json):
		without_values = 0
		seasons = games_commands.get_iracing_seasons(response_empty_json)

		assert not seasons
		assert len(seasons) == without_values



class TestCommandEasport:

	def test_command_get_easport_news(self, response_json):
		news = games_commands.get_easport_news(response_json)

		assert news
		assert len(news) > 0

		article = news[0].model_dump()

		assert "tag" in article
		assert "date" in article
		assert "image" in article
		assert "title" in article
		assert "detail" in article

	def test_command_get_easport_news_with_empty_values(self, response_empty_json):
		without_values = 0
		news = games_commands.get_easport_news(response_empty_json)

		assert not news
		assert len(news) == without_values

	def test_command_get_easport_soon(self, response_json):
		new_games = games_commands.get_easport_soon(response_json)

		assert new_games
		assert len(new_games) > 0

		about_game = new_games[0].model_dump()

		assert "title" in about_game
		assert "date" in about_game
		assert "console" in about_game
		assert "genre" in about_game

	def test_command_get_easport_soon_with_empty_values(self, response_empty_json):
		without_values = 0
		new_games = games_commands.get_easport_soon(response_empty_json)

		assert not new_games
		assert len(new_games) == without_values

	def test_command_get_easport_updates(self, response_json):
		updates = games_commands.get_easport_updates(response_json)

		assert updates
		assert len(updates) > 0

		note = updates[0].model_dump()

		assert "url" in note
		assert "info" in note
		assert "date" in note
		assert "image" in note
		assert "title" in note
		assert "detail" in note

	def test_command_get_easport_updates_with_empty_values(self, response_empty_json):
		without_values = 0
		updates = games_commands.get_easport_updates(response_empty_json)

		assert not updates
		assert len(updates) == without_values


	@pytest.mark.parametrize(
		"detail",
		[
			"gratuitos",
			"novedades"
		]
	)
	def test_command_get_easport_games(self, response_json, detail):
		details = games_commands.get_easport_games(response_json, detail)

		assert details
		assert len(details) > 0

		detail_game = details[0].model_dump()

		assert "url" in detail_game
		assert "logo" in detail_game
		assert "image" in detail_game
		assert "title" in detail_game

	@pytest.mark.parametrize(
		"detail",
		[
			"gratuitos",
			"novedades"
		]
	)
	def test_command_get_easport_games_with_empty_values(self, response_empty_json, detail):
		without_values = 0
		details = games_commands.get_easport_games(response_empty_json, detail)

		assert not details
		assert len(details) == without_values