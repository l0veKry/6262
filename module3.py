import requests
import time
import json

data_referrer = []
# data_communicating = []
data_url = []
data_downloaded = []

def mainfunc(url):
    res=get_virustotal(url)
    with open("module3.json", "w+") as write_file:
        json.dump(res, write_file)

def get_virustotal(url):
    print("Start virustotal scanning: ")
    url_general = 'https://www.virustotal.com/vtapi/v2/domain/report'
    params = {'apikey': '150ba424391dcd507689bd802dfdea3f2bab8ac289bc4b31079abc541c44024f', \
              'domain': url}
    response = requests.get(url_general, params=params)
    data_general = response.json()
    time.sleep(14)

    if 'detected_referrer_samples' not in data_general:
        print("Reference not detected")
    else:
        referrers = data_general['detected_referrer_samples']
        for referrer in referrers:
            if referrer['positives'] > 5:
                sha_id = referrer['sha256']
                print(sha_id)
                url_file = 'https://www.virustotal.com/vtapi/v2/file/report'
                params = {'apikey': '150ba424391dcd507689bd802dfdea3f2bab8ac289bc4b31079abc541c44024f', \
                        'resource': sha_id, 'allinfo': True}
                response = requests.get(url_file, params=params)
                data_json = response.json()
                scans = data_json['scans']
                res = {}
                for key in scans:
                    if scans[key]['detected']:
                        res[key] = scans[key]
                if res:
                    data_referrer.append(res)
                time.sleep(15)
        print("Files referring analysis finished...")

    # communicatings = data_general['detected_communicating_samples']
    if 'detected_referrer_samples' not in data_general:
        print("Urls not detected")
    else:
        urls = data_general['detected_urls']
        for url in urls:
            if url['positives'] > 0:
                url_id = url['url']
                print(url_id)
                url_url = 'https://www.virustotal.com/vtapi/v2/url/report'
                params = {'apikey': '150ba424391dcd507689bd802dfdea3f2bab8ac289bc4b31079abc541c44024f', \
                        'resource': url_id}
                response = requests.get(url_url, params=params)
                data_json = response.json()
                scans = data_json['scans']
                res = {}
                for key in scans:
                    if scans[key]['detected']:
                        res[key] = scans[key]
                if res:
                    data_url.append(res)
                time.sleep(15)
        print("URL analysis finished...")

    if 'detected_downloaded_samples' not in data_general:
        print("Downloads not detected")
    else:
        downloadeds = data_general['detected_downloaded_samples']
        for downloaded in downloadeds:
            if downloaded['positives'] > 0:
                sha_id = referrer['sha256']
                print(sha_id)
                url_file = 'https://www.virustotal.com/vtapi/v2/file/report'
                params = {'apikey': '150ba424391dcd507689bd802dfdea3f2bab8ac289bc4b31079abc541c44024f', \
                        'resource': sha_id, 'allinfo': True}
                response = requests.get(url_file, params=params)
                data_json = response.json()
                scans = data_json['scans']
                res = {}
                for key in scans:
                    if scans[key]['detected']:
                        res[key] = scans[key]
                if res:
                    data_downloaded.append(res)
                time.sleep(15)
        print("Downloaded files analysis finished...")
        # for communicating in communicatings:
        #     sha_id = referrer['sha256']
        #     url_file = 'https://www.virustotal.com/vtapi/v2/file/report'
        #     params = {'apikey': '150ba424391dcd507689bd802dfdea3f2bab8ac289bc4b31079abc541c44024f', \
        #               'resource': sha_id}
        #     response = requests.get(url_file, params=params)
        #     data_json = response.json()

    report = {}
    report['referrer'] = data_referrer
    report['downloaded'] = data_downloaded
    report['url'] = data_url
    return report
        

if __name__ == "__main__":
    with open('test.txt', 'r') as f:
        for line in f:
            report = get_virustotal(line)
            print("Report analysis finished...")

    with open('vt_report.txt', 'w') as w_f:
        json.dump(report, w_f)
        print("Report successfullly saved...")