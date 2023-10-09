from bs4 import BeautifulSoup
import requests

def getSoup(url: str) -> BeautifulSoup | None:
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
    else:
        print("Failed to fetch the page. Status code:", response.status_code)
        html_content = None
        
    if html_content:
        soup = BeautifulSoup(html_content, "html.parser")
    else:
        # Handle the case where the request failed
        soup = None
    return soup