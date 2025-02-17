"""Learn List Methods in Python
List Methods is a collection of built-in methods that can be used to perform various operations on lists in Python.
List is a collection of items. It is one of the most commonly used data types in Python. Lists are mutable, which means that you can change the values of the elements in a list. 
Advantages of using lists:
1. Lists are mutable, 2. Lists are ordered, 3. Lists are versatile, 4. Lists are dynamic, 
5. Lists are easy to use, 6. Lists are flexible, 7. Lists are efficient, 8. Lists are powerful, 
9. Lists are versatile, 10. Lists are easy to understand."""
#syntax: list_name.method_name()
#Example: list.append(), list.clear(), list.copy(), list.count(), list.extend(), list.index(), list.insert(), list.pop(), list.remove(), list.reverse(), list.sort()
list1=[1,4,3,7,9,6,2,8,5,10]
list2=[11,12,13,14,15,16,17,18,19,20]


#append() method adds an element at the end of the list.
list1.append(11) #add 11 at the end of the list
print(list1) #print list1


#sort() method sorts the list in ascending order.
list1.sort() #sort list1 in ascending order
print(list1) #print list1

#Descending order
list1.sort(reverse=True) #sort list1 in descending order
print(list1) #print list1

#reverse() method reverses the order of the list.
list2.reverse() #reverse the order of list1
print(list2) #print list2

#insert() method inserts an element at the specified position.
list2.insert(2,21) #insert 21 at index 2
print(list2) #print list2

#remove() method removes the first occurrence of the specified element.
list2.remove(21) #remove 21 from the list
print(list2) #print list2


#pop() method removes the element at the specified position.
list2.pop(2) #remove element at index 2
print(list2) #print list2


#clear() method removes all the elements from the list.
list2.clear() #remove all elements from the list
print(list2) #print list2