from flask import render_template
from flaskr import app
from flaskr.database import db
from flask import Flask , redirect , url_for ,request , send_from_directory
from flaskr.model import Entry
from werkzeug import secure_filename
import os




# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = '/flaskr/static/uploads'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/',methods=['GET'])
#@app.route('/hello/<name>')
def index():
	entries = Entry.query.all()
	return render_template('index.html',entries=entries)

@app.route('/create',methods=['POST'])
def create():
	file = request.files['file']
	if file and allowed_file(file.filename):
	  filename = secure_filename(file.filename)
	  file.save(os.getcwd() + os.path.join(app.config['UPLOAD_FOLDER'], filename))
	entry=Entry(request.values['title'],request.values['content'],file.filename)
	db.session.add(entry)
	db.session.commit()  
	return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
  return send_from_directory(os.getcwd()+app.config['UPLOAD_FOLDER'],filename)


@app.route('/new',methods=['GET'])
def new():
	return render_template('new.html')