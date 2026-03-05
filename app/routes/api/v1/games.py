from typing import Literal

from fastapi import APIRouter, Depends, status

from fastapi_pagination import paginate
from fastapi_pagination.links import Page

from models import games
from services import games_commands
from services.fetch import sync_get_data

type ResponseJson = list[dict]
type LOLTypeArticle = Literal["noticias", "notas"]
type EasportTypeArticle = Literal["gratuitos", "novedades"]


async def get_json():
	return sync_get_data()


router  = APIRouter(prefix = '/game')


@router.get(
	"/lol/champions",
	status_code = status.HTTP_200_OK,
	response_model = Page[games.LOLChampion]
)
async def lol_champions(data: ResponseJson = Depends(get_json)):
	return paginate(games_commands.get_lol_champions(data))

@router.get(
	"/lol/{detail}",
	status_code = status.HTTP_200_OK,
	response_model = Page[games.LOLArticle]
)
async def lol_articles(detail: LOLTypeArticle, data: ResponseJson =  Depends(get_json)):
	
	return paginate(games_commands.get_lol_articles(data, detail = detail))


@router.get(
	"/easport/news",
	status_code = status.HTTP_200_OK,
	response_model = Page[games.EasportNews]
)
async def easport_news(data: ResponseJson = Depends(get_json)):
	return paginate(
		games_commands.get_easport_news(data)
	)

@router.get(
	"/easport/soon",
	status_code = status.HTTP_200_OK,
	response_model = Page[games.EasportSoon]
)
async def easport_soon(data: ResponseJson = Depends(get_json)):
	return paginate(
		games_commands.get_easport_soon(data)
	)

@router.get(
	"/easport/updates",
	status_code = status.HTTP_200_OK,
	response_model = Page[games.EasportUpdate]
)
async def easport_updates(data: ResponseJson = Depends(get_json)):
	return paginate(
		games_commands.get_easport_updates(data)
	)

@router.get(
	"/easport/games/{detail}",
	status_code = status.HTTP_200_OK,
	response_model = Page[games.EasportGame]
)
async def easport_games(detail: EasportTypeArticle, data: ResponseJson = Depends(get_json)):
	return paginate(
		games_commands.get_easport_games(data, detail = detail)
	)

@router.get(
	"/iracing/cars",
	status_code = status.HTTP_200_OK,
	response_model = Page[games.IracingCars]
)
async def iracing_(data: ResponseJson = Depends(get_json)):
	return paginate(
		games_commands.get_iracing_cars(data)
	)

@router.get(
	"/iracing/tracks",
	status_code = status.HTTP_200_OK,
	response_model = Page[games.IracingTracks]
)
async def iracing_tracks(data: ResponseJson = Depends(get_json)):
	return paginate(
		games_commands.get_iracing_tracks(data)
	)

@router.get(
	"/iracing/seasons",
	status_code = status.HTTP_200_OK,
	response_model = Page[games.IracingSeasons]
)
async def iracing_seasons(data: ResponseJson = Depends(get_json)):
	return paginate(
		games_commands.get_iracing_seasons(data)
	)

@router.get(
	"/iracing/series",
	status_code = status.HTTP_200_OK,
	response_model = Page[games.IracingSeries]
)
async def iracing_series(data: ResponseJson = Depends(get_json)):
	return paginate(
		games_commands.get_iracing_series(data)
	)

@router.get(
	"/iracing/news",
	status_code = status.HTTP_200_OK,
	response_model = Page[games.IracingNews]
)
async def iracing_news(data: ResponseJson = Depends(get_json)):
	return paginate(
		games_commands.get_iracing_news(data)
	)
