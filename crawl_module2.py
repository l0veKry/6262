import sys
import requests
import time
import json


#def main(argv=None, targeturl):
def mainfunc(targeturl):
    # if argv is None:
    #     argv = sys.argv
    response1 = sslLabs(targeturl=targeturl)
    response2 = googleSafeBrowsing(targeturl=targeturl)
    with open("module2.json", "w+") as write_file:
        json.dump({'sslLabs': response1, 'googleSafeBrowsing': response2}, write_file)


def sslLabs(targeturl='https://api.ssllabs.com/api/v3'):
    print("Start ssllabs scanning: ")
    params = {
        'host': targeturl,
        'all': 'on'
    }
    url = 'https://api.ssllabs.com/api/v3'
    endpoint = '/analyze'
    r=requests.get(url=url + endpoint, params=params)
    #status=r.json()['status']
    #while status != "READY":
    #    time.sleep(1.5)
    #    r=requests.get(url=url + endpoint, params=params)
    #    status=r.json()['status']
    return r.json()


def googleSafeBrowsing(targeturl='http://www.urltocheck1.org/'):
    print("Start googleSafeBrowsing scanning: ")
    key = 'AIzaSyA37o9cWU3C89VQQl5C2pXP2R7vHup3vnU'
    url = 'https://safebrowsing.googleapis.com/v4/'
    endpoint = 'threatMatches:find?key=' + key
    # contentType = {'Content-Type': 'application/json'}
    payload = {
        "client": {
            "clientId": 'com.cs6262module2.gatech',
            "clientVersion": "1.5.2"
        },
        "threatInfo": {
            "threatTypes": ["THREAT_TYPE_UNSPECIFIED", "MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL", "THREAT_ENTRY_TYPE_UNSPECIFIED", "EXECUTABLE"],
            "threatEntries": [
                {"url": targeturl},
            ]
        }
    }
    r = requests.post(url=url + endpoint, json=payload)
    return r.json()


if __name__ == "__main__":
    sys.exit(mainfunc)