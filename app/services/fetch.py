from typing import Any
import httpx

from core.settings import config

type Response =  list[dict[str, str | Any]]

TIMEOUT = 10.0
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36  (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

async def async_get_data() -> Response:
	try:
		async with httpx.AsyncClient(headers = HEADERS) as client:
			response = await client.get(config.url, timeout = TIMEOUT)
			response.raise_for_status()
			responseJson = await response.json()
	except httpx.ConnectError as e:
		return []
	except httpx.HTTPStatusError as e:
		return []
	except httpx.ConnectTimeout as e:
		return []
	
	return responseJson

def sync_get_data() -> Response:
	try:
		with httpx.Client(headers = HEADERS) as client:
			response = client.get(config.url, timeout = TIMEOUT)
			response.raise_for_status()
			responseJson = response.json()
	except httpx.ConnectError as e:
		return []
	except httpx.HTTPStatusError as e:
		return []
	except httpx.ConnectTimeout as e:
		return []
	
	return responseJson
