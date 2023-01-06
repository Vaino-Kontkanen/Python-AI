#Make function bubble_sort using bubble sort algorithm to 
#sort numbers given by user; order numbers into the ascending order.
#Bubble Sort is the simplest sorting algorithm that works by 
#repeatedly swapping the adjacent elements if they are in wrong order. 
#https://en.wikipedia.org/wiki/Bubble_sort

def bubble_sort(list):
    n = len(list)
    for i in range(n-1):
        flag=0
        for j in range(n-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                flag = 1
        if flag == 0:
            break
        return list
a = []
number = int(input("Please Enter the Total Number of Elements : "))
for i in range(number):
    value = int(input("Please enter the %d Element : " %i))
    a.append(value)
print("The Sorted List in Ascending Order : ", bubble_sort(a))