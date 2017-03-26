from flask import Flask, render_template, request
import json
import csv
from google import search
from bs4 import BeautifulSoup
import urllib

app = Flask(__name__)

import pygsheets
import sys

Google_Workbook = u''
Google_Sheet_in_Workbook = u''

def read_csv(ifile):
    with open(ifile) as file:
        reader = csv.reader(file, delimiter=',', quotechar='|')
        rows = []
        for row in reader:
            rows.append(row)
        return rows

def google_scrape(url):
    thepage = urllib.urlopen(url)
    soup = BeautifulSoup(thepage, "html.parser")
    if (soup.title):
        return soup.title.text
    return None

def receive(query):
    websites = {}
    i = 1
    # iterate through dictionaries
    c = 0
    while c < query.values():
        for url in search(query.values()[c], stop=50):
            a = google_scrape(url)
            websites[a] = url
            i += 1
            c += 1
    data = json.dumps(websites)
    convert()

def convert():
    websites_csv = open('C:/Users/angel/OneDrive/Documents/GitHub/HackTJ/csv/websitesData.csv', 'w') # opens file for writing
    csvwriter = csv.writer(websites_csv) # creates the csv writer objects
    count = 0
    for i in websites:
        if count == 0:
            header = websites.keys()
            csvwriter.writerow(header)
            count += 1
        csvwriter.writerow(websites.values())
    websites_csv.close()

@app.route("/submit", methods = ["POST"]) # "GET"
def submit():
    text = receive(request.form)
    return text

@app.route("/")
@app.route("/index2.html")
def home():
  return render_template("index2.html")

@app.route("/contact2.html")
def contact():
  return render_template("contact2.html")

@app.route("/")
@app.route("/inputform2.html")
def inputform():
  return render_template("inputform2.html")

def main(ifile):
    gc = pygsheets.authorize(
        outh_file='C:/Users/angel/OneDrive/Documents/GitHub/HackTJ/client_secret.json',
        outh_nonlocal=True)
    all_sheets = gc.list_ssheets()
    all_names = [sheet['name'] for sheet in all_sheets]
    sh = gc.open(Google_Workbook)
    wks = sh.worksheet_by_title(Google_Sheet_in_Workbook)
    to_insert = read_csv(ifile)
    for row in to_insert:
        rows = len(wks.get_col(1, returnas='cell', include_empty=False))
        wks.append_row(start=("A" + str(rows + 1)),
                       end=None, values=row)
    sh = gc.close()

if __name__ == "__main__":
   #app.run(threaded = True)
   if len(sys.argv) == 2:
       main(sys.argv[0])
   else:
       # Input CSV filename, Output Google Spreadsheet name
       print("Error: Wrong number of arguments\nUsage: python auth.py <CSV filename>")
