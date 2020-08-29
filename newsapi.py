import json
import requests

url="https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=babd42a7cc924a6fae8cb2ff70129103"
response=requests.request("GET",url)
info=json.loads(response.text)
news_dict={}
for i,news in enumerate(info['articles']):
	temp={}
	temp['title']=news['title']
	temp['description']=news['description']
	temp['url']=news['url']
	news_dict[i]=temp
print (news_dict)
print("\n\n")
print(json.dumps(news_dict))
	# for news in info:
# 	print(news['articles'])