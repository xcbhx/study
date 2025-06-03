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

@app.route('/intro_algo_quiz', methods=['GET'])
def intro_algorithms_quiz():
  return render_template('intro_to_algo_quiz.html')

@app.route('/submit_intro_algo_quiz', methods=['POST'])
def intro_algorithms_answers():
  user_answers = collect_answers([
    "question1", "question2", "question3", "question4", "question5", "question6"
  ])
  intro_algorithms_correct_answers = next((item for item in quiz_data if item["id"] == "Intro Algorithms Answer"), None)
  if intro_algorithms_correct_answers:
    return render_template(
      'intro_to_algo_answer.html',
      questions=intro_algorithms_correct_answers["questions"],
      user_answers=user_answers
      )
  return "Introduction to Algorithms answers not found.", 404

@app.route('/selection_sort_quiz', methods=['GET'])
def selection_sort_quiz():
  return render_template('selection_sort_quiz.html')

@app.route('/selection_sort_results', methods=['POST'])
def selection_results():
  user_answers = collect_answers([
    "question1", "question2", "question3", "question4", "question5", "question6"
  ])
  selection_sort_answers = next((item for item in quiz_data if item["id"] == "Selection Sort Answers"), None)
  if selection_sort_answers:
    return render_template(
      'selection_sort_results.html',
      questions=selection_sort_answers["questions"],
      user_answers=user_answers
      )
  return "Selection Sort answers not found.", 404

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
  

@app.route('/greedy_algo_quiz', methods=['GET'])
def greedy_quiz():
  return render_template('greedy_algo_quiz.html')


@app.route('/submit_greedy_quiz', methods=['POST'])
def greedy_quiz_answer():
  user_answers = collect_answers([
    "question1", "question2", "question3", "question4", "question5", "question6"
  ])
  greedy_answers = next((item for item in quiz_data if item["id"] == "Greedy Algorithm Answer"), None)
  if greedy_answers:
    return render_template('greedy_algo_answers.html', user_answers=user_answers, greedy_algo_answers=greedy_answers)
  else:
    return "Greedy Algorithm answers not found.", 404
  
@app.route('/dynamic_programming_quiz', methods=['GET'])
def dynamic_quiz():
  return render_template('dynamic_programming_quiz.html')

@app.route('/submit_dynamic_quiz', methods=['POST'])
def dynamic_quiz_answer():
  user_answers = collect_answers([
    "question1", "question2", "question3", "question4", "question5", "question6"
  ])
  dynamic_answers = next((item for item in quiz_data if item["id"] == "Dynamic Programming Answer"), None)
  if dynamic_answers:
    return render_template('dynamic_programming_answers.html', user_answers=user_answers, dynamic_programming_answers=dynamic_answers)
  else:
    return "Dynamic Programming answers not found.", 404

@app.route('/k_nearest_neighbors_quiz', methods=['GET'])
def k_nearest_neighbors_quiz():
  return render_template('k_nearest_neighbors_quiz.html')

@app.route('/submit_k_nearest_neighbors_quiz', methods=['POST'])
def k_nearest_neighbors_quiz_answer():
  user_answers = collect_answers([
    "question1", "question2", "question3", "question4", "question5", "question6"
  ])
  k_nearest_neighbors_answers = next((item for item in quiz_data if item["id"] == "K-nearest Neighbors Answer"), None)
  if k_nearest_neighbors_answers:
    return render_template('k_nearest_neighbors_answers.html', user_answers=user_answers, k_nearest_neighbors_answers=k_nearest_neighbors_answers)
  else:
    return "k-Nearest neighbors answers not found.", 404
  
@app.route('/ch6_ch10', methods=['GET'])
def ch6_ch10_quiz():
  return render_template('ch6_ch10.html')

@app.route('/submit_ch6_ch10_quiz', methods=['POST'])
def ch6_ch10():
  user_answers = collect_answers([
    "question1", "question2", "question3", "question4", "question5", "question6", 
    "question7", "question8", "question9", "question10", "question11", "question12", 
    "question13", "question14", "question15"
  ])
  ch6_ch10_correct_answer = next((item for item in quiz_data if item["id"] == "ch6_ch10 Answer"), None)
  if ch6_ch10_correct_answer:
    return render_template('ch6_ch10_answer.html', user_answers=user_answers, ch6_ch10_answer=ch6_ch10_correct_answer)
  else:
    return "Ch.6 - Ch.10 answers not found.", 404

if __name__ == '__main__':
  app.run(debug=True, port=5001)