from flask import Flask, request
from flask_cors import CORS
import easyocr

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

reader = easyocr.Reader(['en'])

@app.route("/file", methods=['POST'])
def file():
    image = request.files['image'].read()

    result = reader.readtext(image, detail=0, paragraph=True)
    print(result)

    string = "\n".join(result)
    return string

@app.route("/link", methods=['POST'])
def link():
    image = request.json['body']

    result = reader.readtext(image, detail=0, paragraph=True)
    print(result)

    string = "\n".join(result)
    return string

if __name__ == "__main__":
    app.run(debug=True)