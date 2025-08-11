import requests
url = "https://opentdb.com/api.php?amount=1&type=multiple&category=9"
response = requests.get(url)
if response.status_code == 200:
    question_data = response.json()
    question = question_data['results'][0]['question']
    correct_answer = question_data['results'][0]['correct_answer']
    incorrect_answers = question_data['results'][0]['incorrect_answers']
    print(f"Question: {question}")
    answers = incorrect_answers + [correct_answer]
    i = 1
    for answer in answers:
        print(f"{i}. {answer}")
        i += 1
    print(f"Correct answer: {correct_answer}")
else:
    print("Не вдалося отримати питання. Спробуйте ще раз.")