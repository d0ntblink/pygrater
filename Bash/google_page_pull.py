from bs4 import BeautifulSoup
from random import randrange
import requests
from requests.api import get


def create_url(question):
    url = question.replace(' ', '+')
    url = 'https://google.com/search?q=' + url
    return url


def get_html(url):
    user_agent = USER_AGENTS[randrange(len(USER_AGENTS))]
    headers = {'user-agent': user_agent}
    html_content = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html_content, "lxml")
    return soup


USER_AGENTS = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    )