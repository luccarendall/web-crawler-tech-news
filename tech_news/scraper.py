import requests
import time
from parsel import Selector


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
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
