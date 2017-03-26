from flask import Flask, render_template
from google import search
from bs4 import BeautifulSoup
import urllib

app = Flask(__name__)

def google_scrape(url):
    thepage = urllib.urlopen(url)
    soup = BeautifulSoup(thepage, "html.parser")
    return soup.title.text

def receive(query):
    i = 1
    for url in search(query, stop=len(query)-1):
        a = google_scrape(url)
        print str(i) + ". " + a
        print urlprint
        print " "
        i += 1

@app.route("/submit", methods = ["POST"])
def submit():
    text = query("cat")
    return "Hello World!"
    #return render_template("inputform.html")


@app.route("/")
@app.route("/index2.html")
def home():
  return render_template("index2.html")


@app.route("/contact2.html")
def contact():
  return render_template("contact2.html")

@app.route("/inputform2.html")
def inputform():
  return render_template("inputform2.html")



if __name__ == "__main__":
  app.run()
