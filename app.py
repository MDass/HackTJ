from flask import Flask, session, render_template

app = Flask(__name__)

@app.route("/")
def search():
    #session['subject'] = ''
    return render_template('something.html')

"""
@app.route("/")
def main():
  return "Hello!"
"""
if __name__ == "__main__":
  app.run()
