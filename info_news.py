from bs4 import BeautifulSoup
import requests

verge_tech_url = 'https://indianexpress.com/section/technology/'

def content_fetcher(url):
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def tech_news_data(soup:BeautifulSoup):
    article_titles = []
    article_links = []
    html_tags = soup.select('h3 a')
    for h in html_tags:
        title = h.getText()
        link = h.get('href')
        article_titles.append(title)
        article_links.append(link)

    return article_titles, article_links

tech_soup = content_fetcher(verge_tech_url)
titles, title_links = tech_news_data(tech_soup)

if __name__ == "__main__":
    print(len(titles[0]))
    print(titles[2])
    print(title_links[2])