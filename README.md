# 6262 
## Setup
Download and install python 3.7
```
sudo apt install python3.7 
```


### Install dependencies
Install git
```
sudo apt install git
```

Install pip
```
sudo apt install python3-pip
```

Install requests
```
python3 -m pip install requests
```

Install shodan
```
pip3 install shodan
```

Download source files
You either get source files from unziping the gz file or download from our GitHub repo.
https://github.com/FunctionRorscharch/6262.git

If you get the source files from the gz file, you need to download the ranking data from our GitHub repo. Copy the entire data dir to your work dir. 
https://github.com/FunctionRorscharch/6262.git/data

## How to use
### DCG algorithm
The source file dcg_1.py and dcg_2.py are the modules of DCG algorith to process ranking data.
It will generate a res.txt which contains all the url selected by DCG algorithm.
```
python3 dcg_1.py
```

This will process res.txt to another step and return a rankres.txt with all the information needed for the following process.
```
python3 dcg_2.py
```
### Crawling selected urls
Start crawling. This is the main crawler, and it will generate a log directory which contains the analysis results of every url. Three .json files will appear under the dir of each url.
```
python3 crawler.py rankres.txt
```
Run filter function to extract useful information for the final report. 
```
python3 filter.py rankres.txt
```
After this script finished, there should be a data.json in the log/sample_url dir. You can copy data.json to /frontend/test, and you can open index.html in your browser to see the final results.  
