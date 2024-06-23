
from bs4 import BeautifulSoup
import requests

# For movies
web_url = "https://editorial.rottentomatoes.com/guide/popular-movies/"
# For anime
anime_web_url = "https://www.animenewsnetwork.com/"
# For latest netflix release
netflix_release_url = 'https://www.rottentomatoes.com/browse/movies_at_home/affiliates:netflix~sort:newest'

def content_fetcher(url):
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def fetch_movie_data(soup:BeautifulSoup):
    names = []
    links = []
    tags = soup.select('h2 a')
    for i in tags:
        names.append(i.getText())
        links.append(i.get('href'))

    return names, links

def fetch_anime_data(anime_soup:BeautifulSoup):
    news_headlines = []
    article_links = []
    a_tags = anime_soup.select('h3 a')
    for j in a_tags:
        news_headline = j.getText()
        article_link ="https://www.animenewsnetwork.com" + j.get('href')
        news_headlines.append(news_headline)
        article_links.append(article_link)

    return news_headlines, article_links

def fetch_netflix_release_data(nflix_soup:BeautifulSoup):
    releases = []
    tags = nflix_soup.select('span.p--small')
    for t in tags:
        release = t.getText()
        releases.append(release.strip())
    
    return releases


soup = content_fetcher(web_url)
names, links = fetch_movie_data(soup)

anime_news_soup = content_fetcher(anime_web_url)
news_headlines, article_links = fetch_anime_data(anime_news_soup)

nflix_soup = content_fetcher(netflix_release_url)
releases = fetch_netflix_release_data(nflix_soup)

if __name__ == "__main__":
    print("\nAnime stuff...")
    print(news_headlines[0])
    print(article_links[0])

    print('\nMovie stuff...')
    print(names[2], links[2])

    print('\nNetflix stuff...')
    print(len(releases))
    print(releases[16])