import randchars as rs
import password as pw


#main
def main():
    #mini = int(input('minimum number of characters? : '))
    #characters = int(input('maximum number of characters? : '))
    #symbols = input('Include symbols (!@#$%^?) (Y/N) : ')
    # Define a Python object to pickle
    s = pw.Password(3, 5, 2, 4)
    print(s)
    print(len(str(s)))




if __name__ == "__main__": 
    main()