from flask import Flask, render_template, request
import os
from stuff import *
import camelot
import numpy as np
import pandas as pd
import json
from stuff import *
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './input'

@app.route('/')
def pt1():
    return 'lol'
    # file = "../input/11okt10nov.pdf"
    # file = open('input/11okt10nov.pdf','rb')
    cellinfo = []

    tables = camelot.read_pdf(file,pages='1-end')
    cellinfo = tablestocellinfo(tables)

    with open('celldata1.json', 'w') as f:
        json.dump(cellinfo,f)

    docs = []

    # tables[0].col = tables[0].df.col + 1
    # tables[0].row = tables[0].df.row + 2

    # tables[1].col = tables[1].df.col + 1
    # tables[1].row = tables[1].df.row + 1


    cleanuptables(tables,docs)
    return str(docs)
# def first_page():
#     return render_template('first_page.html')

@app.route('/response_page', methods = ['POST'])
def response_page():
    name = request.form['name']    
    return render_template('response_page.html', name=name)

@app.route('/upload')
def upload_files():
   return render_template('/upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
        f = request.files['file']
        print(f)
        filename = f.filename
        # f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],'input.pdf'))
        # file = os.path.join(app.config['UPLOAD_FOLDER'],'input.pdf')
        return 'file uploaded'
        
if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        port = process.env.PORT
        app.run(host='0.0.0.0', port=port)
        #app.run()