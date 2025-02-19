#Set question practice,
"""Q_1:
Store following word meaning in a python dictionary:
table:"a piece of furniture.","list of fact & figures."
cat:"a domesticated carnivorous mammal with soft fur."
Q_2:
you are given a list of subjects for students.Assume one classroom is required for one subject.How many classrooms are needed by the students?
subject:"Java","Python","C++","C","C#","SQL","HTML","CSS","JavaScript","PHP","Java","Python","C++","C#","C#","SQL","HTML","CSS","JavaScript","PHP"

"""

#Solve Q_1:
dictionary={
    "table":["a piece of furniture.","list of fact & figures."],
    "cat":"a domesticated carnivorous mammal with soft fur."
}
print("Solution 1:",dictionary)

#Solve Q_2:
subject={"Java","Python","C++","C","C#","SQL","HTML","CSS","JavaScript","PHP","Java","Python","C++","C#","C#","SQL","HTML","CSS","JavaScript","PHP"}
print("Solution 2:",subject)
print("Number of classrooms needed:",len(subject))


"""
Q_3:
write a program to enter marks of 3 subjects from the user and store them in a dictionary.Start with an empty dictionary & add one by one.
Use the subject name as a key and marks as values.
"""
#Solve Q_3:
marks={}
x=int(input("Enter marks of math:"))
marks.update({"math": x})

x=int(input("Enter marks of science:"))
marks.update({"science": x})

x=int(input("Enter marks of english:"))
marks.update({"english": x})

print("Solution 3:",marks)

"""Q_4:
Figure out a way to store 9 & 9.0 as separate elements in a set.
(You can take help of built-in data types)
"""
#Solve Q_4:
values={
    ("int",9),
    ("float",9.0)
}
print("Solution 4:",values)