#4.Create a program that asks the user to enter their name and their age. Print out a
# message addressed to them that tells them the year that they will turn 100 years old. 
name=str(input("Enter Your Name="))
age=int(input("Enter Your Age="))
if age>100:
	print("Congrats! You crossed 100 years")
else:
    req=100-age
    print("Name={},Your required age for completion of 100 years={}".format(name,req))
