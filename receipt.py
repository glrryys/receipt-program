"""
Shop Receipt Program
Author: Glerys Gonzalez 
Date: 7/20/25
Description: This program takes user input for an item, its price and quantity,
then generates a receipt with proper currency formatting.
"""

def main():
    # get and clean user input for item name
    # .strip() removes leading/trailing spaces, .title() capitalizes each word
    item = input("Enter item: ").strip().title()  # e.g. "  apple pie  " -> "Apple Pie"
    
    # get price and convert to float for decimal support
    # float() converts the input string to a floating-point number
    price = float(input("Enter price: $"))  # e.g. "1.99" -> 1.99
    
    # get quantity and convert to integer
    # int() converts the input string to a whole number
    quantity = int(input("Enter quantity: "))  # e.g. "3" -> 3
    
    # calculate total cost (price × quantity)
    total = price * quantity  # e.g. 1.99 × 3 = 5.97
    
    # create formatted receipt using f-string
    # f-strings allow embedding expressions inside string literals
    receipt = f"""  
        --------- RECEIPT ---------
        Item:      {item:>10}       
        Price:     ${price:>9.2f}   
        Quantity:  {quantity:>10}  
        ---------------------------
        Total:     ${total:>9.2f}   
        ---------------------------
    """
    
    # print the fully formatted receipt
    print(receipt)  

# standard Python idiom to check if this file is being run directly
# (as opposed to being imported as a module)
if __name__ == "__main__":
    main()  # Execute the main function
    