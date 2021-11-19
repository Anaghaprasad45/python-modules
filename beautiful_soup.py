from bs4 import BeautifulSoup

with open("index.html") as f:
    soup = BeautifulSoup(f, 'html.parser')

for i in soup.find_all('a'):
    print(i.get('href'))
