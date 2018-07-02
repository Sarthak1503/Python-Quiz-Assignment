import keyword 
l=keyword.kwlist
n=input("Enter any word: ")
if n in l:
	print('() is keyword'.format(n))
else:
	print('This word is not a keyword')
	print(l)
