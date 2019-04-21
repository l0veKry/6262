import requests
import time
import json

data_referrer = []
data_url = []
data_downloaded = []

def get_virustotal(url):
    url_general = 'https://www.virustotal.com/vtapi/v2/domain/report'
    params = {'apikey': '150ba424391dcd507689bd802dfdea3f2bab8ac289bc4b31079abc541c44024f', \
              'domain': url}
    response = requests.get(url_general, params=params)
    data_general = response.json()
    # print(data_general)
    time.sleep(14)

    report = {}

    if 'detected_referrer_samples' not in data_general.keys():
        has_referrers = False
    else:
        has_referrers = True
        referrers = data_general['detected_referrer_samples']

    if 'detected_urls' not in data_general.keys():
        has_urls = False
    else:
        has_urls = True
        urls = data_general['detected_urls']

    if 'detected_downloaded_samples' not in data_general.keys():
        has_downloaded = False
    else:
        has_downloaded = True
        downloadeds = data_general['detected_downloaded_samples']
    
    if has_referrers == False and has_downloaded == False and has_urls == False:
        report['detect'] = False
        print("No malicious found!!!")
        return report

    report_referrers = False
    report_downloaded = False
    report_urls = False

    if has_referrers:
        for referrer in referrers:
            if referrer['positives'] > 20:
                report_referrers = True
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
    else:
        print("Files referring not found!!!")

    if has_downloaded:
        for downloaded in downloadeds:
            if downloaded['positives'] > 3:
                report_downloaded = True
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
    else:
        print("Downloaded files not found!!!")

    if has_urls:
        for url in urls:
            if url['positives'] > 3:
                report_urls = True
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
    else:
        print("URL not found!!!")

    if report_referrers == False and report_downloaded == False and report_urls == False:
        report['detect'] = False
        return report
    report['detect'] = True
    report['report_referrers'] = report_referrers
    report['report_downloaded'] = report_downloaded
    report['report_urls'] = report_urls

    if report_referrers:
        report['referrer'] = data_referrer
    if report_downloaded:
        report['downloaded'] = data_downloaded
    if report_urls:
        report['url'] = data_url
    return report

def save_report(report, count):
    with open(str(count)+'.json', 'w') as w_f:
        json.dump(report, w_f)
        print("Report "+str(count)+" successfullly saved...")

if __name__ == "__main__":
    count = 0
    for line in open("test.txt"):
        if line.endswith('\n'):
            line=line[:-1]
        print(line)
        count += 1
        report = get_virustotal(line)
        save_report(report, count)
