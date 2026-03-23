import pprint

import pytest, httpx

from app.routes.graphql.schemas import schema

from tests.fixtures import (
	RESPONSE_JSON_NEWS,
	RESPONSE_EMPTY_JSON_NEWS
)

from tests.graphql.utils.querys import(
	MARCA_GAMES,
	LANACION_TEC,
	LANACION_GAMES,
	WIRED_BIO,
	WIRED_SPACE,
	WIRED_NEURO,
	WIRED_ROBOTS
)

class MockResponse:
	@staticmethod
	def raise_for_status():
		assert True

	@staticmethod
	def json():
		return RESPONSE_JSON_NEWS


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
		return RESPONSE_EMPTY_JSON_NEWS


@pytest.fixture
def mock_empty_response(monkeypatch):
	def mock_get(*args, **kwargs):
		return MockEmptyResponse()

	monkeypatch.setattr(httpx.Client, "get", mock_get)


class TestNewsMarca:
	def test_news_marca(self, mock_response):
		query = MARCA_GAMES
		total_element = 5
		news = "marca"
		detail_news = "games"
		response = schema.execute_sync(
			query,
			variable_values = {"count": total_element}
		)

		responseErrors = response.errors
		assert not responseErrors

		responseData = response.data[news]
		assert responseData[detail_news]["edges"]
		assert len(responseData[detail_news]["edges"]) == total_element

		article = responseData[detail_news]["edges"][0]

		assert "title" in article["node"]
		assert "url" in article["node"]
		assert "image" in article["node"]
		assert "meta" in article["node"]
		assert "author" in article["node"]
		assert None not in article["node"].values()

		assert "hasNextPage" in responseData[detail_news]["pageInfo"]
		assert "hasPreviousPage" in responseData[detail_news]["pageInfo"]

	def test_news_marca_with_empty_values(self, mock_empty_response):
		query = MARCA_GAMES
		without_values = 0
		news = "marca"
		detail_news = "games"
		
		response = schema.execute_sync(query)

		responseErrors = response.errors
		assert not responseErrors

		responseData = response.data[news]
		assert not responseData[detail_news]["edges"]
		assert len(responseData[detail_news]["edges"]) == without_values


class TestNewsLaNacion:
	@pytest.mark.parametrize(
		"query,detail",
		[
			(LANACION_GAMES, "games"),
			(LANACION_TEC, "tecnology")
		]
	)
	def test_news_lanacion(self, mock_response, query, detail):
		total_element = 5
		news = "lanacion"

		response = schema.execute_sync(
			query,
			variable_values = {"count": total_element}
		)

		responseErrors = response.errors
		assert not responseErrors

		responseData = response.data[news]
		assert responseData[detail]["edges"]
		assert len(responseData[detail]["edges"]) == total_element

		article = responseData[detail]["edges"][0]

		assert "url" in article["node"]
		assert "date" in article["node"]
		assert "image" in article["node"]
		assert "title" in article["node"]
		assert None not in article["node"].values()

		assert "hasNextPage" in responseData[detail]["pageInfo"]
		assert "hasPreviousPage" in responseData[detail]["pageInfo"]

	@pytest.mark.parametrize(
		"query,detail",
		[
			(LANACION_GAMES, "games"),
			(LANACION_TEC, "tecnology")
		]
	)
	def test_news_lanacion_with_empty_values(self, mock_empty_response, query, detail):
		without_values = 0
		news = "lanacion"
	
		response = schema.execute_sync(query)

		responseErrors = response.errors
		assert not responseErrors

		responseData = response.data[news]
		assert not responseData[detail]["edges"]
		assert len(responseData[detail]["edges"]) == without_values

class TestNewsWired:
	@pytest.mark.parametrize(
		"query,detail",
		[
			(WIRED_SPACE, "space"),
			(WIRED_ROBOTS, "robots"),
			(WIRED_BIO, "biotechnology"),
			(WIRED_NEURO, "neuroscience"),
		]
	)
	def test_news_wired(self, mock_response, query, detail):
		total_element = 5
		news = "wired"

		response = schema.execute_sync(
			query,
			variable_values = {"count": total_element}
		)

		responseErrors = response.errors
		assert not responseErrors

		responseData = response.data[news]
		assert responseData[detail]["edges"]
		assert len(responseData[detail]["edges"]) == total_element

		article = responseData[detail]["edges"][0]

		assert "url" in article["node"]
		assert "detail" in article["node"]
		assert "image" in article["node"]
		assert "title" in article["node"]
		assert None not in article["node"].values()

		assert "hasNextPage" in responseData[detail]["pageInfo"]
		assert "hasPreviousPage" in responseData[detail]["pageInfo"]

	@pytest.mark.parametrize(
		"query,detail",
		[
			(WIRED_SPACE, "space"),
			(WIRED_ROBOTS, "robots"),
			(WIRED_BIO, "biotechnology"),
			(WIRED_NEURO, "neuroscience"),
		]
	)
	def test_news_wired_with_empty_values(self, mock_empty_response, query, detail):
		without_values = 0
		news = "wired"
	
		response = schema.execute_sync(query)

		responseErrors = response.errors
		assert not responseErrors

		responseData = response.data[news]
		assert not responseData[detail]["edges"]
		assert len(responseData[detail]["edges"]) == without_values
