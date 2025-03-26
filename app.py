from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/selectionsort.html')
def selection_sort():
  return render_template('selectionsort.html')


if __name__ == '__main__':
  app.run(debug=True)