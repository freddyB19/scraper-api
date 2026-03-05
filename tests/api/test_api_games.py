import pprint
from unittest.mock import patch

import pytest

from fastapi.testclient import TestClient

from app.main import app

from tests.fixtures import (
	RESPONSE_JSON_GAMES, 
	RESPONSE_EMPTY_JSON_GAMES
)


client = TestClient(app)

STATUS_OK = 200
URL = "/api/v1/game"

class TestAPIGameLol:
	def setup_method(self):
		self.url = f"{URL}/lol"
		self.params = {"size": 5} # page

	@patch('routes.api.v1.games.sync_get_data', lambda: RESPONSE_JSON_GAMES)	
	def test_lol_champion(self):
		detail = "champions"
		
		response = client.get(f"{self.url}/{detail}", params = self.params)

		responseJson = response.json()
		responseStatus = response.status_code
		total_elements = self.params["size"]

		assert responseStatus == STATUS_OK
		assert responseJson['items']
		assert len(responseJson['items']) == total_elements

		champion = responseJson['items'][0]

		assert list(champion.keys()) == ["name", "url", "images"]

	@patch('routes.api.v1.games.sync_get_data', lambda: RESPONSE_JSON_GAMES)
	@pytest.mark.parametrize(
		"detail",
		[
			"noticias",
			"notas"
		]
	)
	def test_lol_articles(self, detail):
		response = client.get(f"{self.url}/{detail}", params = self.params)

		responseJson = response.json()
		responseStatus = response.status_code
		total_elements = self.params["size"]

		assert responseStatus == STATUS_OK
		assert responseJson['items']
		assert len(responseJson['items']) == total_elements

		article = responseJson['items'][0]
		
		assert list(article.keys()) == ["url", "date", "title", "detail", "category"]

	@patch('routes.api.v1.games.sync_get_data', lambda: RESPONSE_EMPTY_JSON_GAMES)
	@pytest.mark.parametrize(
		"detail",
		[
			"notas",
			"noticias",
			"champions"
		]
	)
	def test_lol_articles_with_empty_values(self, detail):
		without_values = 0
		
		response = client.get(f"{self.url}/{detail}")

		responseJson = response.json()
		responseStatus = response.status_code

		assert responseStatus == STATUS_OK
		assert not responseJson['items']
		assert len(responseJson['items']) == without_values

		assert responseJson['links']['next'] is None
		assert responseJson['links']['prev'] is None


class TestAPIGameEasport:
	def setup_method(self):
		self.url = f"{URL}/easport"
		self.params = {"size": 5} # page

	@patch('routes.api.v1.games.sync_get_data', lambda: RESPONSE_JSON_GAMES)
	def test_easport_news(self):
		detail = "news"
		response = client.get(f"{self.url}/{detail}", params = self.params)

		responseJson = response.json()
		responseStatus = response.status_code
		total_elements = self.params['size']

		assert responseStatus == STATUS_OK
		assert responseJson['items']
		assert len(responseJson['items']) == total_elements

		article = responseJson['items'][0]

		assert list(article.keys()) == ['tag', 'date', 'image', 'title', 'detail']

	@patch('routes.api.v1.games.sync_get_data', lambda: RESPONSE_JSON_GAMES)
	@pytest.mark.parametrize(
		"detail",
		[
			"gratuitos",
			"novedades"
		]
	)
	def test_easport_games(self, detail):
		response = client.get(f"{self.url}/games/{detail}", params = self.params)

		responseJson = response.json()
		responseStatus = response.status_code
		total_elements = self.params['size']

		assert responseStatus == STATUS_OK
		assert responseJson['items']
		assert len(responseJson['items']) == total_elements

		article = responseJson['items'][0]

		assert list(article.keys()) == ["url", "logo", "image", "title"]

	@patch('routes.api.v1.games.sync_get_data', lambda: RESPONSE_JSON_GAMES)
	def test_easport_soon(self):
		detail = "soon"
		response = client.get(f"{self.url}/{detail}", params = self.params)

		responseJson = response.json()
		responseStatus = response.status_code
		total_elements = self.params['size']

		assert responseStatus == STATUS_OK
		assert responseJson['items']
		assert len(responseJson['items']) == total_elements

		game = responseJson['items'][0]

		assert list(game.keys()) == ["title", "date", "console", "genre"]

	@patch('routes.api.v1.games.sync_get_data', lambda: RESPONSE_JSON_GAMES)
	def test_easport_updates(self):
		detail = "updates"
		response = client.get(f"{self.url}/{detail}", params = self.params)

		responseJson = response.json()
		responseStatus = response.status_code
		total_elements = self.params['size']

		assert responseStatus == STATUS_OK
		assert responseJson['items']
		assert len(responseJson['items']) == total_elements

		note = responseJson['items'][0]

		assert list(note.keys()) == ["url", "info", "date", "image", "title", "detail"]

	@patch('routes.api.v1.games.sync_get_data', lambda: RESPONSE_EMPTY_JSON_GAMES)
	@pytest.mark.parametrize(
		"detail",
		[
			"news",
			"soon",
			"updates",
		]
	)
	def test_easport_detail_with_empty_values(self, detail):
		without_values = 0
		response = client.get(f"{self.url}/{detail}")

		responseJson = response.json()
		responseStatus = response.status_code

		assert responseStatus == STATUS_OK
		assert not responseJson['items']
		assert len(responseJson['items']) == without_values

		assert responseJson['links']['next'] is None
		assert responseJson['links']['prev'] is None

	@patch('routes.api.v1.games.sync_get_data', lambda: RESPONSE_EMPTY_JSON_GAMES)
	@pytest.mark.parametrize(
		"detail",
		[
			"gratuitos",
			"novedades",
		]
	)
	def test_easport_games_with_empty_values(self, detail):
		without_values = 0
		response = client.get(f"{self.url}/games/{detail}")

		responseJson = response.json()
		responseStatus = response.status_code

		assert responseStatus == STATUS_OK
		assert not responseJson['items']
		assert len(responseJson['items']) == without_values

		assert responseJson['links']['next'] is None
		assert responseJson['links']['prev'] is None


