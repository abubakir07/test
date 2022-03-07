# import requests
# from bs4 import BeautifulSoup as BS

# url = 'https://akipress.org/'

# headers = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'    
# }

# req = requests.get(url, headers=headers)
# with open('lesson_3/articles.html', 'w', encoding='utf-8') as file:
#     file.write(req.text)
#     file.close()
# with open('lesson_3/articles.html', encoding='utf-8') as file:
#     src = file.read()

# soup = BS(src, 'lxml')

# recent = soup.find_all(class_='newslink')

# all = {}
# for i in recent:
#     item_text = i.text 
#     item_href = 'https://akipress.org'+i.get('href')
#     all[item_text] = item_href

# for name , links in  all:
#     with open(f'lesson_3/articles.html', 'w', encoding='utf-8') as file:
#         file.write(req.text)
        
#     with open(f'lesson_3/articles.html', encoding='utf-8') as file:
#         src = file.read()

