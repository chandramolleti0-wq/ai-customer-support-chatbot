from flask import Flask, render_template, request
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("chatbot.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.form["message"]

    bot_reply = get_response(user_message)

    return bot_reply

if __name__ == "__main__":
    app.run(debug=True)