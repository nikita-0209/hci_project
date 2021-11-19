from flask import Flask, jsonify, request, send_file, send_from_directory, safe_join, abort
from flask_cors import CORS
import os
from demo import doWork

app = Flask(__name__)
CORS(app)


# Defining the home page of our site


@app.route("/mp3file", methods=['POST'])  # this sets the route to this page
def filething():
    # print("random")
    if request.files:
        print(request.files['file'])
        mp3file = request.files['file']
        path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), mp3file.filename)
        # print("**")
        # print(path)
        # print("--")
        # print(os.path.realpath(__file__))
        # print("&&")
        # print(os.path.dirname(os.path.realpath(__file__)))
        mp3file.save(path)
        doWork(mp3file.filename)

    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "FINAL.wav")
    return send_file(path, as_attachment=True)
    # return send_from_directory(app.config["CLIENT_REPORTS"], filename=path, as_attachment=True)
    # return jsonify({"key": "Hello world"})  # some basic inline html


if __name__ == "__main__":
    app.run(debug=True)
