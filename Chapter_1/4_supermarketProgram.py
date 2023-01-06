#Make simple Supermarket -program,
#having 10 products with prices in a list as follows:
#[10,14,22,33,44,13,22,55,66,77].
#asking product number from 1 to 10 and summing its price 
#to totalsum and printing product number and price 
#for every product as in example.
#asking products until user gives '0' to quit the program (while-loop).
#printing  "Total:" and the total sum of prices.
#asking "Payment:" from user and printing "Change:" and 
#finally  calculating and printing the amount of change (payment - totalsum) to customer.
#You must use in this program: while, input
def main():
    prices = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]
    print("Supermarket\n===========")
    total = 0
    while True:
        choice = int(input("Please select product (1-10) 0 to Quit: "))
        if choice == 0:
            break
        else:
            print("Product: ", choice, " Price: ", prices[choice-1])
            total = total + prices[choice-1]
    print("Total: ", total)
    pay = int(input("Payment: "))
    print("Change: ", pay-total)
if __name__ == "__main__":
    main()