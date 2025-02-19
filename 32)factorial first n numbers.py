n=int(input("Enter the value of n : "))
i=1
fact=1
while i<=n:
    fact=fact*i
    i=i+1
print("Factorial :",fact)

fact1=1
for el in range(1,n+1):
        fact1=el*fact1
print("Factorial :",fact1)