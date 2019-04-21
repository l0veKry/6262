import sys

keywords = [
    "virus",
    "flash",
    "security",
    "fraud"
]
whitelist = [
    "cdn",
    "microsoft",
    "google",
    "apple",
    "amazon",
    "baidu"
]

def whlist(current_alexa):
    lines = []
    with open(current_alexa, 'r') as f:
        lines = f.readlines()
    for line in lines:
        tokens = line.strip().split(',')
        print(tokens[0])
        if tokens[0] == '50':
            return
        else:
            part = tokens[1].split('.')
            whitelist.append(part[1])
            #print(len(whitelist))
            
def dcg(prev_alexa,current_alexa):
    return
def get_sites(current_alexa, output_file):
    lines = []
    setfilter = set()
    with open(current_alexa, 'r') as f:
        lines = f.readlines()

    
    
    output = ''
    for line in lines:
        tokens = line.strip().split(',')
        for word in keywords:
            if word in tokens[1]:
                for wh in whitelist:
                    if wh in tokens[0] or wh in tokens[1]:
                        break
                    else:
                        part = tokens[1].split('.')
                        if len(part) == 1:
                            if part[0] in setfilter:
                                break
                        elif part[1] in setfilter or part[0] in setfilter:
                            break
                        else:
                            setfilter.add(part[1])
                            output = output + tokens[1] + '\n'
                            break

    with open(output_file, 'w') as f:
        f.write(output)

if __name__ == '__main__':
    print("currently detecting websites")

    current_alexa = "./data/1/top-1m.csv"
    output_file = "./res.txt"
    whlist(current_alexa)
    print(len(whitelist))
    get_sites(current_alexa, output_file)
