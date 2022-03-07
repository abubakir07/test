import requests
from bs4 import BeautifulSoup as BS
import json
import csv 

url = 'https://health-diet.ru/table_calorie/'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
# req = requests.get(url, headers=headers)
# with open('lesson_2/diet.html', 'w', encoding='utf-8') as file:
#     file.write(req.text)
# with open('lesson_2/diet.html', encoding='utf-8') as file:
#     src = file.read()

# soup = BS(src, 'lxml')
# all_products_hrefs = soup.find_all(class_='mzr-tc-group-item-href')
# import json
# all_categories_dict = {}
# for item in all_products_hrefs:
#     item_text = item.text 
#     item_href = 'https://health-diet.ru'+item.get('href')
#     all_categories_dict[item_text] = item_href

# with open('lesson_2/all_categies.json', 'w', encoding='utf-8') as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

with open('lesson_2/all_categies.json', encoding='utf-8') as file:
    all_categories = json.load(file)

for category_name, category_href in all_categories.items():
    #сделали замену символов для названия
    rep = [',', '.', ' ', "'", '-']
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, '_')
    #сделали замену символов для названия
    # будем делать запрос на каждый отдельную страницу категории
    req = requests.get(url=category_href, headers=headers)
    src = req.text 
    # with open(f'lesson_2/html/{category_name}.html', 'w', encoding='utf-8') as file:
    #     file.write(src)
    with open(f'lesson_2/html/{category_name}.html', encoding='utf-8') as file:
        src = file.read()
    
    soup = BS(src, 'lxml')

    #собираем заголовок
    table_head = soup.find(class_='mzr-tc-group-table').find('tr').find_all('th')
    product = table_head[0].text
    calories = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    carbohydrates = table_head[4].text

    with open(f'lesson_2/csv/{category_name}.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                product,
                calories,
                proteins,
                fats,
                carbohydrates
            )
        )
    #данные проукдтов
    products_data = soup.find(class_='mzr-tc-group-table').find('tbody').find_all('tr')

    for item in products_data:
        product_tds = item.find_all('td')

        title = product_tds[0].find('a').text 
        calories = product_tds[1].text
        proteins = product_tds[2].text
        fats = product_tds[3].text
        carbohydrates = product_tds[4].text

        with open(f'lesson_2/csv/{category_name}.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    title,
                    calories,
                    proteins,
                    fats,
                    carbohydrates
                )
            )