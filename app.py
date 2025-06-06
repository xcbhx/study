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

# Quiz route that dynamically display each quiz
@app.route('/quiz/<quiz_id>', methods=['GET'])
def show_quiz(quiz_id):
  quiz_display_name = quiz_id.replace('_', ' ').title() + " Answers"
  quiz = next((q for q in quiz_data if q["id"] == quiz_display_name), None)

  if not quiz:
    return f"Quiz '{quiz_id}' not found.", 404
  
  return render_template(
    'quiz_template.html', 
    quiz_id=quiz_id, 
    questions=quiz["questions"])

# Dynamically display each quiz result
@app.route('/quiz/<quiz_id>/submit', methods=['POST'])
def submit_quiz(quiz_id):
  quiz_display_name = quiz_id.replace('_', ' ').title() + " Answers"
  quiz = next((q for q in quiz_data if q["id"] == quiz_display_name), None)

  if not quiz:
    return f"Answers for '{quiz_id}' not found.", 404
  
  num_questions = len(quiz["questions"])
  user_answers = collect_answers([f"question{i}" for i in range(1, num_questions + 1)])
  
  return render_template(
    'quiz_results_template.html', 
    quiz_id=quiz_id, 
    questions=quiz["questions"],
    user_answers=user_answers
    )

if __name__ == '__main__':
  app.run(debug=True, port=5001)