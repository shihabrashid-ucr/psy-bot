from flask import Flask, render_template, request, jsonify
from backend_dialogue import *

app = Flask(__name__)
backend_manager = BackendDialogue()

@app.route("/")
def home():    
    return render_template("index.html")

@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg') 
    return str(backend_manager.get_answer(userText))

if __name__ == "__main__":
    app.run()

'''
def get_response(user_message):
    return backend_manager.get_answer(user_message)

@app.route('/')
def hello_world():
    return render_template('home2.html')

@app.route('/chat',methods=["POST"])
def chat():
    try:
        user_message = request.form["text"]
        response_text = get_response(user_message)
        return jsonify({"status":"success","response":response_text})
    except Exception as e:
        print(e)
        return jsonify({"status":"success","response":"Sorry I am not trained to do that yet..."})

if __name__ == "__main__":
    app.run()
'''
