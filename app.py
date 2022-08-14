import os

from flask import Flask

app = Flask(__name__)

@app.route("/home")
def home():
	return "<p>Hello, World!</p> \n Welcome home."

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))