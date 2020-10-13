"""
このファイルに解答コードを書いてください
"""

import re
import sys

def main():

    a_dict = {}

    if len(sys.argv) != 2:
        print("Usage: test.py filename")
        
    f = open(sys.argv[1], "r")

    for line in f:
        n_line = line.rstrip('\n')
        n_line = n_line.split(":")
        if len(n_line) == 2:
            num = n_line[0]
            word = n_line[1]
            a_dict[num] = word
        else:
            line = line.rstrip('\n')
            inp = line
            break

    ans = ""
    for i in sorted(a_dict):
        ans = ans + fizzbuzz(int (inp), int (i), a_dict[i])

    if "" == ans:
        print(inp)

    else:  
        print(ans)
        
def fizzbuzz(inp, num, word):

    if inp % num == 0:
        return word

    return ""

main()
    
        
