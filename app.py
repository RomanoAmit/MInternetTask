from flask import Flask, render_template, json
import csv

with open("churn_case_data.csv") as csv_file:
    reader = csv.DictReader(csv_file, delimiter = ';')
    customers = [row for row in reader]
    headers =  [key for key in customers[0]]
    sections = list(dict.fromkeys([costumer['segment'] for costumer in customers]))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact')
def contact():
    return render_template('contact.html') 

@app.route('/data')
def getData():
  #  my_dict = {"title": "Bayside", "ganre":"Alternative"}
    return json.dumps(customers)

if __name__ == "__main__":
    print("running")
    app.run(debug=True)
