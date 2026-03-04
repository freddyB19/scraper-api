from itertools import chain

type Response = list[dict[str, str]]
type NewsData = list[dict[str, str]]

def get_data_news(data: Response, name: str, page: str = None) -> NewsData:
	if not data:
		return []

	format_news = name.lower()

	result = [
		page_news
		for page_news in data 
		if page_news["page"]["name"] == "noticias"
	]

	result_news = [
		page
		for news_name in result
		for page in news_name["page"]["data"]
		if page["nombre"] == format_news
	]

	if not page:
		result_detail_page = map(lambda article: article["pagina"], result_news)
	else:
		format_page = page.lower()
		result_detail_page = [
			article_detail["pagina"]
			for article in result_news
			for article_detail in article["subs"]
			if article_detail["nombre"] == format_page
		]

	details = list(chain.from_iterable(result_detail_page))

	return details if details else []
