from flask import Flask, json, render_template, request, jsonify
from classes.manager import Manager
import json

app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/question', methods=['POST'])
def handle_question():
    question = json.loads(request.data.decode()).get("user_question")

    if question:
        manager = Manager(question)
        response = manager.get_response()
        print(response)
        return jsonify(response)
    #return jsonify({})

if __name__ == "__main__":
    app.run()