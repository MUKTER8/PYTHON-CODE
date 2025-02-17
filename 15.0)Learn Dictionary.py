#Learn Dictionary in Python, how to create, add, remove, update, delete, iterate, sort and copy a dictionary in Python.
# A dictionary is a collection which is unordered, changeable and indexed. 
# In Python dictionaries are written with curly brackets, and they have keys and values.
# Dictionaries are used to store data values in key:value pairs.
info={"name":"John",
      "subject":["Math", "Science", "English"],
      "age":30,
      "city":"New York"}

null_dictionary={} #empty dictionary
print(null_dictionary)
null_dictionary["name"]="Mukter"
print(null_dictionary)

print(info)
print(info["name"])
info["age"]=35
info["city"]="Chicago"
print(info)