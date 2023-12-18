from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

with open('emperors.json', 'r') as file:
  json_data = file.read() #string
  emperors = json.loads(json_data)
  # print(emperors[0]['name'])

@app.route('/')
def home():
  return render_template("index.html", emperors=emperors)

@app.route('/api')
def emperors_api():
  with open('emperors.json', 'r') as file:
    json_data = file.read() #string

  return json.loads(json_data)

if __name__ == '__main__':
    app.run(debug=True)