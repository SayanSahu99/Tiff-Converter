from app import app
from flask import render_template, request, flash, send_file, redirect
from app.convert import convert
import os

@app.route('/')
@app.route('/index')
def index():
  print(os.getcwd())
  print()
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
        file.save(os.path.join(os.path.join(os.path.realpath(__package__), "uploads"), file.filename))
        print(file.filename)

    convert(files)
    return send_file(os.path.join(os.getcwd(), "sample.zip"), as_attachment=True)
