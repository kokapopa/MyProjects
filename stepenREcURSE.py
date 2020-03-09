def f(a,n):
    if n==1: return a
    elif n==0: return 0
    if n%2==0:
        return power(a,n//2)**2
    else: return a*power(a,n-1)

m=input()
m=m.split(" ")
print(f((int(m[0])), int(m[1])))
