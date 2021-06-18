import requests
import json

def cat_url():
    url = 'https://api.thecatapi.com/v1/images/search'
    key = 'bd16a39d-384a-4454-a185-4410f08a90f0'
    r = requests.get(url, key)
    for i in r.json():
        return i['url']

def cat_generator():
    catlist = []
    for i in range(8):
        catlist.append(cat_url())
    return catlist