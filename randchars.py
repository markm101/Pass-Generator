import random
import string



def generator(input):
    if input == 'symbol':
        list = ('!@#$%^&*?')
        ran = int((random.randrange(0, 6)))
    if input == 'lower':
        list = string.ascii_lowercase
        ran = int((random.randrange(0, 26)))
    if input == 'upper':
        list = string.ascii_uppercase
        ran = (int(random.randrange(0,26)))
    if input == 'number':
        list = ('1234567890')
        ran = (int(random.randrange(0,10)))
        
    return (list[ran])


