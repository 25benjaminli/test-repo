from flask import Flask, render_template, request, redirect, url_for
# import mysql.connector

import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/img'

alldocs = []
app = Flask(__name__)

# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']) #configure later
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def index():
    return render_template('main.html')

# def render_downloads():
#   print("here3") #works IF you do it outside of repl.
#   return render_template("download_docs.html", images = allphotos)

@app.route('/a')
def file():
  return render_template("a.html")
@app.route('/file', methods=['POST', 'GET'])
def upload_file():
  if request.method == "GET":
    return render_template("index.html")
  if request.method == "POST":
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
        return redirect('/')
    return redirect('/')
    
@app.route('/download', methods = ['GET'])
def show_downloads():
  print("here4")
  for filename in os.listdir('static/img'):
    # if (filename == "") ben in the GRIND still a grind lets go 
      if not os.path.join(app.config['UPLOAD_FOLDER'], filename) in alldocs and not filename.endswith(".css"): # need to make it check if it is a folder, in which you don't want it to print.
        # allphotos.append(os.path.join('downloads', filename))
        alldocs.append(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      else:
          continue
  
  print("here3") #works IF you do it outside of repl.
  return render_template("download_docs.html", alldocs = alldocs)
  

@app.route('/file_test', methods = ['POST', 'GET'])
def upload_file_test():
  if request.method == "GET":
    return render_template("index.html")
  if request.method == "POST":
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
      filename = secure_filename(uploaded_file.filename)
      uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      return redirect('/download')
    return redirect('/download')



if __name__ == "__main__":
  app.run(debug = True, host = "0.0.0.0") 

