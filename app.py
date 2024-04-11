from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# bot
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json['message']

    rasa_response = requests.post('http://localhost:5005/webhooks/rest/webhook', json={'message': user_message}).json()

    return jsonify(rasa_response)

# html
@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()