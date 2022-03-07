from wsgiref import headers
import requests
from bs4 import BeautifulSoup as bs

link1='https://akipress.org/'

header={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
req=requests.get(link1,headers=header)

# # Записали в файл
# with open('lesson_3/novosti.html','w',encoding='utf-8') as file:
#     file.write(req.text)
#     file.close()

# Читаем файл
with open('lesson_3/novosti.html','r',encoding='utf-8') as file:
    src=file.read()
file.close()
soup=bs(src,'lxml')

recent=soup.find_all(class_='newslink')


# Список новостей
with open('lesson_3/news_list.txt','w',encoding='utf-8') as file:
    for i in recent:
        item_href='https:'+str(i.get('href'))
        file.write(f'{i.text}:{item_href}\n')
file.close()

#Добавление в словарь
all_p={}
for i in recent:
    item_href='https:'+str(i.get('href'))
    all_p[i.text]=item_href


#Вывод общую информацию
for s,links in all_p.items():

    req=requests.get(links,headers=header)

    soup=bs(req.text,'lxml')
    recent=soup.find_all('p')

    dd=' '
    for i in recent:
        dd+=f'{i.text}\n'

    with open(f'lesson_3/ali/{s}.txt','w',encoding='utf-8') as file:
        file.write(dd)