#password class
import randchars as rs
import random
import string


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
       
        
    def __str__(self):
        return f"{self.pw}"
