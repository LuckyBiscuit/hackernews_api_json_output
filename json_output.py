import json
import requests
import pprint
import sys

# request for the hackernews api which lists the ID's for each post but no data from those ids
r = requests.get ('https://hacker-news.firebaseio.com/v0/topstories.json')
packages_json = r.json()

#This tests whether input entered in follows the integer value and returns the an error message for any value errors
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
    # fixed url response here as I realised that there are items that are returned which do not have URL's which was causing errors when running the file, done this through an if statement. So if the parameter URL is present in the package_json list include
    # that URL parameter response else return a string No url to fill out the parameter.
    output_array.append({
        "title" : package_json["title"],
        "uri" : package_json["url"] if "url" in package_json else "No Url",
        "author" : package_json["by"],
        "points" : package_json["score"],
        "comments" : package_json["descendants"],
        "rank" : num
    })
    # When running this first the response did not have any information while gathering the data, so I added this to give some kind of information for the user running the python file.
    print("Gathering Articles:" + str(num) + "/" + str(max_articles))
    if max_articles <= num: 
        break
# This is also to create a more readable response by splitting the gathering response from the json item response.
print("")
print("-----------------------------------DONE---------------------------------------------------")
print("")

#used the pprint module to turn the reponse into a more readable json response.
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(output_array)