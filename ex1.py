import requests
import re
import time
from bs4 import BeautifulSoup
from lxml import html


# Скрипт для вывода новых статей на HABR каждые 5 минут
# https://habr.com/ru/all/


def print_article(lists):
    for i, article in enumerate(reversed(lists)):
        print('\n' + article.h2.text.strip() + '\nСсылка: https://habr.com' + article.h2.a.attrs[
            "href"].strip())


def search():

    # Отпраляем запрос по указанному адресу и получем в ответ документ HTML
    r = requests.get("https://habr.com/ru/all/")

    # Создаем экземпляр bs для работы с полученным документом
    soup = BeautifulSoup(r.text, 'lxml')

    #  Находим все посты, которые находятся в отдельно выделенном div
    lists_of_article = soup.find_all('article', {"class": re.compile('tm-articles-list')})

    return lists_of_article


def main():

    # id последней актуальной статьи
    recent_article_id = ''

    while True:

        #
        articles = search()

        # Проверяем id актуальной последней найденной статьи
        if recent_article_id == '':
            print('Статьи на HABR в данный момент:')
            print_article(articles)
        else:
            for article in reversed(articles):
                if article.attrs['id'] == recent_article_id:
                    break
                print('\nВышла новая статьи на HABR!')
                print(
                    '\n' + article.h2.text.strip() + '\nСсылка: https://habr.com' + article.h2.a.attrs["href"].strip())

        recent_article_id = articles[0].attrs['id']

        time.sleep(300)

    # recent_article = search(recent_article)


if __name__ == '__main__':
    main()
