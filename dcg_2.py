import sys
import os
def rank(res, output_file):
    with open(res, 'r') as f:
        lines = f.readlines()

    output = ''
    s1 = "./data/"
    s2 = "/top-1m.csv"
    s3 = "={"
    s4 = "}"

    for line in lines:
        # split or not
        tokens = line.strip().split(',')

        temp = ''
        for i in range(1,16):
            si=str(i)
            path=s1+si+s2

            with open(path,'r') as fc:
                fclines = fc.readlines()

            for fcline in fclines:
                fctokens = fcline.strip().split(',')
                if fctokens[1] == tokens[1]:
                    if not i == 1:
                        temp = temp + ',' + fctokens[0]
                    else:
                        temp = temp + fctokens[0]
        output = output + tokens[1] + s3 + temp + s4 +'\n'

    with open(output_file, 'w') as f:
        f.write(output)


if __name__ == "__main__":
    res="./res.txt"
    output_file = "./rankres.txt"
