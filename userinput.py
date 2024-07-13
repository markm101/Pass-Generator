import password as pw


def beginning():
    while True:
        x = input('create pass (1), get pass (2), display all stored logins (3)  ')
        if x == '1':
            login = 0
            char_select = input('Select number of characters(1) or individualize(2)?  ')
            if char_select == '1':
                num = int(input("Number of characters in password: "))
                login = pw.Password(num)
            elif char_select == '2':
                symbol = int(input("Number of symbols: "))
                upper = int(input("Number of Uppercase Letters: "))
                lower = int(input("Number of lowercase letters: "))
                numbers = int(input("Number of numbers: "))
                login = pw.Password(symbol, upper, lower, numbers)


            print(f"{str(login)} has been registered")

            key = input('What site is the password for (no spaces)?   ')
            user = input('What is the desired username?  ')

            login.setUser(user)
            login.savePass(key)
            print(f'Your password for {key} has been saved in the data base')
            continue

        elif x == '2':
            key = input('Which login do you need?  ')
            pw.loadPass(key)
            continue

        elif x == '3':
            pw.allPass()
            continue



