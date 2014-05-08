from flask import render_template
from flaskr import app
from flask import Flask , redirect , url_for ,request
from flaskr.model import Entry




# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])


@app.route('/',methods=['GET'])
#@app.route('/hello/<name>')
def index():
	entries = Entry.query.all()
	return render_template('index.html',entries=entries)

@app.route('/upload',methods=['POST'])
def upload():
	request.files['files']
  
	return redirect(url_for('index'))


@app.route('/new',methods=['GET'])
def new():
	return render_template('new.html')