"""
#method =1
with open("numbers.txt","r") as f:
    data=f.read()
    
    num=""
    for i in range(len(data)):
        if(data[i]==","):
            print(int(num))
            num=""
        else:
            num+=data[i]
"""
#method=2
count=0
with open("numbers.txt","r") as f:
    data=f.read()
    print(data)
    
    num=data.split(",")
    for val in num:
        if (int(val)%2==0):
            count+=1
print(count)