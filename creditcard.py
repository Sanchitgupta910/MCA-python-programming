"""
    @AUTHOR: SANCHIT GUPTA
    DATE: 10/9/21
    PROBLEM: Create a module named “OMG” with the functions “ValidateCreditCard” and “ALLISWELL” in it. Call these functions into
        another python script by importing the module “OMG”.
"""

import omg
isvalid = omg.ValidateCreditCard() #isvalid is a boolean variable
print("VALIDITY: ", isvalid)

omg.ALLISWELL(isvalid)

