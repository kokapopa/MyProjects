def Xor(a,b):
 if a==b: return 0
 else: return 1

m=input()
m=m.split(" ")
print (Xor(int(m[0]), int(m[1])))