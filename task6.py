time= int(input("enter time:"))
if(time>0 and time<=24):
	if(time>=7 and time<=11):
		print("good morning")
	elif(time>11 and time<=15):
   		print("good afternoon")
	elif(time>15 and time<=19):
   		print("good evening")
	else:
		print("good night")
