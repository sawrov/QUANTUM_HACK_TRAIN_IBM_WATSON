import sys
import requests
import json

def main(dict):
    url="https://en.wikipedia.org/api/rest_v1/page/summary/"+dict['object_of_interest']+"?redirect=true"
    response=requests.request("GET", url)
    info=json.loads(response.text)
    return { 'message': info['extract'] }
