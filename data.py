import requests
import json
question_data = []
response = requests.get("https://opentdb.com/api.php?amount=10&category=31&difficulty=easy&type=boolean")
if response:
    question_data = response.json()["results"]


print(question_data)









