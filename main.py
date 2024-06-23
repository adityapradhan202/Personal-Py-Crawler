from info_news import titles, title_links
from entertainment import news_headlines, article_links, releases
from entertainment import names, links
import random

def homepage():
    print() # empty line
    print('Enter 1 to get the news related to tech industry.')
    print('Enter 2 to get the news related to anime!')
    print('Enter 3 to get top netflix releases.')
    print('Enter 4 to get the top movies released this year.')
    print('Enter 5 to quit app!')

    user_option = int(input("Enter here: "))
    check_user_input(user_option)


def check_user_input(user_option):
    match user_option:
        case 1:
            tech_news()
        case 2:
            anime_news()
        case 3:
            netflix_releases()
        case 4:
            movies()
        case 5:
            print('Exiting your personal pycrawler! Have a nice day!')
            exit(0)
        case _:
            print('Invalid input!')
            exit(0)


def tech_news():
    print(f'Currently the website has {len(titles)} news...')
    print('Here are 5 random news articles for you...\n')
    
    for i in range(5):
        rand_index = random.randint(0, len(titles)-1)
        print(titles[rand_index])
        print(f'Link - {title_links[rand_index]}')

    homepage()

def anime_news():
    print(f'Currently the website has {len(news_headlines)} news...')
    print('Here are 5 random news articles for you...\n')

    for i in range(5):
        rand_index = random.randint(0, len(news_headlines)-1)
        print(news_headlines[rand_index])
        print(f'Link - {article_links[rand_index]}')

    homepage()

def netflix_releases():
    print(f'Currently the website has {len(news_headlines)} releases...')
    print('Here are 5 random releases for you...\n')

    for j in range(5):
        rand_index = random.randint(0, len(releases)-1)
        print(releases[rand_index])

    homepage()

def movies():
    print(f'Currently the website has {len(names)} movies listed...')
    print('Here are 5 random movies articles for you...\n')

    for j in range(5):
        rand_index = random.randint(0, len(names)-1)
        print(names[rand_index])
        print(f'Link - {links[rand_index]}')

    homepage()


def main():
    homepage()

if __name__ == "__main__":
    main()