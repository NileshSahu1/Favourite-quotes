from flask import Flask ,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:smart@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://qpixtmjrwblaiz:e73a13572a564e0f02ca2aac7035c68742fe2fd5ea20dc7046fff0e14974c72d@ec2-52-200-134-180.compute-1.amazonaws.com:5432/d2jebl0cuunrer'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

class Favquotes(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	author = db.Column(db.String(30))
	quote = db.Column(db.String(2000))


@app.route('/')
def index():
	result = Favquotes.query.all()
	return render_template('index.html',result=result)


@app.route('/quotes')
def quotes():
	 return render_template('quotes.html')

@app.route('/process', methods =['POST'])
def process():
	author = request.form['author']
	quote = request.form['quote']
	quotedata =Favquotes(author=author,quote=quote) # add to favquotes table in database
	db.session.add(quotedata)  # add data to database
	db.session.commit()   # commit it to database

	return redirect(url_for('index'))


   	  #else:
		 #return render_template('quotes.html')
