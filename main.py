from flask import Flask, render_template, g, request, redirect, session

app = Flask(__name__)

# Secret key is necessary for creating user sessions within the app
app.secret_key = 'D8K27qBS8{8*sYVU>3DA530!0469x{'

@app.route("/")
def login():
    return render_template("home.html")

if __name__ == "__main__":
    app.run()
