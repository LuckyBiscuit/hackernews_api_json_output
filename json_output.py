import json
import requests
import pprint
import sys

# request for the hackernews api which lists the ID's for each post but no data from those ids
r = requests.get ('https://hacker-news.firebaseio.com/v0/topstories.json')
packages_json = r.json()

print(packages_json)
