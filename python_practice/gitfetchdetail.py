# Refer to https://github.com/khuyentran1401/top-github-scraper/blob/master/top_github_scraper/utils.py 
# for more code samples.


import requests
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Repository Name", "Created Date","Language", "Stars"]

query= "Python"
#first page
page=2

#search for the top repositories
api_url = f"https://api.github.com/search/repositories?q={query}&{page}"

#send get request
response = requests.get(api_url)

#get the json data
data =  response.json()

for repository in data["items"]:
    name = repository["full_name"]
    created_date = repository["created_at"]
    language = repository["language"]
    stars = repository["stargazers_count"]
    
    table.add_row([name, created_date, language, stars ])

print(table)