def f(a,n):
    if n==1: return a
    elif n==0: return 0
    if n%2==0:
        return f(a,n//2)**2
    else: return a*f(a,n-1)

m=input()
m=m.split(" ")
print(f((float(m[0])), int(m[1])))
