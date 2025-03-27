from flask import Flask, render_template, request

app = Flask(__name__)

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


if __name__ == '__main__':
  app.run(debug=True)