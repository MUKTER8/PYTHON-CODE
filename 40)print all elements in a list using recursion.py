def display(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    display(list,idx+1)

ch=["a","b","c","d"]
print(display(ch))