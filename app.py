'''
Bayan Berri
SoftDev1 p7
hw13--  A RESTful Journey skyward
2017-11-10

'''
from flask import Flask, render_template, session, url_for, redirect, request
import urllib2
import json

app = Flask(__name__)

@app.route("/")
def root():
    data = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=cQGPw3WcqhhqGcvkbjnH5nTux27lcWYsZ0YfK8gE")
    print "\n\n~~~~~~~~~~~~~~printing data.geturl~~~~~~~~~~~~~~~~\n\n"
    print data.geturl()
    print "\n\n\n ~~~~~~~~~~~~~~ printing info()~~~~~~~~~~~~~~~~~~~~"
    print data.info()
    print "\n\n\n ~~~~~~~~~~~~~~ printing read()"
    string= data.read()
    print string
    d= json.loads(string)

    currencyKey= urllib2.urlopen("http://apilayer.net/api/live?access_key=0fec2f60496646d29dcf96603bcc07f0")
    currstr=currencyKey.read()
    dictionary=json.loads(currstr)
    newdict= dictionary["quotes"]

    return render_template("temp.html", Pic=d["url"],explanation=d["explanation"],di=newdict)



if __name__ == "__main__":
    app.debug = True
    app.run()
