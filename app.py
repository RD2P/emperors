from flask import Flask, render_template, jsonify
from db import get_emperors_from_db

app = Flask(__name__)
  
emperors_list = get_emperors_from_db()

@app.route('/')
def home():
  return render_template("index.html", emperors=emperors_list)

@app.route('/api')
def emperors_api():
   return jsonify(emperors_list)

if __name__ == '__main__':
    app.run(debug=True)
  