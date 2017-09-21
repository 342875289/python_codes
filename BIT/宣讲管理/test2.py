from bs4 import BeautifulSoup

soup = BeautifulSoup("<html><body><p>data</p></body></html>",'html.parser')

print(soup)
print(soup('p'))