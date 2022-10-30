import requests
from bs4 import BeautifulSoup as BS 

page = 1
selector_path = "#main-content > #catalog-content > .list-view > ._default-grid_1fhuj_203 >\
 [data-key] > article > section"

while True:
    r = requests.get("https://stopgame.ru/review/p" + str(page) + "?subsection=izumitelno")
    html = BS(r.content, "html.parser")
    items = html.select(selector_path)
    if len(items):
        if page == 28:
            break
        for el in items:
            title = el.select('._card__content_1akif_357 > a')
            with open("parser-result.txt", "a", encoding="utf-8") as r:
                r.write(title[0].text + "\n")
        page += 1
    else: break
