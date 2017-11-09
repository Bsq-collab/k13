'''

along with a bit of explanation of the image content.
(You need only 2 files to accomplish this.)
Store your work in the workshop under 13_rest, as lastF

'''
from flask import Flask, render_template, session, url_for, redirect, request
import urllib2
import json


app = Flask(__name__)
data = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=cQGPw3WcqhhqGcvkbjnH5nTux27lcWYsZ0YfK8gE")
#data= data.read()


@app.route("/")
def root():
    print "\n\n~~~~~~~~~~~~~~printing data.geturl~~~~~~~~~~~~~~~~\n\n"
    #print data.geturl()
    print "\n\n\n ~~~~~~~~~~~~~~ printing info()~~~~~~~~~~~~~~~~~~~~"
    #print data.info()
    print "\n\n\n ~~~~~~~~~~~~~~ printing read()"
    string= data.read()
    print string
    d= json.loads(string)
    print "adeeb thinks he's cool"
   # d= str(d);
    return render_template("temp.html", Pic=d["url"],explanation=d["explanation"])
#return data.read()
    '''


'''

if __name__ == "__main__":
    app.debug = True
    app.run()
