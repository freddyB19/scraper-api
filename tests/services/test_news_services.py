import pprint

import pytest

from faker import Faker

from app.services.news_services import get_data_news

from tests.fixtures import (
	RESPONSE_JSON_NEWS, 
	RESPONSE_EMPTY_JSON_NEWS
)

faker = Faker(locale="es")

@pytest.fixture
def response_json():
	return RESPONSE_JSON_NEWS

@pytest.fixture
def response_empty_json():
	return RESPONSE_EMPTY_JSON_NEWS

def test_get_news_marca(response_json):
	news = "marca"

	marca = get_data_news(response_json, name = news)

	pprint.pprint(marca, indent = 4)

	assert marca

	detail = marca[0]

	assert "titulo" in detail
	assert "url" in detail
	assert "imagen" in detail
	assert "meta" in detail
	assert "autor" in detail

def test_get_empty_news_marca(response_empty_json):
	news = "marca"

	marca = get_data_news(response_empty_json, name = news)

	assert not marca
	assert len(marca) == 0

def test_get_news_lanacion(response_json):
	news = "la nación"

	lanacion = get_data_news(response_json, name = news)

	assert lanacion

	detail = lanacion[0]

	assert "titulo" in detail
	assert "url" in detail
	assert "url_link" in detail
	assert "imagen" in detail
	assert "fecha" in detail

def test_get_news_lanacion_tecnologia(response_json):
	news = "la nación"
	page = "la nación tecnología"

	lanacion_tec = get_data_news(response_json, name = news, page = page)

	assert lanacion_tec
	
	detail = lanacion_tec[0]

	assert "titulo" in detail
	assert "url" in detail
	assert "url_link" in detail
	assert "imagen" in detail
	assert "fecha" in detail

def test_get_empty_news_lanacion(response_empty_json):
	news = "la nación"

	lanacion = get_data_news(response_empty_json, name = news)

	assert not lanacion
	assert len(lanacion) == 0

def test_get_empty_news_lanacion_tecnologia(response_empty_json):
	news = "la nación"
	page = "la nación tecnología"

	lanacion_tec = get_data_news(response_empty_json, name = news, page = page)

	assert not lanacion_tec
	assert len(lanacion_tec) == 0

def test_get_news_wired_robots(response_json):
	news = "wired"
	page = "wired robots"

	wired_robots = get_data_news(response_json, name = news, page = page)

	assert wired_robots

	detail = wired_robots[0]

	assert "titulo" in detail
	assert "imagen" in detail
	assert "resum" in detail
	assert "url" in detail

def test_get_news_wired_espacio(response_json):
	news = "wired"
	page = "wired espacio"

	wired_espacio = get_data_news(response_json, name = news, page = page)

	assert wired_espacio

	detail = wired_espacio[0]

	assert "title" in detail
	assert "image" in detail
	assert "summary" in detail
	assert "url" in detail

def test_get_news_wired_neurociencia(response_json):
	news = "wired"
	page = "wired neurociencia"

	wired_neuro = get_data_news(response_json, name = news, page = page)

	assert wired_neuro

	detail = wired_neuro[0]

	assert "title" in detail
	assert "image" in detail
	assert "summary" in detail
	assert "url" in detail

def test_get_news_wired_biotecnologia(response_json):
	news = "wired"
	page = "wired biotecnología"

	wired_biotec = get_data_news(response_json, name = news, page = page)

	assert wired_biotec

	detail = wired_biotec[0]

	assert "title" in detail
	assert "image" in detail
	assert "summary" in detail
	assert "url" in detail

@pytest.mark.parametrize(
	"page",[
		"wired robots",
		"wired espacio",
		"wired neurociencia",
		"wired biotecnología",
	]
)
def test_get_empty_news_wired(response_empty_json, page):
	news = "wired"

	wired = get_data_news(response_empty_json, name = news, page = page)

	assert not wired
	assert len(wired) == 0
