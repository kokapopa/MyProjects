a=input()
b=input()
print(b.split(" ")[(len(a.split(" "))%len(b.split(" ")))-1])