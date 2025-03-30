from flask import Flask, render_template, request
import json

app = Flask(__name__)

def load_quiz_answers():
  try:
    with open('quiz_data.json', 'r') as file:
      return json.load(file)
  except FileNotFoundError:
    return []
  
quiz_data = load_quiz_answers()

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/category', methods=['GET'])
def category():
  return render_template('category.html')

@app.route('/selectionsort', methods=['GET', 'POST'])
def selection_sort():
  if request.method == 'POST':
    return 'Form submitted successfully!'
  return render_template('/selectionsort.html')

@app.route('/quicksortNotes', methods=['GET'])
def quicksort():
  return render_template('/quicksortNotes.html')

@app.route('/quicksortQuiz', methods=['GET'])
def quicksortQuiz():
  return render_template('/quicksortQuiz.html')

@app.route('/submit_quicksort_quiz', methods=['POST'])
def quicksortAnswers():
  user_answers = {key: request.form.get(key, "") for key in ["question1", "question2", "question3", "question4", "question5"]}
  quicksort_correct_answers = next((item for item in quiz_data if item["id"] == "Quicksort Answer"), None)
  if quicksort_correct_answers:
    return render_template('/quicksortAnswer.html', user_answers=user_answers, quicksort_answers=quicksort_correct_answers)
  else:
    return "Quicksort answers not found.", 404


if __name__ == '__main__':
  app.run(debug=True)