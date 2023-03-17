import requests
import time



# Requisito 1
def fetch(url):
    headers = { "user-agent": "Fake user-agent" }
    try:
        time.sleep(1)
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text # Conteúdo HTML é retornado por .text não .content
        else:
            return None
    except:
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
