#In this exercise create two functions
#my_split : which splits sentence given as 
#first argument using second argument as a 
#separator character to separate list items. 
#Function returns a list of items.
#my_join : which joins list given as first argument 
#to a string separated with character given as
#second argument. Function returns a string.
#In this exercise you are not allowed to use 
#Python split and join functions
def my_split(string, sep):
    list1 = []
    word = ''
    for c in string:
        if c not in sep:
            word += c
        elif word:
            list1.append(word)
            word = ''
    if word:
        list1.append(word)
    return list1
def my_join(lst, sep):
    str = ''
    for item in lst:
        str = str + item + sep
    str = str[:-1]
    return str
sentence = str(input("Please enter sentence: "))
print(my_join(my_split(sentence, ' '), ','))
print(my_join(my_split(sentence, ' '), '\n'))