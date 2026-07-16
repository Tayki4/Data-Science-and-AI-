
# HTTP Protokolü
# API nedir?
# requests modülüne bakın?
# Free bir API veri çekicem
# https://newsapi.org/ --> üye olun.


from requests import get
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
from pprint import pprint

try:
    end_point = 'https://newsapi.org/v2/everything?q=tesla&from=2025-11-18&sortBy=publishedAt&apiKey=47f3419f49864ca889f632677d485de1'
    
    response = get(end_point, timeout=6000)
    
    data = response.json()
    
    # region First Article
    # print(
    #     f'Author: {data.get("articles")[0].get("author")}\n'
    #     f'Title: {data.get("articles")[0].get("title")}\n'
    # )
    # endregion
    
    # region Searching
    #! End-User "author name" alıyoruz ve bu yazarın makalelerini ekrana basıyoruz.
    author_name = input('Author Name: ')
    # Path I
    for article in data.get('articles'):
        if article.get('author') == author_name:
            pprint(article)
            
    # Path II
    results = [article for article in data.get('articles') if article.get('author') == author_name]
    
    for result in results:
        pprint(result)
    # endregion
except HTTPError as err:
    print(f'HTTP Error: {err}')
except ConnectionError as err:
    print(f'Connection Error: {err}')
except Timeout as err:
    print(f'Timeout Error: {err}')
except RequestException as err:
    print(f'General Error: {err}')