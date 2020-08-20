l=input()
openbrackets=['(','[','{']
l1=list()
flag=False
count=0
for ds in l:
	count+=1
	if(ds in openbrackets):
		l1.append(ds)
	elif(ds==']'):
		if(l1[-1]=='['):
			l1.pop()
		else:
			flag=False
			break
	elif(ds==')'):
		if(l1[-1]=='('):
			l1.pop()
		else:
			flag=False
			break
	elif(ds=='}'):
		if(l1[-1]=='{'):
			l1.pop()
		else:
			flag=False
			break
	if(count==len(l) and not l1):
		flag=True
		break

		

if(flag):
	print('Balanced')
else:
	print('unbalanced')

# method 2

# l=["(",'{','[']
# r=[')','}',']']
# ln=input()
# list1=list()
# for i in ln:
# 	if i in l:
# 		list1.append(i)
# 	elif i in r:
# 		pos=r.index(i)
# 		if(len(list1)>0 and (l[pos]== list1[-1])):
# 			list1.pop()
# 		else:
# 			print('Unbalanced')
# 			break 

# if(len(list1)==0):
# 	print('Balanced')
# else:
# 	print('Unbalanced')