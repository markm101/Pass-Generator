import randchars as rs
import string




#main
def main():
    #mini = int(input('minimum number of characters? : '))
    #characters = int(input('maximum number of characters? : '))
    #symbols = input('Include symbols (!@#$%^?) (Y/N) : ')

    #generator test (ignore)
    while True:
        a = rs.generator('number')
        if a == '0':
            print(a)
            print ('done')
            break
        else:
            print(a)






if __name__ == "__main__": 
    main()