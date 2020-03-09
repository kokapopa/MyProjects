def f(a,n):
    if n==1: return a
    elif n==0: return 0
    if n%2==0:
        return a**n//2*a**n//2
    else: return a*a**(n-1//2)*a**(n-1//2)

m=input()
m=m.split(" ")
print(f((int(m[0])), int(m[1])))
