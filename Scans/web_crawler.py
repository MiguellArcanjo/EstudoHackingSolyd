import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

TARGET_URL = "http://100.24.123.145"
TARGET_DOMAIN = urlparse(TARGET_URL).netloc

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}

TO_CRAWL = [TARGET_URL]
CRAWLED = set()

def process_links(current_url, html):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all("a", href=True):
        link = tag["href"]
        full_url = urljoin(current_url, link).split('#')[0]
        
        if urlparse(full_url).netloc == TARGET_DOMAIN:
            if full_url not in CRAWLED and full_url not in TO_CRAWL:
                TO_CRAWL.append(full_url)
        else:
            if full_url.startswith("http"):
                print(f"  [Link Externo Detectado]: {full_url}")

while TO_CRAWL:
    url = TO_CRAWL.pop(0)

    if url in CRAWLED:
        continue

    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        print(f"\n--- Rastreando Interno: {url} ---")
        
        if "text/html" in response.headers.get("Content-Type", ""):
            process_links(url, response.text)
        
        CRAWLED.add(url)
    except Exception as e:
        print(f"Erro ao acessar {url}: {e}")

print(f"\nBusca finalizada. Total de páginas internas exploradas: {len(CRAWLED)}")