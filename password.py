#password class
import randchars as rs
import random
from multipledispatch import dispatch

class Password:
    @dispatch(int)
    def __init__(self, char_amt):
        self.pw = ''
        for i in range (char_amt):
            a = (int(random.randrange(0,4)))
            if a == 0:
                self.pw += rs.generator('symbol')
            if a == 1:
                self.pw += rs.generator('lower')
            if a == 2:
                self.pw += rs.generator('upper')
            if a == 3:
                self.pw += rs.generator('number')

    @dispatch(int,int,int,int)
    def __init__(self, symbol, upper, lower, numbers):
        my_string = ''
        for i in range(symbol):
            my_string += rs.generator('symbol')
        for i in range(upper):
            my_string += rs.generator('upper')
        for i in range(lower):
            my_string += rs.generator('lower')
        for i in range(numbers):
            my_string += rs.generator('number')
        self.pw = ''.join(sorted(my_string, key=lambda x: random.random())) 


    def setUser(self, username):
        self.user = username

    def savePass(self, key):
        with open("myfile.txt", 'a') as f:
            f.write(f"{key} {self.user} {self.pw}\n")
        print('saved')



    def __str__(self):
        return f"{self.pw}"


def loadPass(key):
    out = f"No login for site {key}"
    passwords = {}
    with open("myfile.txt", 'r') as f:
        for k in f:
            i = k.split(' ')
            passwords[i[0]] = [i[1], i[2]]
    for i in passwords:
        if i == key:
            out = f"Username and Password for {key} are : {passwords[i][0]} and {passwords[i][1]}"
    print(out)

def allPass():
    passwords = {}
    with open("myfile.txt", 'r') as f:
        for k in f:
            i = k.split(' ')
            passwords[i[0]] = [i[1], i[2]]
    for i in passwords:
        print(i)