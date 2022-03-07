from unittest import result
import requests
from bs4 import BeautifulSoup as BS
import json

# persons_url_list = []

# for i in range(0, 800, 20):
#     url = f"https://www.bundestag.de/ajax/filterlist/en/members/453158-453158?limit=20&noFilterSet=true&offset={i}"
#     q = requests.get(url)
#     result = q.content
#     soup = BS(result, 'lxml')
#     persons = soup.find_all(class_='bt-open-in-overlay')


#     for person in persons:
#         person_page_url = person.get('href')
#         persons_url_list.append(person_page_url)
# with open('lesson_4/person_list.txt', 'a', encoding='utf-8') as file:
#     for line in persons_url_list:
#         file.write(f"{line}\n")

with open('lesson_4/person_list.txt', encoding='utf-8') as file:
    lines = [line.strip() for line in file.readlines()]

    data_dict = []

    for line in lines:
        req = requests.get(line)
        result = req.content

        soup = BS(result,'lxml')
        person = soup.find(class_='bt-biografie-name').find('h3').text
        person_name_company = person.strip().split(',')
        person_name = person_name_company[0]
        person_company = person_name_company[1]

        social_networks = soup.find_all(class_='bt-link-extern')
        social_networks_urls = []
        for item in social_networks:
            social_networks_urls.append(item.get('href'))

        data = {
            'person_name':person_name,
            'person_company':person_company,
            'social_network':social_networks_urls
        }
        data_dict.append(data)

        with open('lesson_4/data.json','w',encoding='utf-8') as file:
            json.dump(data_dict, file, indent=4, ensure_ascii=False)

