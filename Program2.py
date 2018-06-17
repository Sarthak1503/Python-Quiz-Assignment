#2.Write a program which will find all such no.s which are divisible by 7 
# but are not multiple of 5,between 2000&3200. The no.s obtained should be printed 
# in a comma-separated sequence on a single line.
l=[]
for i in range(2000,3201):
	if i%7==0:
		if i%5!=0:
			l.append(i)
print(l)