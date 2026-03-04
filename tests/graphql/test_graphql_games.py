import pprint

import pytest, httpx

from app.routes.graphql.schemas import schema

from tests.fixtures import (
	RESPONSE_JSON_GAMES, 
	RESPONSE_EMPTY_JSON_GAMES
)
from tests.graphql.utils.querys import (
	LOL_NEWS,
	LOL_NOTES,
	LOL_CHAMPIONS,
	IRACING_CARS,
	IRACING_NEWS,
	IRACING_TRACKS,
	IRACING_SERIES,
	IRACING_SEASONS,
	EASPORT_NEWS,
	EASPORT_SOON,
	EASPORT_FREE,
	EASPORT_UPDATES,
	EASPORT_NOVELTIES
)

class MockResponse:
	@staticmethod
	def raise_for_status():
		assert True

	@staticmethod
	def json():
		return RESPONSE_JSON_GAMES


@pytest.fixture
def mock_response(monkeypatch):
	def mock_get(*args, **kwargs):
		return MockResponse()

	monkeypatch.setattr(httpx.Client, "get", mock_get)

class MockEmptyResponse:
	@staticmethod
	def raise_for_status():
		assert True

	@staticmethod
	def json():
		return RESPONSE_EMPTY_JSON_GAMES


@pytest.fixture
def mock_empty_response(monkeypatch):
	def mock_get(*args, **kwargs):
		return MockEmptyResponse()

	monkeypatch.setattr(httpx.Client, "get", mock_get)


class TestGameLol:

	def test_game_lol_champions(self, mock_response):
		query = LOL_CHAMPIONS
		total_element = 5
		response = schema.execute_sync(
			query,
			variable_values = {"count": total_element}
		)

		responseErrors = response.errors
		assert not responseErrors

		responseData = response.data["lol"]
		assert "champions" in responseData
		assert responseData["champions"]["edges"]
		assert len(responseData["champions"]["edges"]) == total_element

		champion = responseData["champions"]["edges"][0]

		assert "images" in champion["node"]
		assert "name" in champion["node"]
		assert "url" in champion["node"]

		assert "hasNextPage" in responseData["champions"]["pageInfo"]
		assert "hasPreviousPage" in responseData["champions"]["pageInfo"]

	def test_game_lol_news(self, mock_response):
		query = LOL_NEWS
		total_element = 5
		detail = "news"
		
		response = schema.execute_sync(
			query,
			variable_values = {"count": total_element}
		)

		responseErrors = response.errors
		assert not responseErrors

		responseData = response.data["lol"]
		assert detail in responseData

		assert responseData[detail]["edges"]
		assert len(responseData[detail]["edges"]) == total_element

		news = responseData[detail]["edges"][0]

		assert "category" in news["node"]
		assert "date" in news["node"]
		assert "detail" in news["node"]
		assert "title" in news["node"]
		assert "url" in news["node"]

		assert "hasNextPage" in responseData[detail]["pageInfo"]
		assert "hasPreviousPage" in responseData[detail]["pageInfo"]

	def test_game_lol_notes(self, mock_response):
		query = LOL_NOTES
		total_element = 5
		detail = "notes"
		response = schema.execute_sync(
			query,
			variable_values = {"count": total_element}
		)

		responseErrors = response.errors
		assert not responseErrors

		responseData = response.data["lol"]
		assert detail in responseData

		assert responseData[detail]["edges"]
		assert len(responseData[detail]["edges"]) == total_element

		note = responseData[detail]["edges"][0]

		assert "category" in note["node"]
		assert "date" in note["node"]
		assert "detail" in note["node"]
		assert "title" in note["node"]
		assert "url" in note["node"]

		assert "hasNextPage" in responseData[detail]["pageInfo"]
		assert "hasPreviousPage" in responseData[detail]["pageInfo"]

	@pytest.mark.parametrize(
		"query,detail",
		[
			(LOL_NEWS, "news"),
			(LOL_NOTES, "notes"),
			(LOL_CHAMPIONS, "champions"),

		]
	)
	def test_game_lol_with_empty_values(self, mock_empty_response, query, detail):
		game = "lol"
		without_values = 0
		
		response = schema.execute_sync(query)

		responseErrors = response.errors
		assert not responseErrors

		responseData = response.data[game]
		assert detail in responseData
		assert not responseData[detail]["edges"]
		assert len(responseData[detail]["edges"]) == without_values


