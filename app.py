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

@app.route('/hashTablesNotes', methods=['GET'])
def hashTables():
  return render_template('/hashTablesNotes.html')

@app.route('/hashTablesQuiz', methods=['GET'])
def hashTablesQuiz():
  return render_template('/hashTablesQuiz.html')

@app.route('/submit_hashTables_quiz', methods=['POST'])
def hashTablesAnswers():
  user_answers = {key: request.form.get(key, "") for key in ["question1", "question2", "question3", "question4", "question5"]}
  hashTables_correct_answer = next((item for item in quiz_data if item["id"] == "HashTable Answer"), None)
  if hashTables_correct_answer:
    return render_template('/hashTablesAnswer.html', user_answers=user_answers, hashTables_answers=hashTables_correct_answer)
  else:
    return "Hash Table answers not found.", 404
  
@app.route('/ch1_ch5', methods=['GET'])
def ch1_ch5_quiz():
  return render_template('/ch1_ch5.html')

@app.route('/submit_ch1_ch5_quiz', methods=['POST'])
def ch1_ch5():
  user_answers = {key: request.form.get(key, "") for key in ["question1", "question2", "question3", "question4", "question5", "question6", "question7", "question8", "question9", "question10", "question11", "question12", "question13", "question14", "question15"]}
  ch1_ch5_correct_answer = next((item for item in quiz_data if item["id"] == "ch1_ch5 Answer"), None)
  if ch1_ch5_correct_answer:
    return render_template('/ch1_ch5_answer.html', user_answers=user_answers, ch1_ch5_answer=ch1_ch5_correct_answer)
  else:
    return "Ch.1 - Ch.5 answers not found.", 404
  
@app.route('/breathFirstSearchQuiz', methods=['GET'])
def breath_first_search_quiz():
  return render_template('/breathFirstSearchQuiz.html')

@app.route('/submit_breathFirstSearch_quiz', methods=['POST'])
def breath_first_search():
  user_answers = {key: request.form.get(key, "") for key in ["question1", "question2", "question3", "question4", "question5", "question6"]}
  breath_first_search_answer = next((item for item in quiz_data if item["id"] == "BreathFirstSearch Answer"), None)
  if breath_first_search_answer:
    return render_template('./breathFirstSearchAnswer.html', user_answers=user_answers, breath_first_search=breath_first_search_answer)
  else:
    return "Breath First Search answers not found.", 404
  
  
if __name__ == '__main__':
  app.run(debug=True)