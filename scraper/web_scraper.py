import requests
from bs4 import BeautifulSoup


def fetch_data(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        data = soup.find_all('p')  # 你可以在这里修改提取规则
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return []
