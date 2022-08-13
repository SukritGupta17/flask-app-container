from flask import Flask

app = Flask(__name__)

@app.route("/home")
def home():
	return "<p>Hello, World!</p> \n Welcome home."

