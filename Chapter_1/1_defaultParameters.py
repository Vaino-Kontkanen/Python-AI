#This exercise tests out the default values of parameters. 
#Create a program which has a main function and a subfunction called tester. 
#The main function prompts user for an input "Write something (quit ends): " and sends this input to the subfunction as a parameter.

#Define the subfunction tester so that it has one parameter called "givenstring", 
#which has the default value "Too short". If the user input is less than 10 characters, 
#the program uses the default value and if 10 or more, it prints the usergiven input. 
#If the user inputs "quit", the program is terminated. 

def main():
    while True:
        a = input("Write something (quit ends): ")
        if a == "quit":
            break
        else:
            tester(a)
def tester(str, givenstring="Too Short"):
    if len(givenstring) > len(str):
        print(givenstring)
    else:
        print(str)
if __name__ == "__main__":
    main()