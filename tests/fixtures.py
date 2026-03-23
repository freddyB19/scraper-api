from faker import Faker

faker = Faker(locale="es")

RESPONSE_JSON_GAMES = [
	{
		"page": {
			"name": "lol",
			"data": {
				"champions": [
					{
						"champion": faker.name(),
						"url": faker.url(),
						"images": [faker.image_url() for _ in range(10)],
					}
					for _ in range(20)
				],
				"noticias": [
					{
						"titulo": faker.text(),
						"url": faker.url(),
						"categoria": faker.domain_word(),
						"fecha": faker.iso8601(),
						"detalle": faker.paragraph(),
					}
					for _ in range(20)
				],
				"notas": [
					{
						"titulo": faker.text(),
						"url": faker.url(),
						"categoria": faker.domain_word(),
						"fecha": faker.iso8601(),
						"detalle": faker.paragraph(),
					}
					for _ in range(20)
				],
			}
		},
	},
	{
		"page": {
			"name": "easport",
			"data": {
				"noticias": [
					{
						"imagen": faker.image_url(),
						"titulo": faker.text(),
						"etiqueta": faker.word(),
						"fecha": faker.iso8601(),
						"descripcion": faker.paragraph()
					}
					for _ in range(20)
				],
				"novedades": [
					{
						"imagen": faker.image_url(),
						"titulo": faker.text(),
						"url": faker.url(),
						"logo": faker.image_url()
					}

					for _ in range(20)
				],
				"proximamente": [
					{
						"titulo": faker.text(),
						"fecha": faker.iso8601(),
						"plataformas": [{"url": faker.url(), "tipo": faker.word()} for _ in range(4)],
						"genero": [{"url": faker.url(), "tipo": faker.word()} for _ in range(2)],
					}
					for _ in range(5)
				],
				"gratuitos": [
					{
						"imagen": faker.image_url(),
						"titulo": faker.text(),
						"url": faker.url(),
						"logo": faker.image_url()
					}

					for _ in range(20)
				],
				"actualizaciones": [
					{
						"imagen": faker.image_url(),
						"titulo": faker.text(),
						"url": faker.url(),
						"logo": faker.image_url(),
						"informacion": faker.paragraph(),
						"fecha": faker.iso8601(),
						"detalle": faker.paragraph()
					}

					for _ in range(20)
				],
			}
		},
	},
	{
		"page": {
			"name": "iracing",
			"data": {
				"cars": [
					{
						"type": faker.word(),
						"url": faker.url(),
						"image": faker.image_url(),
						"is_new": faker.random_element(elements=[True, False]),
					}

					for _ in range(20)
				],
				"tracks": [
					{
						"track": faker.text(),
						"url": faker.url(),
						"image": faker.image_url(),
						"is_new": faker.random_element(elements = [True, False]),
						"included": faker.random_element(elements = [True, False]),
					}
					for _ in range(20)
				],
				"series": [
					{
						"name": faker.text(),
						"data": [
							{
								"url": faker.url(), 
								"image": faker.image_url(), 
								"name": faker.text(), 
							}
							for _ in range(10)
						]
					}
					for _ in range(20)
				],
				"seasons": [
					{
						"season": faker.text(),
						"season_url": faker.url(),
						"season_date": faker.iso8601(),
						"is_latest": faker.random_element(elements = [True, False]),
						"image": faker.image_url(),
					}
					for _ in range(20)
				],
				"news": [
					{
						"title": faker.text(),
						"url": faker.url(),
						"image": faker.image_url(),
						"author": {"name": faker.name(), "url": faker.url()},
						"detail": faker.paragraph(),
						"date": faker.iso8601(),
					}
					for _ in range(20)
				]
			}
		}
	}
]

RESPONSE_EMPTY_JSON_GAMES = [
	{
		"page": {
			"name": "lol",
			"data": {
				"champions": [],
				"noticias": [],
				"notas": [],
			}
		},
	},
	{
		"page": {
			"name": "easport",
			"data": {
				"noticias": [],
				"novedades": [],
				"proximamente": [],
				"gratuitos": [],
				"actualizaciones": [],
			}
		},
	},
	{
		"page": {
			"name": "iracing",
			"data": {
				"cars": [],
				"tracks": [],
				"series": [],
				"seasons": [],
				"news": []
			}
		}
	}
]


RESPONSE_JSON_NEWS = [{
	"page": {
		"name": "noticias",
		"data": [
			{
				"nombre": "marca",
				"pagina": [
					{
						"titulo": faker.text(),
						"url": faker.url(),
						"imagen": faker.image_url(),
						"meta": faker.word(),
						"autor": faker.name()
					}
					for _ in range(20)
				]
			},
			{
				"nombre": "la naci\u00f3n",
				"pagina": [
					{
						"titulo": faker.text(),
						"url": faker.url(),
						"url_link": faker.url(),
						"imagen": faker.image_url(),
						"fecha": faker.iso8601()
					}
					for _ in range(20)
				],
				"subs": [
					{
						"nombre": "la naci\u00f3n tecnolog\u00eda",
						"pagina": [
							{
								"titulo": faker.text(),
								"url": faker.url(),
								"url_link": faker.url(),
								"imagen": faker.image_url(),
								"fecha": faker.iso8601()
							}
							for _ in range(20)
						]
					}
				]
			},
			{
				"nombre": "wired",
				"subs": [
					{
						"nombre": "wired robots",
						"pagina": [
							{
								"title": faker.text(),
								"image": faker.image_url(),
								"summary": faker.paragraph(),
								"url": faker.url()
							}
							for _ in range(20)
						]
					},
					{
						"nombre": "wired neurociencia",
						"pagina": [
							{
								"title": faker.text(),
								"image": faker.image_url(),
								"summary": faker.paragraph(),
								"url": faker.url()
							}
							for _ in range(20)
						]
					},
					{
						"nombre": "wired biotecnolog\u00eda",
						"pagina": [
							{
								"title": faker.text(),
								"image": faker.image_url(),
								"summary": faker.paragraph(),
								"url": faker.url()
							}
							for _ in range(20)
						]
					},
					{
						"nombre": "wired espacio",
						"pagina": [
							{
								"title": faker.text(),
								"image": faker.image_url(),
								"summary": faker.paragraph(),
								"url": faker.url()
							}
							for _ in range(20)
						]
					},
				]
			}
		]
	}	
}]

RESPONSE_EMPTY_JSON_NEWS = [{
	"page": {
		"name": "noticias",
		"data": [
			{
				"nombre": "marca",
				"pagina": []
			},
			{
				"nombre": "la naci\u00f3n",
				"pagina": [],
				"subs": [
					{
						"nombre": "la naci\u00f3n tecnolog\u00eda",
						"pagina": []
					}
				]
			},
			{
				"nombre": "wired",
				"subs": [
					{
						"nombre": "wired robots",
						"pagina": []
					},
					{
						"nombre": "wired neurociencia",
						"pagina": []
					},
					{
						"nombre": "wired biotecnolog\u00eda",
						"pagina": []
					},
					{
						"nombre": "wired espacio",
						"pagina": []
					},
				]
			}
		]
	}	
}]

__all__ = [
	"JSON_GAMES", 
	"RESPONSE_EMPTY_JSON_GAMES",
	"RESPONSE_JSON_NEWS",
	"RESPONSE_EMPTY_JSON_NEWS",
]