import strawberry

from .types import LOL, Iracing, Easport, Marca, LaNacion, Wired

from services.games_services import get_data_game
from services.fetch import async_get_data, sync_get_data


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
