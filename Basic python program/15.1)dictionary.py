"""learn nested dictionary in python, how to create a nested dictionary, access elements,
add elements, delete elements, update elements, and iterate through the nested dictionary in python.
Syntax: dictionary = {
key1: {keyA: valueA,keyB: valueB}, 
key2: {keyC: valueC, keyD: valueD}}
"""
student={
    "name":"John",
    "Subjects":{
        "Maths":90,
        "Physics":80,
        "Chemistry":70
    }
}

print("Output 1: ",student)
print("Output 2:" ,student["Subjects"])
print("Output 3: ",student["Subjects"]["Maths"])   

#type casting
print("Output 4: ",list(student.keys())) #return the keys of the dictionary
print("Output 5: ",list(student.values())) #return the values of the dictionary

#Dictionary Methods
#example: clear(), copy(), fromkeys(), get(), items(), keys(), pop(), popitem(), setdefault(), update(), values()
info1=student.keys() #return the keys of the dictionary
print("Output 6: ",info1)

info2=student.values() #return the values of the dictionary
print("Output 7: ",info2)

info3=student.items() #return the key-value pair of the dictionary
print("Output 8: ",info3)

print("Output 9: ",list(student.items()))

info4=student.get("name") #return the value of the key

print("Output 10: ",info4)

#update method in dictionary,Syntax: dictionary.update(key=value)
new_dict={"name":"Jonathan","age":20}
student.update(new_dict)
print("Output 11: ",student)