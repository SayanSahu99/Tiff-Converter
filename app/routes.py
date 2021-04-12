from app import app
from flask import render_template, request, flash, redirect;


@app.route('/')
@app.route('/index')
def index():
  return render_template("index.html");

@app.route('/', methods=['POST'])
def upload_file():
  if request.method == 'POST':

      if 'files[]' not in request.files:
          flash('No file part')
          return redirect(request.url)

      files = request.files.getlist('files[]')

      flash('File(s) successfully uploaded')
      print(files)
      return redirect('/')