from flask import Flask, render_template, url_for
from second import second

app = Flask(__name__)
app.register_blueprint(second, url_prefix="/admin")

@app.route("/homee")
def home():
	return render_template("home.html")

@app.route("/test")
def test():
	return "<h1>Test</h1>"

if __name__=="__main__":
	app.run(debug=True)
