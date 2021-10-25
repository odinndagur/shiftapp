from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './input'

@app.route('/')
def first_page():
    return render_template('first_page.html')

@app.route('/response_page', methods = ['POST'])
def response_page():
    name = request.form['name']    
    return render_template('response_page.html', name=name)

@app.route('/upload')
def upload_file():
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
        app.run(host='0.0.0.0', port=port)
        #app.run()