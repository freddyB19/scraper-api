import pprint
from unittest.mock import patch

import pytest
from faker import Faker

from fastapi.testclient import TestClient

from app.main import app

from tests.fixtures import (
	RESPONSE_JSON_NEWS,
	RESPONSE_EMPTY_JSON_NEWS
)

faker = Faker(locale = "es")

client = TestClient(app)

STATUS_OK = 200
HTTP_422_UNPROCESSABLE = 422

URL = "/api/v1/news"


class TestAPINewsMarca:
	def setup_method(self):
		self.url = f"{URL}/marca"
		self.params = {"size": 5}

	@patch('routes.api.v1.news.sync_get_data', lambda: RESPONSE_JSON_NEWS)
	def test_marca_games(self):
		"""
			Validar "GET /marca"
		"""
		total_elements = self.params['size']
		detail = "game"
		response = client.get(f"{self.url}/{detail}", params = self.params)

		responseJson = response.json()
		responseStatus = response.status_code

		assert responseStatus == STATUS_OK
		assert responseJson['items']
		assert len(responseJson['items']) == total_elements

		article = responseJson['items'][0]

		assert list(article.keys()) == ["url", "meta", "author", "title", "image"]

	@patch('routes.api.v1.news.sync_get_data', lambda: RESPONSE_EMPTY_JSON_NEWS)
	def test_marca_games_with_empty_values(self):
		"""
			Validar "GET /marca" con resultados vacíos
		"""
		without_values = 0
		detail = "game"
		response = client.get(f"{self.url}/{detail}", params = self.params)

		responseJson = response.json()
		responseStatus = response.status_code

		assert responseStatus == STATUS_OK
		assert not responseJson['items']
		assert len(responseJson['items']) == without_values

		assert responseJson['links']['next'] is None
		assert responseJson['links']['prev'] is None


class TestAPINewsWired:
	def setup_method(self):
		self.url = f"{URL}/wired"
		self.params = {"size": 5}

	@patch('routes.api.v1.news.sync_get_data', lambda: RESPONSE_JSON_NEWS)
	@pytest.mark.parametrize(
		"detail",
		[
			"robots",
			"espacio",
			"neurociencia",
			"biotecnología"
		]
	)
	def test_wired(self, detail):
		"""
			Validar "GET /wired/:detail"
		"""
		total_elements = self.params['size']
		response = client.get(f"{self.url}/{detail}", params = self.params)

		responseJson = response.json()
		responseStatus = response.status_code

		assert responseStatus == STATUS_OK
		assert responseJson['items']
		assert len(responseJson['items']) == total_elements

		note = responseJson['items'][0]

		assert list(note.keys()) == ["url", "title", "image", "detail"]

	@patch('routes.api.v1.news.sync_get_data', lambda: RESPONSE_EMPTY_JSON_NEWS)
	@pytest.mark.parametrize(
		"detail",
		[
			"robots",
			"espacio",
			"neurociencia",
			"biotecnología"
		]
	)
	def test_wired_with_empty_values(self, detail):
		"""
			Validar "GET /wired/:detail" con resultados vacíos
		"""
		without_values = 0
		response = client.get(f"{self.url}/{detail}", params = self.params)

		responseJson = response.json()
		responseStatus = response.status_code

		assert responseStatus == STATUS_OK
		assert not responseJson['items']
		assert len(responseJson['items']) == without_values

		assert responseJson['links']['next'] is None
		assert responseJson['links']['prev'] is None

	@patch('routes.api.v1.news.sync_get_data', lambda: RESPONSE_JSON_NEWS)
	def test_wired_with_wrong_page(self):
		"""
			Generar [Error 422] "GET /wired/:detail" por query_param invalido
		"""
		detail = faker.word()
		response = client.get(f"{self.url}/{detail}", params = self.params)

		responseJson = response.json()
		responseStatus = response.status_code

		assert responseStatus == HTTP_422_UNPROCESSABLE

class TestAPINewsLaNacion:

	def setup_method(self):
		self.url = f"{URL}/nacion"
		self.params = {"size": 5}

	@patch('routes.api.v1.news.sync_get_data', lambda: RESPONSE_JSON_NEWS)
	@pytest.mark.parametrize(
		"detail", [
			"juegos",
			"tecnologia"
		]
	)
	def test_lanacion(self, detail):
		"""
			Validar "GET /nacion/:detail"
		"""
		total_elements = self.params['size']
		response = client.get(f"{self.url}/{detail}", params = self.params)

		responseJson = response.json()
		responseStatus = response.status_code

		assert responseStatus == STATUS_OK
		assert responseJson['items']
		assert len(responseJson['items']) == total_elements

		note = responseJson['items'][0]

		assert list(note.keys()) == ["url", "date", "image", "title"]

	@patch('routes.api.v1.news.sync_get_data', lambda: RESPONSE_EMPTY_JSON_NEWS)
	@pytest.mark.parametrize(
		"detail", [
			"juegos",
			"tecnologia"
		]
	)
	def test_lanacion_with_empty_values(self, detail):
		"""
			Validar "GET /nacion/:detail" con resultados vacíos
		"""
		without_values = 0
		response = client.get(f"{self.url}/{detail}", params = self.params)

		responseJson = response.json()
		responseStatus = response.status_code

		assert responseStatus == STATUS_OK
		assert not responseJson['items']
		assert len(responseJson['items']) == without_values

		assert responseJson['links']['next'] is None
		assert responseJson['links']['prev'] is None

	@patch('routes.api.v1.news.sync_get_data', lambda: RESPONSE_JSON_NEWS)
	def test_lanacion_with_wrong_page(self):
		"""
			Generar [Error 422] "GET /nacion/:detail" por query_param invalido
		"""
		detail = faker.word()
		response = client.get(f"{self.url}/{detail}", params = self.params)

		responseJson = response.json()
		responseStatus = response.status_code

		assert responseStatus == HTTP_422_UNPROCESSABLE
