import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import numpy as np

from tensorflow import keras
from keras.preprocessing.image import load_img,img_to_array




classes = ["犬","猫"]
image_size = 64

UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = set([ 'jpg', 'jpeg', 'gif','png'])

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

model = keras.models.load_model('./pet_model.h5')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        
        if 'file' not in request.files:
            ans = 'ファイルがありません'
            return render_template("index.html",answer=ans)
        
        file = request.files['file']
        
        if file.filename == '':
            ans = 'ファイルがありません'
            return render_template("index.html",answer=ans)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            filepath = os.path.join(UPLOAD_FOLDER, filename)

            img = load_img(filepath, target_size=(image_size,image_size))
            img = img_to_array(img)
            img = np.expand_dims(img, axis=0)
            data = img /255

            result = model.predict(data)
            result = round(result[0,0])
            
            pred_answer = "これは " + classes[result] + " です"

            return render_template("index.html",answer=pred_answer)

    return render_template("index.html",answer="判定受け付け待ち")

if __name__ == "__main__":
    app.run(debug= True)   
