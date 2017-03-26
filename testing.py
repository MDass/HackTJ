from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index.html")
def main():
  return render_template("http://www.slimsearch.com/")

if __name__ == "__main__":
  app.run()