class TestGameEasport:

	def test_game_easport_free(self, mock_response):
		query = EASPORT_FREE
		game = "easport"
		detail = "free"
		total_element = 5

		response = schema.execute_sync(
			query, 
			variable_values = {"count": total_element}
		)

		responseErrors = response.errors
		assert not responseErrors

		responseData = response.data[game]
		assert detail in responseData

		assert responseData[detail]["edges"]
		assert len(responseData[detail]["edges"]) == total_element

		detail_game = responseData[detail]["edges"][0]

		assert "image" in detail_game["node"]
		assert "logo" in detail_game["node"]
		assert "title" in detail_game["node"]
		assert "url" in detail_game["node"]

		assert "hasNextPage" in responseData[detail]["pageInfo"]
		assert "hasPreviousPage" in responseData[detail]["pageInfo"]

	def test_game_easport_news(self, mock_response):
		query = EASPORT_NEWS
		game = "easport"
		detail = "news"
		total_element = 5

		response = schema.execute_sync(
			query,
			variable_values = {"count": total_element}
		)

		responseErrors = response.errors
		assert not responseErrors

		responseData = response.data[game]
		assert detail in responseData

		assert responseData[detail]["edges"]
		assert len(responseData[detail]["edges"]) == total_element

		detail_game = responseData[detail]["edges"][0]

		assert "date" in detail_game["node"]
		assert "detail" in detail_game["node"]
		assert "image" in detail_game["node"]
		assert "tag" in detail_game["node"]
		assert "title" in detail_game["node"]

		assert "hasNextPage" in responseData[detail]["pageInfo"]
		assert "hasPreviousPage" in responseData[detail]["pageInfo"]

	def test_game_easport_novelties(self, mock_response):
		query = EASPORT_NOVELTIES
		game = "easport"
		detail = "novelties"
		total_element = 5

		response = schema.execute_sync(
			query,
			variable_values = {"count": total_element}
		)

		responseErrors = response.errors
		assert not responseErrors

		responseData = response.data[game]
		assert detail in responseData

		assert responseData[detail]["edges"]
		assert len(responseData[detail]["edges"]) == total_element

		detail_game = responseData[detail]["edges"][0]

		assert "image" in detail_game["node"]
		assert "logo" in detail_game["node"]
		assert "title" in detail_game["node"]
		assert "url" in detail_game["node"]

		assert "hasNextPage" in responseData[detail]["pageInfo"]
		assert "hasPreviousPage" in responseData[detail]["pageInfo"]

	def test_game_easport_soon(self, mock_response):
		query = EASPORT_SOON
		game = "easport"
		detail = "soon"
		total_element = 5

		response = schema.execute_sync(
			query,
			variable_values = {"count": total_element}
		)

		responseErrors = response.errors
		assert not responseErrors

		responseData = response.data[game]
		assert detail in responseData

		assert responseData[detail]["edges"]
		assert len(responseData[detail]["edges"]) == total_element

		detail_game = responseData[detail]["edges"][0]

		assert "console" in detail_game["node"]
		assert "date" in detail_game["node"]
		assert "genre" in detail_game["node"]
		assert "title" in detail_game["node"]

		assert "hasNextPage" in responseData[detail]["pageInfo"]
		assert "hasPreviousPage" in responseData[detail]["pageInfo"]

	def test_game_easport_updates(self, mock_response):
		query = EASPORT_UPDATES
		game = "easport"
		detail = "updates"
		total_element = 5

		response = schema.execute_sync(
			query,
			variable_values = {"count": total_element}
		)

		responseErrors = response.errors
		assert not responseErrors

		responseData = response.data[game]
		assert detail in responseData

		assert responseData[detail]["edges"]
		assert len(responseData[detail]["edges"]) == total_element

		detail_game = responseData[detail]["edges"][0]

		assert "date" in detail_game["node"]
		assert "detail" in detail_game["node"]
		assert "image" in detail_game["node"]
		assert "info" in detail_game["node"]
		assert "title" in detail_game["node"]
		assert "url" in detail_game["node"]

		assert "hasNextPage" in responseData[detail]["pageInfo"]
		assert "hasPreviousPage" in responseData[detail]["pageInfo"]

	@pytest.mark.parametrize(
		"query,detail",
		[
			(EASPORT_NEWS, "news"),
			(EASPORT_SOON, "soon"),
			(EASPORT_FREE, "free"),
			(EASPORT_UPDATES, "updates"),
			(EASPORT_NOVELTIES, "novelties"),
		]
	)
	def test_game_easport_with_empty_values(self, mock_empty_response, query, detail):
		game = "easport"
		without_values = 0

		response = schema.execute_sync(query)

		responseErrors = response.errors
		assert not responseErrors

		responseData = response.data[game]
		assert detail in responseData
		assert not responseData[detail]["edges"]
		assert len(responseData[detail]["edges"]) == without_values


