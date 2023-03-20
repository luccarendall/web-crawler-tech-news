import requests
import time
from parsel import Selector
import re


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    try:
        time.sleep(1)
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text
            # Conteúdo HTML é retornado por .text não .content
        else:
            return None
    except requests.exceptions.Timeout:  # Flake reclamou de deixar só o except
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    lista_vazia = []
    # busco a tag onde existe o href (a) uso a class dela.
    # Lembra que a leitura é <-
    # Tipo: eu quero o atributo tal, no caso href(link) que está na classe tal.
    # Se a classe fosse fora da tag precisaria ter aquela cascata lá
    links = selector.css('.cs-overlay-link::attr(href)').getall()

    if not links:
        return lista_vazia
    else:
        return links


# Requisito 3
def scrape_next_page_link(html_content):
    try:
        selector = Selector(text=html_content)
        next_page = selector.css('.next::attr(href)').get()
        # Lembrar que a palavra após a classe não conta.
        # Exemplo: .next page-numbers. A classe do link é apenas o .next
        return next_page
    except LookupError:
        return None


# Requisito 4
def scrape_news(html_content):
    # Remover caracteres vazios ao final
    # https://stackoverflow.com/questions/18457101/python-re-compile-and-re-sub
    # https://stackoverflow.com/questions/3075130/what-is-the-difference-between-and-regular-expressions
    removerEspacos = re.compile("<.*?>")

    try:
        # Pegar o conteúdo html
        selector = Selector(text=html_content)
        # Buscar cada informação
        url_noticia = selector.css('div::attr(data-share-url)').get()
        title_noticia = selector.css('.entry-title::text').get()
        timestamp_noticia = selector.css('.meta-date::text').get()
        pessoa_redatora = selector.css('.author a::text').get()
        tempo_de_leitura = selector.css('.meta-reading-time::text').get()
        resumo = re.sub(
            removerEspacos, '', selector.css(".entry-content p").get()
            )
        categoria = selector.css('.category-style .label::text').get()
        # Preencher um dicionário com as informações coletadas
        noticia_blog = {
            'url': url_noticia,
            # https://stackoverflow.com/questions/10993612/how-to-remove-xa0-from-string-in-python
            'title': title_noticia.replace(u'\xa0', u''),
            'timestamp': timestamp_noticia,
            'writer': pessoa_redatora,
            'reading_time': int(tempo_de_leitura.split(' ')[0]),
            # remove todos os espaços em branco no final da string ↓
            'summary': resumo.rstrip(),
            'category': categoria
        }
        # Retornar o uma noticia
        return noticia_blog
    except LookupError:
        return "Erro na raspagem da noticia"


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
