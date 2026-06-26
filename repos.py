import pandas as pd
from requests_html import HTMLSession

session = HTMLSession()
url = 'https://github.com/David-Odesomi?tab=repositories'
response = session.get(url)

container = response.html.find('#user-repositories-list', first=True)

lists = container.find('li')

name: list = []
language: list = []
date: list = []

for item in lists:
    tmp = item.text.split('\n')
    name.append(tmp[0])
    language.append(tmp[1])
    date.append(tmp[2])

df = pd.DataFrame({'Name': name, 'Language': language, 'Date': date})
df.to_csv('repositories.csv', index=False, encoding='utf-8')