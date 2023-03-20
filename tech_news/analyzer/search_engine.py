from tech_news.database import search_news
from datetime import datetime


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
    try:
        # Formato como a data chega:
        iso_data = "%Y-%m-%d"

        # https://stackoverflow.com/questions/9978534/match-dates-using-python-regular-expressions
        # Formata a data para dd/mm/yyyy
        data_DMY = datetime.strptime(date, iso_data).strftime("%d/%m/%Y")
        # Busca usando a data no formato "correto"
        busca = {
                    "timestamp": data_DMY
                }
        # Traz a noticia encontrada
        return [
            (
                noticia_encontrada["title"], noticia_encontrada["url"]
            )
            for noticia_encontrada in search_news(busca)]
    # Caso a data inserida seja inválida, cai nesse erro e retorna a mensagem
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    # praticamente igual a busca por titulo, só alterando o termo de busca
    # busca_por_categoria. Flake pediu para diminuir o tamanho da linha
    busca_categ = search_news(
        {
            'category': {
                        '$regex': category,
                        '$options': 'i',
                     }
        }
    )

    return [
        (
            noticia_encontrada['title'],
            noticia_encontrada['url']) for noticia_encontrada in busca_categ
    ]
