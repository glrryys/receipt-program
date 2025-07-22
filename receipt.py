
def main():
    #main() is just creating a function
    item = input("Enter item: ").strip().title()  #strip means removes any extra spaces at the 
    # beginning or end (like if you typed " apple pie "
    # title means makes the first letter of each word uppercase 
    # (so "apple pie" becomes "Apple Pie"

    # both strings are built in


       
    # float converts what the user types (which is a text string) into a \
    # number with decimals so the program can do math with it.
    price = float(input("Enter price: $"))  # e.g. "1.99" -> 1.99
    
    # int converts the answer into a whole number 
    # so it can be used in math
    quantity = int(input("Enter quantity: "))  # e.g. "3" -> 3
    
    # calculate total cost (price × quantity)
    total = price * quantity  # e.g. 1.99 × 3 = 5.97
    
    # f = lets you create a string (a block of text) that can 
    #  include variables or values inside it.

    #f"..." = single string lines
    # however with /n you can make it look like multi line strings
    #f""..."" = multi line strings

    #which means you can write like this 
    # """This is line 1
    #This is line 2
    #This is line 3"""

    receipt = f"""  
        --------- RECEIPT ---------
        Item:      {item:>10}       
        Price:     ${price:>9.2f}   
        Quantity:  {quantity:>10}  
        ---------------------------
        Total:     ${total:>9.2f}   
        ---------------------------
    """
    
    # print the format receipt
    print(receipt)  

# only execute this part if the file is being run directly
# can be done the normal way but just trying to build the habit
# best for creating functions to be able to use
if __name__ == "__main__":
    main()  
    
