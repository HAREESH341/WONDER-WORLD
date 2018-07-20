# fee=("10k","20k","30k","40k")
# # print(fee)
# # print(type(fee))
# fee=list(fee)
# print(fee)
# # print(type(fee))
# fee[1]="15k"
# print(fee)
# fee=tuple(fee)
# print(fee)
# print(type(fee))


formData={"name":"hareesh","sex":"male","tech":"python","mob":7995877911}
# print(formData)
# print(type(formData))
# print(dir(dict))
# print(formData["mob"])
# print(formData["lname"])
# formData["tech"]="machine learning"
# print(formData["tech"])
# formData["lname"]="mutyala"
# print(formData["lname"])
# print(formData)
# print(formData.keys())
# print(formData.values())
# print(formData.items())
# for i in formData:
	# print(i)
# for i in formData.keys():
# 	print(i)
# for i in formData.values():
# 	print(i)
# for i in formData.items():
# 	print(i)
# formData.clear()
# print(formData)
# new=formData.copy()
# print(new)
# a=formData.pop("name")
# print(a)
# print(formData)
# b=formData.popitem()
# print(formData)
# print(b)
# nums={1:2,2:3,4:5,6:7}
# nums.update(formData)
# print(nums)
# print(formData)
# formData.update({10:20,30:40})
# print(formData)
# print(len(formData))
# l1=[1,2,3,4,5,6,7,8,9]
# l2=["a","b","c","d","e","f"]
# # z = zip(l1,l2)
# # print(z)
# # print(dict(z))
# e=enumerate(l1)
# print(e)
# print(dict(e))


# l1=[i for i in range(1,5)]
# l2=[i**2 for i in range(1,5)]
# print(dict(zip(l1,l2)))

# d={}
# for i in range(1,5):
	# d[i]=i**2
# print(d)


# di={x:x**2 for x in range(1,9)}
# print(di)

# listtask=[10,20,30,[2,4,5],100,(1,2,3),200]
# output=[]
# for x in listtask:
# 	if  type(x) is tuple or type(x) is list:
# 		for i in x:
# 			output.append(i)
# 	else:
# 		output.append(x)
# print(output)	


# l1=[5,8,2,9,]
# l2=[13,43,65,89,]
# opp=[x+y for x,y in zip(l1,l2)]
# print(opp)
# op=[]
# for x,y in zip(l1,l2):
# 	op.append(x+y)
# print("output:",op)

# mean=0
# total=0
# for i in range(1,101):
# 	total +=i
# mean = total/100
# print(mean)
# cumsum=0
# for i in range(1,101):
# 	cumsum += (i-mean)
# print(cumsum)













































