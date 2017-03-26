from flask import Flask, render_template
import json
import csv
from google import search
from bs4 import BeautifulSoup
import urllib

app = Flask(__name__)

def google_scrape(url):
    thepage = urllib.urlopen(url)
    soup = BeautifulSoup(thepage, "html.parser")
    return soup.title.text

def receive(query):
    websites = {}
    i = 1
    for url in search(query, stop=50):
        a = google_scrape(url)
        websites[a] = url
        i += 1
    data = json.dumps(websites)

def convert():
    websites_csv = open('/tmp/websitesData.csv', 'w') # opens file for writing
    csvwriter = csv.writer(websites_csv) # creates the csv writer object
    count = 0
    for i in websites:
        if count == 0:
            header = websites.keys()
            csvwriter.writerow(header)
            count += 1
        csvwriter.writerow(websites.values())
    websites_csv.close()


@app.route("/submit", methods = ["POST"])
def submit():
    text = receive("cat")
    convert
    return "text"
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
