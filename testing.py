from flask import Flask, render_template
from google import search
from bs4 import BeautifulSoup
import urllib

app = Flask(__name__)

def google_scrape(url):
    thepage = urllib.urlopen(url)
    soup = BeautifulSoup(thepage, "html.parser")
    return soup.title.text

def receive():
    i = 1
    query = "search this"
    for url in search(query, stop=10):
        a = google_scrape(url)
        print str(i) + ". " + a
        print urlprint
        print " "
        i += 1
"""
@app.route("/submit", methods = ["POST"])
def submit():
    return "Hello World!"
    #return render_template("inputform.html")
"""

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
