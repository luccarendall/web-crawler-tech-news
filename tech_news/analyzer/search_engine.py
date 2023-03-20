from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    busca_titulo = search_news(
        {
            'title': {
                        '$regex': title,
                        '$options': 'i',
                     }
        }
    )

    return [
        (
            noticia_encontrada['title'],
            noticia_encontrada['url']) for noticia_encontrada in busca_titulo
    ]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
