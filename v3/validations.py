#This feature helps us verify whether the user has entered the correct product number.
def validationProductName(nameProduct):
    if nameProduct.isalpha():
        return False
    else:
        print("")
        print("Error: the name of the product cant empty, ni numerico")
        return True
     

#This feature helps us validate the numbers entered by the user.
def validationNum(num):
    if num > 0:
        return False

    else:
        print("")
        print("Error: the price to product is only positive")