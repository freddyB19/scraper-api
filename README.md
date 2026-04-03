# Scraper API

Una API con formato REST/GraphQL para organizar y estructurar los datos sobre noticias y videojuegos extraídos mediante un scraper.

## Requisitos

- Python 3.13+
- Poetry (opcional) o pip

## Instalación

```bash
pip install -e .
```

## Ejecución

```bash
fastapi dev
```

El servidor estará disponible en `http://localhost:8000`

## Documentación

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### REST API

#### Noticias

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/v1/news/marca/game` | Artículos de videojuegos de Marca |
| GET | `/api/v1/news/wired/{detail}` | Artículos de Wired (espacio, robots, neurociencia, biotecnologia) |
| GET | `/api/v1/news/nacion/{detail}` | Artículos de La Nación (juegos, tecnologia) |

#### Videojuegos

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/v1/game/lol/champion` | Campeones de League of Legends |
| GET | `/api/v1/game/lol/{detail}` | Artículos de LOL (noticias, notas) |
| GET | `/api/v1/game/easport/news` | Noticias de EA Sports |
| GET | `/api/v1/game/easport/soon` | Próximos juegos de EA Sports |
| GET | `/api/v1/game/easport/update` | Actualizaciones de EA Sports |
| GET | `/api/v1/game/easport/game/{detail}` | Juegos de EA Sports (gratuitos, novedades) |
| GET | `/api/v1/game/iracing/car` | Coches de iRacing |
| GET | `/api/v1/game/iracing/track` | Pistas de iRacing |
| GET | `/api/v1/game/iracing/season` | Temporadas de iRacing |
| GET | `/api/v1/game/iracing/serie` | Series de iRacing |
| GET | `/api/v1/game/iracing/news` | Noticias de iRacing |

### GraphQL

Accede al endpoint GraphQL en: `/graphql`

## Testing

```bash
pytest
```

## Licencia

MIT
