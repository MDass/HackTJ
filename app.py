from flask import Flask, session, render_template

app = Flask(__name__)

@app.route("/")
def search():
    # Search engine API
    return render_template('inputform.html') # creating webpage

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
