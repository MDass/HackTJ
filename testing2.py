from flask import Flask, render_template

app = Flask(__name__, static_url_path='')


@app.route("/")
def home():
    return app.send_static_file('index.html')
    return 'Hello world'
  # return render_template("index.html")


def main():
    app.run()
    pass

if __name__ == '__main__':
    main()
