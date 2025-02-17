#Write a program to check if a list contains a palindrome oƒ elements.(Hint:use copy() method)
#Palindrome  is a word, phrase, number, or other sequence of characters that reads the same forward and backward.
list1=[1,2,3,4,5,4,3,2,1]
list2=[1,2,3,4,5,6,7,8,9]
copy_list1 = list1.copy()
copy_list1.reverse()
if list1 == copy_list1:
    print("Yes it is palindrome")
else:
    print("not a palindrome")

copy_list2=list2.copy()
copy_list2.reverse()
if list2 == copy_list2:
    print("Yes it is palindrome")
else:
    print("not a palindrome")
    