class TestAPIGameIracing:
	def setup_method(self):
		self.url = f"{URL}/iracing"
		self.params = {"size": 5}

	@patch('routes.api.v1.games.sync_get_data', lambda: RESPONSE_JSON_GAMES)
	def test_iracing_cars(self):
		detail = "cars"
		total_elements = self.params['size']
		
		response = client.get(f"{self.url}/{detail}", params = self.params)

		responseJson = response.json()
		responseStatus = response.status_code

		assert responseStatus == STATUS_OK
		assert responseJson['items']
		assert len(responseJson['items']) == total_elements

		article = responseJson['items'][0]

		assert list(article.keys()) == ["url", "type", "image", "is_new"]

	@patch('routes.api.v1.games.sync_get_data', lambda: RESPONSE_JSON_GAMES)
	def test_iracing_tracks(self):
		detail = "tracks"
		total_elements = self.params['size']
		
		response = client.get(f"{self.url}/{detail}", params = self.params)

		responseJson = response.json()
		responseStatus = response.status_code

		assert responseStatus == STATUS_OK
		assert responseJson['items']
		assert len(responseJson['items']) == total_elements

		track = responseJson['items'][0]

		assert list(track.keys()) == ["url", "track", "image", "is_new", "included"]

	@patch('routes.api.v1.games.sync_get_data', lambda: RESPONSE_JSON_GAMES)
	def test_iracing_series(self):
		detail = "series"
		total_elements = self.params['size']
		
		response = client.get(f"{self.url}/{detail}", params = self.params)

		responseJson = response.json()
		responseStatus = response.status_code

		assert responseStatus == STATUS_OK
		assert responseJson['items']
		assert len(responseJson['items']) == total_elements

		serie = responseJson['items'][0]

		assert list(serie.keys()) == ["name", "type"]

	@patch('routes.api.v1.games.sync_get_data', lambda: RESPONSE_JSON_GAMES)
	def test_iracing_seasons(self):
		detail = "seasons"
		total_elements = self.params['size']
		
		response = client.get(f"{self.url}/{detail}", params = self.params)

		responseJson = response.json()
		responseStatus = response.status_code

		assert responseStatus == STATUS_OK
		assert responseJson['items']
		assert len(responseJson['items']) == total_elements

		season = responseJson['items'][0]

		assert list(season.keys()) == ["image", "season", "season_url", "season_date", "is_latest"]

	@patch('routes.api.v1.games.sync_get_data', lambda: RESPONSE_JSON_GAMES)
	def test_iracing_news(self):
		detail = "news"
		total_elements = self.params['size']

		response = client.get(f"{self.url}/{detail}", params = self.params)

		responseJson = response.json()
		responseStatus = response.status_code

		assert responseStatus == STATUS_OK
		assert responseJson['items']
		assert len(responseJson['items']) == total_elements

		article = responseJson['items'][0]

		assert list(article.keys()) == ["url", "date", "title", "image", "detail", "author"]

	@patch('routes.api.v1.games.sync_get_data', lambda: RESPONSE_EMPTY_JSON_GAMES)
	@pytest.mark.parametrize(
		"detail",
		[
			"news", 
			"cars",
			"tracks",
			"series",
			"seasons"
		]
	)
	def test_iracing_with_empty_values(self, detail):
		without_values = 0

		response = client.get(f"{self.url}/{detail}")

		responseJson = response.json()
		responseStatus = response.status_code

		assert responseStatus == STATUS_OK
		assert not responseJson['items']
		assert len(responseJson['items']) == without_values

		assert responseJson['links']['next'] is None
		assert responseJson['links']['prev'] is None