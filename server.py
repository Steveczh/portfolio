
from flask import Flask, render_template, url_for,request
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')

@app.route("/components.html")
def blog():
    return render_template('components.html')

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a',newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data =request.form.to_dict()
        write_to_csv(data)
        return '<p>form submitted<p/>'
    else:
        return '<p>something went wrong <p/>'
    


# $ export FLASK_APP=sample
# $ export FLASK_ENV=development
# $ flask run