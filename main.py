print("welcome to the app!!")

# calculate quantity and prince for the total of the product
def calculationTotalProduct (quantity, price ):
    result = quantity * price
    return result


# request user data
nameProduct = input("Enter the name product: ").strip()
price = float(input("Enter the price of the product: "))
quantity = int(input("Enter the quantity: "))


# show data
print(f"""
Product: {nameProduct}
Price: {price}
Quantity: {quantity}
Total cost: {calculationTotalProduct(quantity, price)}""")