# num = int(input("enter a number dear:"))
# sqnum = str(num**2)
# cunum = str(num**3)
# num = str(num)
# lenght= len(cunum)
# print("%s %s %s" % (num.zfill(lenght),sqnum.zfill(lenght),cunum))

# output

# enter a number dear:3
# 03 09 27

# enter a number dear:5
# 005 025 125

# enter a number dear:10
# 0010 0100 1000


# Task2

# time=input("Enter Time as HH:MM:SS AM/PM   ")
# time1=time.split(":")
# hh=int(time1[0])
# ss=int(time1[2][0:2])
# temp=time1[2][2:4]
# if(time=="12:00:00am" or time=="12:00:00pm"):
# 	print("00:00:00am")
# else:	
# 	if(temp=='pm'):
# 		if(hh<12):
# 			hh=hh+12
# 		print("%d:%s:%d" %(hh,time1[1],ss))
# 	else:
# 		print("%s:%s:%d" %(time1[0],time1[1],ss))


# output

# Enter Time as HH:MM:SS AM/PM   03:55:33pm
# 15:55:33

# Enter Time as HH:MM:SS AM/PM   12:00:00am
# 00:00:00am


 



