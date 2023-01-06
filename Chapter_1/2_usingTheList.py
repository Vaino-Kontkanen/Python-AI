#In the second exercise the idea is to create a small grocery shopping list with the list datastructure. 
#In short, create a program that allows the user to (1) add products to the list, (2) remove items and 
#(3) print the list and quit.

#If the user adds something to the list, the program asks "What will be added?: " 
#and saves it as the last item in the list. If the user decides to remove something, 
#the program informs the user about how many items there are on the list 
#(There are [number] items in the list.") and prompts the user for the removed item ("Which item is deleted?: "). 
#If the user selects 0, the first item is removed. When the user quits, 
#the final list is printed for the user "The following items remain in the list:" 
#followed by the remaining items one per line. If the user selects anything outside the options, 
#including when deleting items, the program responds "Incorrect selection.".

def main():
	MyList =[]
	
	while True:
		choice = input("Would you like to \n(1)Add or \n(2)Remove items or \n(3)Quit?: ")
		if choice =="1":
			AddItem(MyList)
		elif choice =="2":
			RemoveItem(MyList)
		elif choice =="3":
			PrintList(MyList)
			break
		else:
			print("Incorrect selection.")
def AddItem(list):
	itemAdded = input("What will be added?: ")
	list.append(itemAdded)
def RemoveItem(list):
	print("There are", len(list), "items in the list.")
	itemRemovedIndex = input("Which item is deleted?: ")
	if int(itemRemovedIndex) >= len(list) or int(itemRemovedIndex) < 0:
		print("Incorrect selection.")
	else: list.remove(list[int(itemRemovedIndex)])
def PrintList(list):
	print("The following items remain in the list:")
	[print(item) for item in list]
if __name__ == "__main__":
	main()