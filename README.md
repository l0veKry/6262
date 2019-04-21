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
python3 dcg_1.py
python3 dcg_2.py

