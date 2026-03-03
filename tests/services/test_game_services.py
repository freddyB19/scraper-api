import pytest
from faker import Faker

from app.services.games_services import get_data_game

from tests.fixtures import RESPONSE_JSON_GAMES

faker = Faker(locale="es")

@pytest.fixture
def response_json():
	return RESPONSE_JSON_GAMES


def test_get_lol_champions(response_json):
	game = "lol"
	detail_game = "champions"
	champions = get_data_game(response_json, game=game, detail_game = detail_game)

	assert champions

	champion = champions[0]

	assert "champion" in champion
	assert "url" in champion
	assert "images" in champion

def test_get_lol_news(response_json):
	game = "lol"
	detail_game = "noticias"
	news = get_data_game(response_json, game=game, detail_game = detail_game)

	assert news

	article = news[0]

	assert "titulo" in article
	assert "url" in article
	assert "categoria" in article
	assert "fecha" in article
	assert "detalle" in article

def test_get_lol_notes(response_json):
	game = "lol"
	detail_game = "notas"
	notes = get_data_game(response_json, game=game, detail_game = detail_game)

	assert notes

	article = notes[0]

	assert "titulo" in article
	assert "url" in article
	assert "categoria" in article
	assert "fecha" in article
	assert "detalle" in article

def test_get_easport_news(response_json):
	game = "easport"
	detail_game = "noticias"
	detail = get_data_game(response_json, game=game, detail_game = detail_game)

	assert detail

	news = detail[0]

	assert "imagen" in news
	assert "titulo" in news
	assert "etiqueta" in news
	assert "fecha" in news
	assert "descripcion" in news

def test_get_easport_novelties(response_json):
	game = "easport"
	detail_game = "novedades"
	detail = get_data_game(response_json, game=game, detail_game = detail_game)

	assert detail
	novelty = detail[0]

	assert "imagen" in novelty
	assert "titulo" in novelty
	assert "url" in novelty
	assert "logo" in novelty

def test_get_easport_soon(response_json):
	game = "easport"
	detail_game = "proximamente"
	detail = get_data_game(response_json, game=game, detail_game = detail_game)

	assert detail
	soon = detail[0]

	assert "titulo" in soon
	assert "fecha" in soon
	assert "plataformas" in soon
	assert "genero" in soon

def test_get_easport_free(response_json):
	game = "easport"
	detail_game = "gratuitos"
	detail = get_data_game(response_json, game=game, detail_game = detail_game)

	assert detail
	free = detail[0]

	assert "imagen" in free
	assert "titulo" in free
	assert "url" in free
	assert "logo" in free

def test_get_easport_updates(response_json):
	game = "easport"
	detail_game = "actualizaciones"
	detail = get_data_game(response_json, game=game, detail_game = detail_game)

	assert detail
	update = detail[0]

	assert "imagen" in update
	assert "titulo" in update
	assert "url" in update
	assert "logo" in update
	assert "informacion" in update
	assert "fecha" in update
	assert "detalle" in update

def test_get_iracing_news(response_json):
	game = "iracing"
	detail_game = "news"
	detail = get_data_game(response_json, game=game, detail_game = detail_game)

	assert detail

	article = detail[0]

	assert "title" in article
	assert "url" in article
	assert "image" in article
	assert "author" in article
	assert "detail" in article
	assert "date" in article

def test_get_iracing_cars(response_json):
	game = "iracing"
	detail_game = "cars"
	detail = get_data_game(response_json, game=game, detail_game = detail_game)

	assert detail
	car = detail[0]

	assert "type" in car
	assert "url" in car
	assert "image" in car
	assert "is_new" in car

def test_get_iracing_tracks(response_json):
	game = "iracing"
	detail_game = "tracks"
	detail = get_data_game(response_json, game=game, detail_game = detail_game)

	assert detail
	track = detail[0]

	assert "track" in track
	assert "url" in track
	assert "image" in track
	assert "is_new" in track
	assert "included" in track

def test_get_iracing_series(response_json):
	game = "iracing"
	detail_game = "series"
	detail = get_data_game(response_json, game=game, detail_game = detail_game)

	assert detail

	serie = detail[0]

	assert "name" in serie
	assert "data" in serie

def test_get_iracing_seasons(response_json):
	game = "iracing"
	detail_game = "seasons"
	detail = get_data_game(response_json, game=game, detail_game = detail_game)

	assert detail
	season = detail[0]

	assert "season" in season
	assert "season_url" in season
	assert "season_date" in season
	assert "is_latest" in season
	assert "image" in season

def test_get_data_game_with_wrong_game(response_json):
	wrong_game = faker.word()
	detail_game =  faker.random_element(elements = ["champions", "tracks", "noticias"])

	detail = get_data_game(response_json, game=wrong_game, detail_game = detail_game)
	assert not detail

def test_get_data_game_with_wrong_detail_game(response_json):
	game = faker.random_element(elements = ["lol", "easport", "iracing"])
	wrong_detail_game = faker.word()
	detail = get_data_game(response_json, game=game, detail_game = wrong_detail_game)
	assert not detail
