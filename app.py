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

def collect_answers(keys):
  return {key: request.form.get(key, "")for key in keys}

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/category', methods=['GET'])
def category():
  return render_template('category.html')

@app.route('/selection_sort', methods=['GET', 'POST'])
def selection_sort():
  if request.method == 'POST':
    return 'Form submitted successfully!'
  return render_template('selection_sort.html')

@app.route('/quicksort_quiz', methods=['GET'])
def quicksort_quiz():
  return render_template('quicksort_quiz.html')

@app.route('/submit_quicksort_quiz', methods=['POST'])
def quicksort_answers():
  user_answers = collect_answers([
    "question1", "question2", "question3", "question4", "question5"
  ])
  quicksort_correct_answers = next((item for item in quiz_data if item["id"] == "Quicksort Answer"), None)
  if quicksort_correct_answers:
    return render_template('quicksort_answer.html', user_answers=user_answers, quicksort_answers=quicksort_correct_answers)
  else:
    return "Quicksort answers not found.", 404

@app.route('/hash_tables_quiz', methods=['GET'])
def hash_tables_quiz():
  return render_template('hash_tables_quiz.html')

@app.route('/submit_hash_tables_quiz', methods=['POST'])
def hash_tables_answers():
  user_answers = collect_answers([
    "question1", "question2", "question3", "question4", "question5"
  ])
  hash_tables_correct_answer = next((item for item in quiz_data if item["id"] == "Hash Table Answer"), None)
  if hash_tables_correct_answer:
    return render_template('hash_tables_answer.html', user_answers=user_answers, hash_tables_answers=hash_tables_correct_answer)
  else:
    return "Hash Table answers not found.", 404
  
@app.route('/ch1_ch5', methods=['GET'])
def ch1_ch5_quiz():
  return render_template('ch1_ch5.html')

@app.route('/submit_ch1_ch5_quiz', methods=['POST'])
def ch1_ch5():
  user_answers = collect_answers([
    "question1", "question2", "question3", "question4", "question5", "question6", 
    "question7", "question8", "question9", "question10", "question11", "question12", 
    "question13", "question14", "question15"
  ])
  ch1_ch5_correct_answer = next((item for item in quiz_data if item["id"] == "ch1_ch5 Answer"), None)
  if ch1_ch5_correct_answer:
    return render_template('ch1_ch5_answer.html', user_answers=user_answers, ch1_ch5_answer=ch1_ch5_correct_answer)
  else:
    return "Ch.1 - Ch.5 answers not found.", 404
  
@app.route('/breadth_first_search_quiz', methods=['GET'])
def breadth_first_search_quiz():
  return render_template('breadth_first_search_quiz.html')

@app.route('/submit_breadth_first_search_quiz', methods=['POST'])
def breath_first_search():
  user_answers = collect_answers([
    "question1", "question2", "question3", "question4", "question5", "question6"
  ])
  breadth_first_search_answer = next((item for item in quiz_data if item["id"] == "Breadth-First Search Answer"), None)
  if breadth_first_search_answer:
    return render_template('breadth_first_search_answer.html', user_answers=user_answers, breadth_first_search=breadth_first_search_answer)
  else:
    return "Breath First Search answers not found.", 404
  
@app.route('/dijkstra_algo_quiz', methods=['GET'])
def dijkstra_quiz():
  return render_template('dijkstra_algo_quiz.html')

@app.route('/submit_dijkstras_quiz', methods=['POST'])
def dijkstra_quiz_answer():
  user_answers = collect_answers([
    "question1", "question2", "question3", "question4", "question5", "question6"
  ])
  dijkstra_answers = next((item for item in quiz_data if item["id"] == "Dijkstras Algorithm Answer"), None)
  if dijkstra_answers:
    return render_template('dijkstra_algo_answers.html', user_answers=user_answers, dijkstra_algo_answers=dijkstra_answers)
  else:
    return "Dijkstra's Algorithm answers not found.", 404

if __name__ == '__main__':
  app.run(debug=True)