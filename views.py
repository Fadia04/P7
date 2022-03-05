from flask import Flask, json, render_template, request, jsonify
from classes.manager import Manager
<<<<<<< HEAD
import json
=======
from classes.messages import negative_responses
from random import choice
import json
import os
>>>>>>> afa3ce2cccc9609d925ed4674cfb213557abe24d

app = Flask(__name__)

@app.route('/')
def index():
    """Function to display website"""
    google_api_key = os.getenv("GOOGLE_SECRET_KEY")
    return render_template('index.html', google_api_key =google_api_key )

@app.route('/question', methods=['POST'])
def handle_question():
<<<<<<< HEAD
=======
    """Function with request POST allowed to use the user's question if exits from javascript file and instanciate 
    the Manager class in order to return the response to javascript and the front end """
>>>>>>> afa3ce2cccc9609d925ed4674cfb213557abe24d
    question = json.loads(request.data.decode()).get("user_question")

    if question:
        manager = Manager(question)
        response = manager.get_response()
        print(response)
        return jsonify(response)
    return jsonify({"status": "nok", "message": choice(negative_responses)})

if __name__ == "__main__":
    app.run()