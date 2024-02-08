import requests

api_key = "a69b5828969941f3892e87943282e80"
api_url = "https://newsapi.org/v2/everything?q=tesla&from=2024-01-08&sortBy=" \
          "publishedAt&apiKey=a69b5828969941f3892e87943282e820"

# Make a request
request = requests.get(api_url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
