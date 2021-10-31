"""
    @AUTHOR: SANCHIT GUPTA
    DATE: 10/9/21
    PROBLEM: Create a module named “OMG” with the functions “ValidateCreditCard” and “ALLISWELL” in it. Call these functions into
        another python script by importing the module “OMG”.
"""

def ValidateCreditCard():
    ccnumber = list(input("Please enter a card number: ").strip())
    if len(ccnumber) <= 13 and len(ccnumber) >= 19:
        return False

    # Remove the last digit from the card number
    check_digit = int(ccnumber.pop())
# Reverse the order of the remaining numbers
    ccnumber.reverse()
    processed_digits = []
    doubled_digit = 0
#index is used for the current iteration digit is used for the item at the current iteration"""
    for index, digit in enumerate(ccnumber):
        if index % 2 == 0:
            doubled_digit = int(digit) * 2
            
            if doubled_digit > 9:
                doubled_digit = int(doubled_digit / 10) + doubled_digit % 10
                processed_digits.append(doubled_digit)
               
            else:
                processed_digits.append(doubled_digit)
        else:
            processed_digits.append(int(digit))
    total = sum(processed_digits)
    
    last_digit = total % 10
    
#Subtract the last digit from the sum obtained in “d” from 10
    final_digit = 10 - last_digit
    
# checking if last digit of credit card number is same as digit obtained after subtraction
    if check_digit == final_digit:
        return True
    return False


def ALLISWELL(isvalid):
    if isvalid:
        print("ALL IS WELL")
    else:
        print("ALL IS WELL")
        print("ALL IS WELL")
