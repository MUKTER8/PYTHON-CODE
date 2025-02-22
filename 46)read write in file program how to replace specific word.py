with open("practice.txt", "r") as f:
    data = f.read()

update = data.replace("python", "Java")
print(update)

with open("practice.txt","w") as f:
    f.write(update)