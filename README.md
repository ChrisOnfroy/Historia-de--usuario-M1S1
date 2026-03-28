# User Story M1S3

This program is a new version because it includes CSV file management for data persistence

## What does the program do?

- The program adds products to the inventory along with their price and quantity.
- Validates that the name is not empty or numeric, and that price and quantity are positive numbers.
- Show products of the inventory if was added
- Calculate the total value of the inventory and the total units in stock
- Find the most expensive product and the product with highest stock
- Search for specific products by name
- Update existing product information
- Delete products with confirmation
- Save inventory to a CSV file automatically
- Load inventory from a CSV file

## Example usage

When you run the program, you'll see messages like:

### MENU
```text
            Please enter a digit number (1-9) :
            1. Create product
            2. Show Inventory
            3. Search Product
            4. Update Product
            5. Delete Product
            6. Statistics
            7. Upload CSV
            8. Charge CSV
            9. Exit
            Enter →
```
### ADD PRODUCT
```text
            Enter the name product: cocacola

            Enter the price of the product: 2000

            Enter the quantity: 3

            Product 'cocacola' added successfully!
```
### SHOW INVENTORY
```text
            ==================================================
            INVENTORY LIST
            ==================================================
            Product: cocacola | Price: $2000.00 | Quantity: 3
            Product: pepsi | Price: $1800.00 | Quantity: 5
```

### SEARCH PRODUCT
```text
            Enter name product: cocacola

            Product found:
              Name: cocacola
              Price: $2000.00
              Quantity: 3 units
```
### UPDATE PRODUCT
```text
            Enter name product: cocacola

            Current product: cocacola - $2000.0 - 3 units
            Write new name: cocacola zero
            Write new price: 2200
            Write new quantity: 10

            Product updated successfully!
```
### DELETE PRODUCT
```text
            Enter name product to delete: pepsi

            Product found: pepsi | Price: $1800.00 | Quantity: 5
            Are you sure you want to delete this product? (y/n): y

            Product 'pepsi' has been deleted successfully!
```
### CALCULATE STATISTICS
```text
            ==================================================
            INVENTORY STATISTICS
            ==================================================

             TOTAL UNITS: 13 units
             TOTAL VALUE: $22000.0

             MOST EXPENSIVE PRODUCT:
                • Name: cocacola zero
                • Price: $2200.0

             HIGHEST STOCK PRODUCT:
                • Name: cocacola zero
                • Quantity: 10 units
```
### UPLOAD CSV (SAVE)
```text
            Inventory saved successfully to 'v3/data/inventory.csv'
CHARGE CSV (LOAD)
text
            File loaded successfully. 2 products loaded.
Project Structure
text
            inventory-system/
            │
            ├── main.py                 # Main menu
            ├── services.py             # Core functions
            ├── validations.py          # Validations
            ├── archives.py             # CSV operations
            └── v3/
                └── data/
                    └── inventory.csv   # Data file
```
### What's new in M1S3?
• CSV file persistence (save and load)

• Search product functionality

• Update product functionality

• Delete product with confirmation

• Enhanced statistics (most expensive, highest stock)

• Improved menu with 9 options

• Better error handling

• Modular code structure



# User Story M1S2

This program is a new version beacuse content options for the user

## What does the program do?

- The program adds products to the inventory along with their price and quantity.
- Validates that the name is not empty or numeric, and that price and quantity are positive numbers.
- show products of the inventory if was added 
- calculte the total of the invetory and the total products in the inventory
- The user decides to exit the program by selecting the last option

## Example usage

When you run the program, you'll see messages like:


### MENU
```text
            Please enter a digit number (1-4) :
            1. Add product
            2. Show producto
            3. Calculate Estadistics
            4. Exit
            Enter →  
```
### ADD PRODUCT
```text
            Enter the name product: cocacola

            Enter the price of the product: 2000

            Enter the quantity: 3
```
### SHOW PRODUCTS
```text
            Product: cocacola | Price: 2000.0 | Quantity: 3
```

### Calculate Statistics
```text
            The total values is: 6000.0
            the Quantity total the produtcs is: 1
```






# User Story M1S1

This program is a simple inventory application written in Python.

## What does the program do?

- Prompts the user for a product name, price, and quantity.
- Validates that the name is not empty or numeric, and that price and quantity are positive numbers.
- Calculates the total cost of the product by multiplying price and quantity.
- Displays the entered data and the total cost on the screen.

## Example usage

When you run the program, you'll see messages like:

```text
welcome to the app!!
Enter the name product: (for example) Apples
Enter the price of the product: 10.5
Enter the quantity: 3

Product: Apples
Price: 10.5
Quantity: 3
Total cost: 31.5
```

## Requirements

- Python 3.8 or higher

## How to run

Open a terminal in the project folder and run:

```bash
python3 inventory.py
```
