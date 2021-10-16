def check_cash(user_cash):
    money_bank = 0

    for cash in user_cash:
        if cash == 25:                                #if cash == 25 directly add it into money bank
            money_bank += 25
        elif cash > 25:
            if money_bank >= (cash - 25):             # checks whether if money_bank has enough cash to give change else returns "False"
                money_bank -= cash-25
            else:
                print("Available Cash = ", money_bank)
                print("Required Cash =", cash-25)
                return "False"

    print("Cash left = ", money_bank)
    return "True"

if __name__ == '__main__':
    user_cash = []
    numPersons = int(input("Enter Number of persons : "))
    print("Enter cash: ")
    while numPersons != 0:
        user_cash.append(int(input()))                        # appends every values into 'user_cash' as integers
        numPersons -= 1

    print(check_cash(user_cash))
    
print("xyyzxyzxzxyy".count('xyy', 2, 11))
