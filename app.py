from flask import Flask, render_template, request
from html2mail.process import process
from bs4 import BeautifulSoup as bs

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process_file():
    soup = bs(request.form['htmlInput'])  # make BeautifulSoup
    original = soup.prettify()
    file_process = process(original)
    soup = bs(' '.join(file_process))  # make BeautifulSoup
    return render_template('index.html', original_file=original, file_process=soup.prettify())


if __name__ == '__main__':
    app.run()
