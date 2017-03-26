from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/")
def contact():
  return render_template("contact.html")

@app.route("/")
def inputform():
  return render_template("inputform.html")

if __name__ == "__main__":
  app.run()
