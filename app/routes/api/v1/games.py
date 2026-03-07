from typing import Literal

from fastapi import APIRouter, Depends, Request, status

from fastapi_pagination import paginate
from fastapi_pagination.links import Page

from slowapi import Limiter
from slowapi.util import get_remote_address

from models import games
from services import games_commands
from services.fetch import sync_get_data

type ResponseJson = list[dict]
type LOLTypeArticle = Literal["noticias", "notas"]
type EasportTypeArticle = Literal["gratuitos", "novedades"]


async def get_json():
	return sync_get_data()


router  = APIRouter(prefix = '/game')
limiter = Limiter(key_func=get_remote_address, strategy = "fixed-window")


@router.get(
	"/lol/champions",
	status_code = status.HTTP_200_OK,
	response_model = Page[games.LOLChampion]
)
@limiter.limit("30/minute", per_method = True)
async def lol_champions(request: Request, data: ResponseJson = Depends(get_json)):
	return paginate(games_commands.get_lol_champions(data))

@router.get(
	"/lol/{detail}",
	status_code = status.HTTP_200_OK,
	response_model = Page[games.LOLArticle]
)
@limiter.limit("30/minute", per_method = True)
async def lol_articles(request: Request, detail: LOLTypeArticle, data: ResponseJson =  Depends(get_json)):
	
	return paginate(games_commands.get_lol_articles(data, detail = detail))


@router.get(
	"/easport/news",
	status_code = status.HTTP_200_OK,
	response_model = Page[games.EasportNews]
)
@limiter.limit("30/minute", per_method = True)
async def easport_news(request: Request, data: ResponseJson = Depends(get_json)):
	return paginate(
		games_commands.get_easport_news(data)
	)

@router.get(
	"/easport/soon",
	status_code = status.HTTP_200_OK,
	response_model = Page[games.EasportSoon]
)
@limiter.limit("30/minute", per_method = True)
async def easport_soon(request: Request, data: ResponseJson = Depends(get_json)):
	return paginate(
		games_commands.get_easport_soon(data)
	)

@router.get(
	"/easport/updates",
	status_code = status.HTTP_200_OK,
	response_model = Page[games.EasportUpdate]
)
@limiter.limit("30/minute", per_method = True)
async def easport_updates(request: Request, data: ResponseJson = Depends(get_json)):
	return paginate(
		games_commands.get_easport_updates(data)
	)

@router.get(
	"/easport/games/{detail}",
	status_code = status.HTTP_200_OK,
	response_model = Page[games.EasportGame]
)
@limiter.limit("30/minute", per_method = True)
async def easport_games(request: Request, detail: EasportTypeArticle, data: ResponseJson = Depends(get_json)):
	return paginate(
		games_commands.get_easport_games(data, detail = detail)
	)

@router.get(
	"/iracing/cars",
	status_code = status.HTTP_200_OK,
	response_model = Page[games.IracingCars]
)
@limiter.limit("30/minute", per_method = True)
async def iracing_cars(request: Request, data: ResponseJson = Depends(get_json)):
	return paginate(
		games_commands.get_iracing_cars(data)
	)

@router.get(
	"/iracing/tracks",
	status_code = status.HTTP_200_OK,
	response_model = Page[games.IracingTracks]
)
@limiter.limit("30/minute", per_method = True)
async def iracing_tracks(request: Request, data: ResponseJson = Depends(get_json)):
	return paginate(
		games_commands.get_iracing_tracks(data)
	)

@router.get(
	"/iracing/seasons",
	status_code = status.HTTP_200_OK,
	response_model = Page[games.IracingSeasons]
)
@limiter.limit("30/minute", per_method = True)
async def iracing_seasons(request: Request, data: ResponseJson = Depends(get_json)):
	return paginate(
		games_commands.get_iracing_seasons(data)
	)

@router.get(
	"/iracing/series",
	status_code = status.HTTP_200_OK,
	response_model = Page[games.IracingSeries]
)
@limiter.limit("30/minute", per_method = True)
async def iracing_series(request: Request, data: ResponseJson = Depends(get_json)):
	return paginate(
		games_commands.get_iracing_series(data)
	)

@router.get(
	"/iracing/news",
	status_code = status.HTTP_200_OK,
	response_model = Page[games.IracingNews]
)
@limiter.limit("30/minute", per_method = True)
async def iracing_news(request: Request, data: ResponseJson = Depends(get_json)):
	return paginate(
		games_commands.get_iracing_news(data)
	)
