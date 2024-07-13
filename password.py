#password class
import randchars as rs
import random
import pickle
import random


file = open('myfile.txt', 'a+')



class Password:
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



       
    def savePass(self, log, user):
        file.write(f"\n {log} :   {user}   {self.pw}")


    

    def __str__(self):
        return f"{self.pw}"
