import requests
import urllib.parse
from bs4 import BeautifulSoup

def extract_disease(url):
	source=requests.get(url)
	soup = BeautifulSoup(source.text,"html.parser")
	# soup = BeautifulSoup(source.text, 'lxml')
	container=soup.find("div",{"class":"mw-parser-output"})
	for tag in container.find_all("li"):
		if tag.a:
			try:
				print(urllib.parse.unquote(tag.a.get('href')))
			except:
				print(tag.a.get('href'))

url="https://en.wikipedia.org/wiki/Lists_of_diseases"
source=requests.get(url)
soup = BeautifulSoup(source.text,"html.parser")
container=soup.find("div",{"id":"toc"})
url_list=[]
for tag in container.find_all("li"):
		if tag.a:
			url_list.append(tag.a.get('href'))

for url in url_list:
	print(url)
	extract_disease("https://en.wikipedia.org"+url)
