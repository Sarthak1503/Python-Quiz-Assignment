#3.Write a program which accepts a sequence of comma-separated no.s from console &
#  generate a list & tuple which contains every number. 
st=input('Enter the sequence:')
l=st.split(',')
t=tuple(l)
print(l)
print(t)