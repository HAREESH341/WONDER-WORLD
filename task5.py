a= int(input("enter a:"))
b= int(input("enter b:"))
c= int(input("enter c:"))
if(a<b and b<c):
	print("c is largest")
elif(b<c and c<a):
	print("a is larger")
elif(c<a and a<b):
	print("b is larger")
else:
	print("all are equal")
