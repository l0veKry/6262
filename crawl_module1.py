import sys
import shodan
import json
import socket
import time

SHODAN_API_KEY = "giRyAvmoU95GbT9Brqw9JQ1IwmPl2M6o"

api = shodan.Shodan(SHODAN_API_KEY)

host = api.host('91.223.182.33')

# Print general info
#print(host)
#print(json.dumps(host))

def mainfunc(url):
    res=search_shodan(url)
    with open("module1.json", "w+") as write_file:
        json.dump(res, write_file)

def search_shodan(url):
	if url.endswith('\n'):
		url=url[:-1]
	try:
		print("Start shodan scanning: ")
		print(url)
		ipaddr = socket.gethostbyname(url)
		host = api.host(ipaddr)
#		print(json.dumps(host))
		return host
	except:
		print("An exception occurred")

if __name__ == "__main__":
	with open('test.txt', 'r') as f:
		for line in f:
			time.sleep(1)
			if line.endswith('\n'):
				line=line[:-1]
			f2 = open(line, 'w')
			res = search_shodan(line) 
			json.dump(res, f2)
