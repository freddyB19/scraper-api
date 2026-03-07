from typing import Literal

from fastapi import APIRouter, Depends, Request, status

from fastapi_pagination import paginate
from fastapi_pagination.links import Page

from slowapi import Limiter
from slowapi.util import get_remote_address

from models import news
from services import news_commands
from services.fetch import sync_get_data

type ResponseJson = list[dict]
type LaNacionTypeArticle = Literal['juegos', 'tecnologia']
type WiredTypeArticle = Literal['espacio', 'robots', 'neurociencia', 'biotecnología']


router = APIRouter(prefix = "/news")
limiter = Limiter(key_func=get_remote_address, strategy = "fixed-window")

async def get_json():
	return sync_get_data()


@router.get(
	'/marca/game',
	status_code = status.HTTP_200_OK,
	response_model = Page[news.MarcaVideogames]
)
@limiter.limit("30/minute", per_method = True)
async def marca(request: Request, data: ResponseJson = Depends(get_json)):
	return paginate(
		news_commands.get_marca_videogames(data)
	)


@router.get(
	'/wired/{detail}',
	status_code = status.HTTP_200_OK,
	response_model = Page[news.WiredArticle]
)
@limiter.limit("30/minute", per_method = True)
async def wired(request: Request, detail: WiredTypeArticle, data: ResponseJson = Depends(get_json)):
	return paginate(
		news_commands.get_wired_articles(data, page = detail)
	)


@router.get(
	'/nacion/{detail}',
	status_code = status.HTTP_200_OK,
	response_model = Page[news.LaNacionArticle]
)
@limiter.limit("30/minute", per_method = True)
async def la_nacion(request: Request, detail: LaNacionTypeArticle, data: ResponseJson = Depends(get_json)):
	return paginate(
		news_commands.get_lanacion_articles(data, page = detail)
	)
