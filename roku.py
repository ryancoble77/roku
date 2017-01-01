
import requests


## initialize and constants
roku_ip = '192.168.1.133'
roku_port = '8060'
rokuUrl = 'http://'+ roku_ip +':'+ roku_port


Channels = {
    'Netflix': '12',
    'Amazon': '13',
    'Sling': '46041',
    'WatchESPN': '34376',
    'RokuMedia': '2213',
    'HBO_GO': '8378'
}

ContentType = {
    'Movie': 'movie',
    'TV': 'tv-show',
    'Person': 'person',
    'Channel': 'channel',
    'Game': 'game'
}

Keys = {
    'Home': 'Home',
    'Rev': 'Rev',
    'Fwd': 'Fwd',
    'Play': 'Play',
    'Select': 'Select',
    'Left': 'Left',
    'Right': 'Right',
    'Down': 'Down',
    'Up': 'Up',
    'Back': 'Back',
    'InstantReplay': 'InstantReplay',
    'Info': 'Info',
    'Backspace': 'Backspace',
    'Search': 'Search',
    'Enter': 'Enter',
}


#function definitions
def getApps(url):
    response = requests.get(url+ '/query/apps')
    responseString = response.content
    return responseString


def getActiveApp(url):
    response = requests.get(url+ '/query/active-app')
    responseString = response.content
    return responseString


def launchAppByID(url, appID):
    response = requests.post(url+ '/launch/'+ appID)
    responseString = response.content
    return responseString


def searchContent(url, keyword, type, provider):
    response = requests.post(url+ '/search/browse?keyword='+ keyword +'&type='+ type +'&provider-id='+ provider +'&launch=true')
    responseString = response.content
    return responseString


def keyPress(url, key):
    response = requests.post(url+ '/keypress/'+ key)
    responseString = response.content
    return responseString







