import os
import sys
import json

def overview(name,statistic):
    f=open("module1.json","r")
    url=name
    f1_dict=json.load(f)
    hostname=f1_dict['hostnames']
    ip=f1_dict['ip_str']
    country=f1_dict['country_name']
    organization=f1_dict['org']
    isp=f1_dict['isp']
    ports=f1_dict['ports']

    services = None
    vulns = None
    if 'data' in f1_dict:
        datas = f1_dict['data']
        for data in datas:
            if 'http' in data:
                if 'components' in data['http']:
                    services = data['http']['components']
            if "opts" in data:
                if "vulns" in data['opts']:
                    vulns = data['opts']['vulns']
    f.close()

    f=open("module2.json","r")
    f2_dict=json.load(f)
    data_google=f2_dict['googleSafeBrowsing']
    commonNames = f2_dict['sslLabs']['certs'][0]['commonNames']
    keyAlg=f2_dict['sslLabs']['certs'][0]['keyAlg']
    keyStrength=f2_dict['sslLabs']['certs'][0]['keyStrength']
    notBefore=f2_dict['sslLabs']['certs'][0]['notBefore']
    notAfter=f2_dict['sslLabs']['certs'][0]['notAfter']
    issuerInfo=f2_dict['sslLabs']['certs'][0]['issuerSubject']
    sslGrade=f2_dict['sslLabs']['endpoints'][0]['grade']
    hasWarnings=f2_dict['sslLabs']['endpoints'][0]['hasWarnings']
    with open("overview.json", "w+") as write_file:
        json.dump({'data':{'statistic':statistic, 'url':name,'hostname':hostname,'ip':ip,'country':country,'organization':organization,'isp':isp,'ports':ports,'services':services,'vulns':vulns,'googleSafeBrowsing': data_google,'commonNames':commonNames,'keyAlg':keyAlg,'keyStrength':keyStrength,'notBefore':notBefore,'notAfter':notAfter,'issuerInfo':issuerInfo, 'sslGrade':sslGrade,'sslWarning':hasWarnings}}, write_file)

        #services = f1_dict['data'][1][]



if __name__ == "__main__":
    filepath = sys.argv[1]
    mainpath=os.getcwd()+"/log"
    f = open(filepath, "r")
    line = f.readline()
    while line:
        line = line.strip("\n ' '")
        name=line.split('=')[0]
        line=line.split('}')[0]     
        statistic=line.split('{')[-1]
        print(mainpath+'/'+name)
        os.chdir(mainpath+'/'+name)
        overview(name,statistic)
        #exit(0)
        os.chdir(mainpath)
        line=f.readline()
    f.close()