class TestGameIracing:

	def test_game_iracing_cars(self, mock_response):
		query = IRACING_CARS
		game = "iracing"
		detail = "cars"
		total_element = 5

		response = schema.execute_sync(
			query, 
			variable_values = {"count": total_element}
		)

		responseErrors = response.errors
		assert not responseErrors

		responseData = response.data[game]
		assert detail in responseData

		assert responseData[detail]["edges"]
		assert len(responseData[detail]["edges"]) == total_element

		detail_game = responseData[detail]["edges"][0]

		assert "image" in detail_game["node"]
		assert "isNew" in detail_game["node"]
		assert "type" in detail_game["node"]
		assert "url" in detail_game["node"]

		assert "hasNextPage" in responseData[detail]["pageInfo"]
		assert "hasPreviousPage" in responseData[detail]["pageInfo"]

	def test_game_iracing_tracks(self, mock_response):
		query = IRACING_TRACKS
		game = "iracing"
		detail = "tracks"
		total_element = 5

		response = schema.execute_sync(
			query, 
			variable_values = {"count": total_element}
		)

		responseErrors = response.errors
		assert not responseErrors

		responseData = response.data[game]
		assert detail in responseData

		assert responseData[detail]["edges"]
		assert len(responseData[detail]["edges"]) == total_element

		detail_game = responseData[detail]["edges"][0]

		assert "image" in detail_game["node"]
		assert "included" in detail_game["node"]
		assert "isNew" in detail_game["node"]
		assert "track" in detail_game["node"]
		assert "url" in detail_game["node"]

		assert "hasNextPage" in responseData[detail]["pageInfo"]
		assert "hasPreviousPage" in responseData[detail]["pageInfo"]

	def test_game_iracing_series(self, mock_response):
		query = IRACING_SERIES
		game = "iracing"
		detail = "series"
		total_element = 5

		response = schema.execute_sync(
			query, 
			variable_values = {"count": total_element}
		)

		responseErrors = response.errors
		assert not responseErrors

		responseData = response.data[game]
		assert detail in responseData

		assert responseData[detail]["edges"]
		assert len(responseData[detail]["edges"]) == total_element

		detail_game = responseData[detail]["edges"][0]

		assert "name" in detail_game["node"]
		assert "type" in detail_game["node"]
		
		assert "hasNextPage" in responseData[detail]["pageInfo"]
		assert "hasPreviousPage" in responseData[detail]["pageInfo"]

	def test_game_iracing_seasons(self, mock_response):
		query = IRACING_SEASONS
		game = "iracing"
		detail = "seasons"
		total_element = 5

		response = schema.execute_sync(
			query, 
			variable_values = {"count": total_element}
		)

		responseErrors = response.errors
		assert not responseErrors

		responseData = response.data[game]
		assert detail in responseData

		assert responseData[detail]["edges"]
		assert len(responseData[detail]["edges"]) == total_element

		detail_game = responseData[detail]["edges"][0]

		assert "image" in detail_game["node"]
		assert "isLatest" in detail_game["node"]
		assert "season" in detail_game["node"]
		assert "seasonDate" in detail_game["node"]
		assert "seasonUrl" in detail_game["node"]

		assert "hasNextPage" in responseData[detail]["pageInfo"]
		assert "hasPreviousPage" in responseData[detail]["pageInfo"]

	def test_game_iracing_news(self, mock_response):
		query = IRACING_NEWS
		game = "iracing"
		detail = "news"
		total_element = 5

		response = schema.execute_sync(
			query, 
			variable_values = {"count": total_element}
		)

		responseErrors = response.errors
		assert not responseErrors

		responseData = response.data[game]
		assert detail in responseData

		assert responseData[detail]["edges"]
		assert len(responseData[detail]["edges"]) == total_element

		detail_game = responseData[detail]["edges"][0]

		assert "author" in detail_game["node"]
		assert "date" in detail_game["node"]
		assert "detail" in detail_game["node"]
		assert "image" in detail_game["node"]
		assert "title" in detail_game["node"]
		assert "url" in detail_game["node"]

		assert "hasNextPage" in responseData[detail]["pageInfo"]
		assert "hasPreviousPage" in responseData[detail]["pageInfo"]

	@pytest.mark.parametrize(
		"query,detail",
		[
			(IRACING_CARS, "cars"),
			(IRACING_NEWS, "news"),
			(IRACING_TRACKS, "tracks"),
			(IRACING_SERIES, "series"),
			(IRACING_SEASONS, "seasons")
		]
	)
	def test_game_iracing_with_empty_values(self, mock_empty_response, query, detail):
		game = "iracing"
		without_values = 0
		response = schema.execute_sync(query)

		responseErrors = response.errors
		assert not responseErrors

		responseData = response.data[game]
		assert detail in responseData
		assert not responseData[detail]["edges"]
		assert len(responseData[detail]["edges"]) == without_values
