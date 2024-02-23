import requests

from send_email import send_email

api_key = "a69b5828969941f3892e87943282e80"
api_url = "https://newsapi.org/v2/everything?q=tesla&from=2024-01-23&sortBy=" \
          "publishedAt&apiKey=a69b5828969941f3892e87943282e820"

# Make a request
request = requests.get(api_url)

# Get a dictionary with data
content = request.json()

body = ""
# Access the article title and description
for article in content["articles"]:
    if article["title"] and article["description"] is not None:
        body += article["title"] + "\n" + article["description"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)