from flask import Flask, jsonify
app = Flask(__name__)





@app.route("/pocasi")
def hello():
    return jsonify({"OK": "OK"})
