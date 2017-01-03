from flask import Flask
from flask import redirect
from flask import url_for
import ssdp
import roku
import os

# Initialize, read app configuration and setup
app = Flask(__name__)
port = int(os.getenv('VCAP_APP_PORT', 8080))
try:
    print "finding roku..."
    rokuUrl = str(ssdp.discover("roku:ecp"))
    print "roku found at: "+ rokuUrl
except:
    print "Error getting finding roku... setting to default"
    rokuUrl = "http://192.168.1.133:8060/"


# keys
@app.route('/home')
def home():
    returnString = roku.keyPress(rokuUrl, roku.Keys['Home'])
    return redirect(url_for('status'))


@app.route('/play')
def play():
    returnString = roku.keyPress(rokuUrl, roku.Keys['Play'])
    return redirect(url_for('status'))


@app.route('/back')
def back():
    returnString = roku.keyPress(rokuUrl, roku.Keys['Back'])
    return redirect(url_for('status'))


@app.route('/enter')
def enter():
    returnString = roku.keyPress(rokuUrl, roku.Keys['Enter'])
    return redirect(url_for('status'))


@app.route('/select')
def select():
    returnString = roku.keyPress(rokuUrl, roku.Keys['Select'])
    return redirect(url_for('status'))


@app.route('/info')
def info():
    returnString = roku.keyPress(rokuUrl, roku.Keys['Info'])
    return redirect(url_for('status'))

@app.route('/right')
def right():
    returnString = roku.keyPress(rokuUrl, roku.Keys['Right'])
    return redirect(url_for('status'))

@app.route('/left')
def left():
    returnString = roku.keyPress(rokuUrl, roku.Keys['Left'])
    return redirect(url_for('status'))

@app.route('/up')
def up():
    returnString = roku.keyPress(rokuUrl, roku.Keys['Up'])
    return redirect(url_for('status'))

@app.route('/down')
def down():
    returnString = roku.keyPress(rokuUrl, roku.Keys['Down'])
    return redirect(url_for('status'))




# launch apps
@app.route('/Netflix')
def Netflix():
    roku.launchAppByID(rokuUrl, roku.Channels['Netflix'])
    return redirect(url_for('status'))


@app.route('/Amazon')
def Amazon():
    roku.launchAppByID(rokuUrl, roku.Channels['Amazon'])
    return redirect(url_for('status'))


@app.route('/HBO')
def HBO():
    roku.launchAppByID(rokuUrl, roku.Channels['HBO_GO'])
    return redirect(url_for('status'))




# search
@app.route('/searchNetflix/<string>')
def searchNetflix(string):
    roku.searchContent(rokuUrl, string, roku.ContentType['Movie'], roku.Channels['Netflix'])
    return redirect(url_for('status'))


@app.route('/searchAmazon/<string>')
def searchAmazon(string):
    roku.searchContent(rokuUrl, string, roku.ContentType['Movie'], roku.Channels['Amazon'])
    return redirect(url_for('status'))


@app.route('/searchHBO/<string>')
def searchHBO(string):
    roku.searchContent(rokuUrl, string, roku.ContentType['Movie'], roku.Channels['HBO_GO'])
    return redirect(url_for('status'))


# Info
@app.route('/')
def status():
    print "RokuURL: "+ rokuUrl
    returnString = roku.getActiveApp(rokuUrl)
    return str(returnString)


# Info
@app.route('/apps')
def apps():
    returnString = roku.getApps(rokuUrl)
    return str(returnString)


# main definition
if __name__ == '__main__':
    app.run('0.0.0.0', port)
