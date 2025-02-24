list=[1,7,3,4,5,6,7,8,9]
x=7
idx=0
for el in list:
    if(el==x):
        print("found at index:",idx)
        break
    idx +=1
    