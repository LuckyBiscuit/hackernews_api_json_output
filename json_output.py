import json
import requests
import pprint
import sys

# request for the hackernews api which lists the ID's for each post but no data from those ids
r = requests.get ('https://hacker-news.firebaseio.com/v0/topstories.json')
packages_json = r.json()

# print(packages_json)

# article_id variable to be run through the packages.json to pass through the ids with the different api call for each individual item.
for num, article_id in enumerate(packages_json, start=1):
    package_url = f'https://hacker-news.firebaseio.com/v0/item/{article_id}.json'
    r = requests.get(package_url)
    packages_json = r.json()

    print(package_url)