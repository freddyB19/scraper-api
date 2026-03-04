import strawberry

from .types import LOL, Iracing, Easport, Marca, LaNacion, Wired

from services.fetch import sync_get_data
from services.news_services import get_data_news
from services.games_services import get_data_game


@strawberry.type
class Query:

    @strawberry.field
    def lol(self) -> LOL:
        game = "lol"
        data = sync_get_data()

        notes = get_data_game(data, game = game, detail_game = "notas")
        news = get_data_game(data, game = game, detail_game = "noticias")
        champions = get_data_game(data, game = game, detail_game = "champions")

        return {
            "news": news,
            "champions": champions,
            "notes": notes
        }

    @strawberry.field
    def easport(self) -> Easport:
        game = "easport"
        data = sync_get_data()

        news = get_data_game(data, game = game, detail_game = "noticias")
        free = get_data_game(data, game = game, detail_game = "gratuitos")
        soon = get_data_game(data, game = game, detail_game = "proximamente")
        novelties = get_data_game(data, game = game, detail_game = "novedades")
        updates = get_data_game(data, game = game, detail_game = "actualizaciones")

        return {
            "news": news,
            "novelties": novelties,
            "free": free,
            "soon": soon,
            "updates": updates
        }

    @strawberry.field
    def iracing(self) -> Iracing:
        game = "iracing"
        data = sync_get_data()

        news = get_data_game(data, game = game, detail_game = "news")
        cars = get_data_game(data, game = game, detail_game = "cars")
        tracks = get_data_game(data, game = game, detail_game = "tracks")
        series = get_data_game(data, game = game, detail_game = "series")
        seasons = get_data_game(data, game = game, detail_game = "seasons")

        return {
            "news": news,
            "cars": cars,
            "tracks": tracks,
            "series": series,
            "seasons": seasons
        }

    @strawberry.field
    def marca(self) -> Marca:
        name = "marca"
        data = sync_get_data()

        marca = get_data_news(data, name = name)
        return {"marca": marca}

    @strawberry.field
    def lanacion(self) -> LaNacion:
        name = "la nación"
        data = sync_get_data()

        games = get_data_news(data, name = name)
        tecnology = get_data_news(data, name = name, page = "la nación tecnología")

        return {
            "games": games,
            "tecnology": tecnology
        }

    @strawberry.field
    def wired(self) -> Wired:
        name = "wired"
        data = sync_get_data()

        space = get_data_news(data, name = name, page = "wired espacio")
        robots = get_data_news(data, name = name, page = "wired robots")
        neuroscience = get_data_news(data, name = name, page = "wired neurociencia")
        biotechnology = get_data_news(data, name = name, page = "wired biotecnología")

        return {
            "space": space,
            "robots": robots,
            "neuroscience": neuroscience,
            "biotechnology": biotechnology
        }
