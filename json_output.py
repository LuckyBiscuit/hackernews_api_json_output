import json
import requests
import pprint
import sys

# request for the hackernews api which lists the ID's for each post but no data from those ids
r = requests.get ('https://hacker-news.firebaseio.com/v0/topstories.json')
packages_json = r.json()

try: 
    int(sys.argv[1])
except ValueError:
    print("Error: Input Invalid")
    exit()

max_articles = int(sys.argv[1])

output_array = []

# article_id variable to be run through the packages.json to pass through the ids with the different api call for each individual item.
for num, article_id in enumerate(packages_json, start = 1):
    package_url = f'https://hacker-news.firebaseio.com/v0/item/{article_id}.json'
    r = requests.get(package_url)
    package_json = r.json()

    # test for package_url response print(package_url)
    # out_put_array defined which should return json output from each item   
    output_array.append({
        "title" : package_json["title"],
        "uri" : package_json["url"] if "url" in package_json else "No Url",
        "author" : package_json["by"],
        "points" : package_json["score"],
        "comments" : package_json["descendants"],
        "rank" : num
    })
    print("Gathering Articles:" + str(num) + "/" + str(max_articles))
    if max_articles <= num: 
        break

print("")
print("-----------------------------------DONE---------------------------------------------------")
print("")


pp = pprint.PrettyPrinter(indent=4)
pp.pprint(output_array)