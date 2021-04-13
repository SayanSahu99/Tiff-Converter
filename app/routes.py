from app import app
from flask import render_template, request, flash, send_file, redirect
from app.convert import convert_jpg, convert_png
import os

@app.route('/')
@app.route('/index')
def index():
  if(os.path.exists(os.path.join(os.getcwd(), 'sample.zip'))):
    os.remove(os.path.join(os.getcwd(), 'sample.zip'))
  return render_template("index.html")

@app.route('/', methods=['POST'])
def upload_file():
  if request.method == 'POST':
    if 'files[]' not in request.files:
        flash('No file part')
        return redirect(request.url)

    files = request.files.getlist('files[]')

    for file in files:
      if file.filename != '':
        file.save(os.path.join(app.config['UPLOAD_PATH'], file.filename))
        print(file.filename)

    extension = 'jpg'
    data = request.form.get('ext', extension)
    if data == 'jpg':
      convert_jpg(files)
    else:
      convert_png(files)
    return send_file(os.path.join(os.getcwd(), "sample.zip"), as_attachment=True)
