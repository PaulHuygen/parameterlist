#!/usr/bin/python
import os
from threading import Lock
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)

lock = Lock()

num = 0

@app.route("/")
def hello():
    global num
    with lock:
        num = num + 1
        thisnum = num
#        return "Hello World! for the {}-th time".format(thisnum)
        return "{}".format(thisnum)

@app.route("/uploadparfile", methods=['GET', 'POST'])
def upload_parfile():
    ret = "NOPE"
    if request.method == 'POST':
        file = request.files['file']
#        partext = request.files['file'].read()
#        ret = partext
        return ret        
#        if file and allowed_file(file.filename):
#            filename = secure_filename(file.filename)
#            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#            return redirect(url_for('uploaded_file',
#                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


if __name__ == "__main__":
    app.debug = True
    app.run()
