import requests
import json

response = requests.get('http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

# print(response.json()['items'])
skipped_questions = 0

for question in response.json()['items']:
    if question["answer_count"] == 0:
        print(question["title"])
        print(question["link"])

    else:
        skipped_questions += 1
        print("skippped")
    print( )    
print(f"Skipped questions: {skipped_questions}")   