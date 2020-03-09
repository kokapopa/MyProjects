def f(a):
    i=2
    while i*i<=a:
        if a%i==0:
            return False
        i+=1
    return True

n=int(input())
if f(n):
    print("prime")
else: print("composite")