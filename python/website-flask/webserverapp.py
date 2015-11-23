from flask import Flask, render_template, request, redirect
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from collectAnalysis import collectAnalysis

app = Flask(__name__)
sentiment_generated = []

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
	workbookname = request.form['inputxlsx']
	#320 - 350
	collectAnalysis(workbookname, 1000, 1020, sentiment_generated)
	return render_template('post.html', sentiment_generated=sentiment_generated)
	
if __name__ == '__main__':
	app.run()