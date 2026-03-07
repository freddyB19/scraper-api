import pprint

import pytest
from faker import Faker

from app.services import news_commands

from tests.fixtures import (
	RESPONSE_JSON_NEWS,
	RESPONSE_EMPTY_JSON_NEWS
)

@pytest.fixture
def response_json():
	return RESPONSE_JSON_NEWS

@pytest.fixture
def response_empty_json():
	return RESPONSE_EMPTY_JSON_NEWS

faker = Faker(locale = "es")


class TestCommandNewsMarca:

	def test_command_get_marca_videogames(self, response_json):
		without_values = 0
		notes = news_commands.get_marca_videogames(response_json)

		assert notes
		assert len(notes) > without_values

		note = notes[0].model_dump()

		assert list(note.keys()) == ["url", "meta", "author", "title", "image"]


	def test_command_get_marca_videogames_with_empty_values(self, response_empty_json):
		without_values = 0
		notes = news_commands.get_marca_videogames(response_empty_json)

		assert not notes
		assert len(notes) == without_values


class TestCommandNewsWired:

	@pytest.mark.parametrize(
		"page",
		[
			"robots",
			"espacio",
			"neurociencia",
			"biotecnología"
		]
	)
	def test_command_get_wired(self, response_json, page):
		without_values = 0
		notes = news_commands.get_wired_articles(response_json, page = page)

		assert notes
		assert len(notes) > without_values

		note = notes[0].model_dump()

		assert list(note.keys()) == ["url", "title", "image", "detail"]

	@pytest.mark.parametrize(
		"page",
		[
			"robots",
			"espacio",
			"neurociencia",
			"biotecnología"
		]
	)
	def test_command_get_wired(self, response_empty_json, page):
		without_values = 0
		notes = news_commands.get_wired_articles(response_empty_json, page = page)

		assert not notes
		assert len(notes) == without_values

	@pytest.mark.xfail()
	def test_command_get_wired_with_wrong_page(self, response_json):
		page = faker.word()
		_ = news_commands.get_wired_articles(response_json, page = page)



class TestCommandNewsLaNacion:

	@pytest.mark.parametrize(
		"page",
		[
			"juegos",
			"tecnologia"
		]
	)
	def test_command_get_lanacion(self, response_json, page):
		without_values = 0
		notes = news_commands.get_lanacion_articles(response_json, page = page)

		assert notes
		assert len(notes) > without_values

		note = notes[0].model_dump()

		assert list(note.keys()) == ["url", "date", "image", "title"]

	@pytest.mark.parametrize(
		"page",
		[
			"juegos",
			"tecnologia"
		]
	)
	def test_command_get_lanacion_with_empty_values(self, response_empty_json, page):
		without_values = 0
		notes = news_commands.get_lanacion_articles(response_empty_json, page = page)

		assert not notes
		assert len(notes) == without_values

	@pytest.mark.xfail
	def test_command_get_lanacion_with_wrong_page(self, response_json):
		page = faker.word()
		_ = news_commands.get_lanacion_articles(response_json, page = page)
