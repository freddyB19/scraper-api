from fastapi import APIRouter

from .v1.news import router as router_news
from .v1.games import router as router_games


router  = APIRouter(prefix = '/api/v1')

router.include_router(router_games)
router.include_router(router_news)
