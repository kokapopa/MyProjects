def f(a):
    d=2
    while a%d != 0:
        d+=1
    if d==a: return "prime"
    else: return "composite"

m=input()
print (f(int(m)))