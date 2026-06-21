import urllib.request
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def inspect_links(url):
    print(f"=== Links on {url} ===")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            links = soup.find_all('a', href=True)
            for link in links:
                href = link['href']
                text = link.get_text(strip=True)
                if any(x in href.lower() for x in ['leda', 'maria', 'isabella', 'lang', 'es', 'en', 'it']):
                    # Print interesting links
                    print(f"  {text} -> {href}")
    except Exception as e:
        print(f"Error: {e}")

inspect_links("https://kalihotels.com/")
