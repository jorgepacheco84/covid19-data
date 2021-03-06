import re
import ast
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

from .helpers.constants import INFOGRAM_LINK


def get_gov_page():
    uclient = ureq(INFOGRAM_LINK)
    page_html = uclient.read()
    uclient.close()
    page_soup = soup(page_html, "html.parser")
    scripts = page_soup.find_all("script")[7].string
    data_string = re.search(r"\],\[\"Arica(.+)\]\]\]", scripts).group()
    data = data_string.replace('"["', '"],["').replace("]]]", "]")[2:]

    return ast.literal_eval(data)
