# main.py
# imports...
import sys
import re
from collections import defaultdict

def check_input():
    if len(sys.argv) <= 1:
        print("Error: no File given. Usage: [filename].py [importfile].txt")
        sys.exit()
    elif not sys.argv[1].endswith('.txt'):
        print("Error: wrong file format of input file. Usage: [filename].py [importfile].txt")
        sys.exit()

def read_import_file():
    knots = {}
    keys_of_knots = []
    links = defaultdict(dict)
    i = 0
    with open(sys.argv[1], 'r') as f:
        for line in f:
            if re.search("[a-z|A-Z] = [0-9];", line): #found Node
                knots[line[4]] = int(line[8])
                keysOfKnots = keysOfKnots + [line[4]]
                print(knots)
            elif re.search("[a-z|A-Z] - [a-z|A-Z] : [0-9]{1,3};", line):   #found link
                number = line[12:len(line)-2]
                links[line[4]][line[8]] = number
                print(links)
        print(knots[keysOfKnots[1]])


def main():
    #print(sys.argv)
    check_input()
    read_import_file()


if __name__ == "__main__":
    main()





