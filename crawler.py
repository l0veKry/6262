import os
import sys
import csv
import crawl_module1
import crawl_module2
import crawl_module3
import shutil

#make new directory 
def mkdir(name):
    folder = os.path.exists(name)
    if folder:
        shutil.rmtree(name)
    os.mkdir(name)

#starts crawlers function
def start(targeturl):
    mkdir(targeturl)
    path=os.getcwd()
    os.chdir(path+"/"+targeturl)
    crawl_module1.mainfunc(targeturl)
    crawl_module2.mainfunc(targeturl)
    crawl_module3.mainfunc(targeturl)
    os.chdir(path)
    
#main function, reads each line from .txt file and kicks off crawlers
if __name__ == "__main__":
    filepath = sys.argv[1]
    f = open(filepath, "r")
    line = f.readline()
    mainpath=os.getcwd()
    mkdir("log")
    os.chdir(mainpath+"/log")
    while line:
        print ("#starts analyze  :"+line)
        line=line.split('=')[0]
        start(line)            
        print("-------------------------------------------------")
        line = f.readline()
    f.close()





