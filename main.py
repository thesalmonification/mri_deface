import os
from flask import Flask, flash, request, send_file, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask import send_from_directory

UPLOAD_FOLDER = './Uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return 'No file uploaded', 400
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return 'No file selected', 400
        if file: #and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


            #Perform deface here...
            os.system('./mri_deface_linux ' + os.path.join(app.config['UPLOAD_FOLDER'], filename) + ' talairach_mixed_with_skull.gca face.gca ' + os.path.join(app.config['UPLOAD_FOLDER'], 'defaced_'+ filename))

            #return redirect(url_for('download_file', name=filename))
            return send_file(os.path.join(app.config['UPLOAD_FOLDER'], 'defaced_'+ filename), as_attachment=True)
    return '''
    <!doctype html>
    <title>T1 MRI Deface Tool</title>
    <h1>Based on the MBIRN Tool from FreeSurfer</h1>
    <h3>Upload new File</h3>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


if __name__ == '__main__': 
    app.run(debug=True,port=8080,host='0.0.0.0') 