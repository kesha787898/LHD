import bs4
import re
from urllib.request import urlopen
import favicon


def get_data_by_url(url):
    try:
        html = urlopen(url)
    except:
        return None
    soup = bs4.BeautifulSoup(html, 'html.parser')
    text = re.sub(r'\s+', ' ', soup.get_text())
    icon = favicon.get(url)[0][0]
    title = soup.title.text
    return {'text': text, 'icon': icon, 'title': title}
