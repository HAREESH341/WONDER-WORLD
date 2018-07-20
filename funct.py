# def addn(a,b):
# 	res=a+b
# 	return res
# a = addn(100,20)
# print(a)

# def avgn(a,b,c):
	# print("a",a,"b",b,"c",c)
	# avg=(a+b+c)//3
	# print(avg)
# avgn(12,50.534,9.987)

# def makeCake(fla = "vannila", wei = "2" , sha = "vowel"):
# 	print(" you have ordered "+fla + " flavoured cake of "+wei+ " kgs and "+sha+" shape")
# makeCake(fla = "vannila" , wei = "2" , sha = "round")
# makeCake(fla = "chocolate" , wei = "1.5" , sha = "rectangle")
# makeCake(fla = "pineapple" , wei = "3")
# makeCake(wei = "5")
# makeCake()

def Vavgn(*args):
	print(*args)
	sum = 0
	for i in args:
		sum = sum + i
	print(sum)
	avg = sum / len(args)
	print(avg)

Vavgn(10)
Vavgn(10,20)
Vavgn(10,20,30)
Vavgn(10,20,30,40)








