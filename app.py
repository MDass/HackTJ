from flask import Flask, session, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Search engine API
    return render_template("http://www.slimsearch.com/index.html") # creating webpage

@app.route("/inputform". methods=["GET", "POST"])
def inputform():
    if request.method == "POST":
        return redirect(url_for('index'))
    return render_template("http://www.slimsearch.com/inputform.html")

@app.route("/contact")
def contact():
    return render_template("http://www.slimsearch.com/contact.html")

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
