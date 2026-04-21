from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
}

def fetch_Website_contents(url):
    response = requests.get(url,headers=headers)
    print(response)
    soup = BeautifulSoup(response.content,"html.parser")
    title = soup.title.string if soup.title else "No title found"
    for irr in soup.body(["script","style","img","input"]):
        irr.decompose()
    text = soup.body.get_text(separator="\n",strip=True)
    return title + "\n\n" + text

def fetch_website_links(url):
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content,"html.parser")
    links = [link.get("href") for link in soup.find_all("a")]
    return [link for link in links if link]
