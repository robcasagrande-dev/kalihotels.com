import urllib.request
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def get_info(url):
    print(f"--- Info for {url} ---")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.title.string if soup.title else 'No Title'
            h1s = [h.get_text(strip=True) for h in soup.find_all('h1')]
            h2s = [h.get_text(strip=True) for h in soup.find_all('h2')]
            print(f"Title: {title}")
            print(f"H1s: {h1s}")
            print(f"H2s (first 5): {h2s[:5]}")
    except Exception as e:
        print(f"Error: {e}")

get_info("https://kalihotels.com/villa-maria/")
get_info("https://kalihotels.com/villa-maria-tayrona/")
get_info("https://kalihotels.com/information-villa-maria/")
