import random



def generator(input):
    if input == symbol:
        list = ['!', '@', "#", "$", "%", "?",]
        ran = int((random.randrange(0, 6)))
    
    if input == lower:
        list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
    return (list[ran])


def genlower():
    list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ran = int((random.randrange(0,22)))
    return (list[ran])

