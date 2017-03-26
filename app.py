from flask import Flask, session, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Search engine API
    return render_template('index.html') # creating webpage

@app.route("index")
def inputform():
    return render_template("inputform")

@app.route("index")
def contact():
    return render_template("contact")

def result():
    pass
    # Big Parser API to generate grid
"""
@app.route("/")
def main():
  return "Hello!"
"""
if __name__ == "__main__":
  app.run()
