class A:
    var1="welcome A"
class B:
    vae2="welcome B"
class C(A,B):
    var3="welcome C"

c1=C()
print(c1.var3)
print(c1.vae2)
print(c1.var1)
