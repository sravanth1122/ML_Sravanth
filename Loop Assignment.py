#!/usr/bin/env python
# coding: utf-8
# test to git
# In[1]:


# Q. W. A P. which takes one number from 0 to 9 from the user and prints
# it in the word. And if the word is not from 0 to 9 then
# it should print that number is outside of the range and program should
# exit.
# For exapmple:-
# input = 1
# output = one

i=int(input('Enter a number between 0-9\n'))
if i==0:
    print('Zero')
elif i==1:
    print('one')
elif i==2:
    print('two')
elif    i==3:
    print('three')
elif    i==4:
    print('Four')
elif    i==5:
    print('Five')
elif    i==6:
    print('Six')
elif    i==7:
    print('Seven')
elif    i==8:
    print('Eight')
elif    i==9:
    print('Nine')
else:
    print('Given number is out of range')


# In[2]:


# Q. W. A P. to implement calculator but the operation to be done and two numbers will be taken as input from user:-
# Operation console should show below:-
#  Please select any one operation from below:-
#  * To add enter 1
#  * to subtract enter 2
#  * To multiply enter 3
#  * To divide enter 4
#  * To divide and find quotient enter 5
#  * To divide and find remainder enter 6
#  * To divide and find num1 to the power of num2 enter 7
#  * To Come out of the program enter 8


# In[3]:


INPUT='''Please select any one operation from below:-
 * To add enter 1
 * to subtract enter 2
 * To multiply enter 3
 * To divide enter 4
 * To divide and find quotient enter 5
 * To divide and find remainder enter 6
* To divide and find num1 to the power of num2 enter 7
* To Come out of the program enter 8\n'''
b=int(input(INPUT))
if b==8:
    print('Nothing to show')
else:
    c1=int(input('Enter the first number'))
    c2=int(input('Enter the second number'))
    if b==1:
        print(c1+c2)
    elif b==2:
        print(c1-c2)
    elif b==3:
        print(c1*c2)
    elif b==4:
        print(c1/c2)
    elif b==5:
        print(c1//c2)
    elif b==6:
        print(c1%c2)
    elif b==7:
        print(c1/c2)
        print(c1**c2)


# In[4]:


# Q. W A P to check whether a year entered by user is an leap year or not?
# Check with below input:-
#  leap year:- 2012, 1968, 2004, 1200, 1600,2400
#  Non-lear year:- 1971, 2006, 1700,1800,1900
c=int(input('Enter the year'))
if c%4==0:
    if c%400==0:
        print('Leap year')
    elif c%100!=0:
        print("leap year")
    else:
        print('Non leap year')
else:
    print('non-leap year')


# In[5]:


# Q. W A P which takes one number from the user and checks whether it is
# an even or odd number?, If it even then prints number is
# even number else prints that number is odd number.
d=int(input('Enter the number'))
if d%2==0:
    print('Number is even number')
else:
    print('Number is odd number')


# In[6]:


# Q. W A P which takes two numbers from the user and prints below output:-
#  1. num1 is greater than num2 if num1 is greater than num2
#  2. num1 is smaller than num2 if num1 is smaller than num2
#  3. num1 is equal to num2 if num1 and num2 are equal
# Note:- 1. Do this problem using if - else
#  2. Do this using ternary operator

e1=int(input('enter the number1'))
e2=int(input('enter the number2'))
e3=('num1 is greater than num2' if e1>e2 else 'num1 is smaller than num2'if e1<e2 else 'num1 and num2 are equal')
print(e3)


# In[7]:




# Q. W A P which takes three numbers from the user and prints below
# output:-
#  1. num1 is greater than num2 and num3 if num1 is greater than num2
# and num3
#  2. num2 is greater than num1 and num3 if num2 is greater than num1
# and num3
#  3. num3 is greater than num1 and num2 if num3 is greater than num1
# and num2
# Note:- 1. Do this problem using if - elif - else
#  2. Do this using ternary operator
# a = a if a>b else b
# Loops - for loop, while loop
f1=int(input('enter the number1'))
f2=int(input('enter the number2'))
f3=int(input('enter the number3'))
f4=('num1 is greater than num2 and num3'if f1>f2&f1>f3 else 'num2 is greater than num1 and num3' if f2>f1&f2>f3 else 'num3 is greater than num1 and num2')
print(f4)


# In[8]:


# Q. Write a Python program to find the length of the my_str using loop:-
str='Write a Python program to find the length of the my_str'
# Output:- 55
j=0
for i in str:
    j=j+1    
print(j)
    


# In[9]:



# Q. Write a Python program to find the total number of times letter 'p'
# is appeared in the below string using loop:-
str_Input='peter piper picked a peck of pickled peppers.\n'
# Output:- 9
count=0
for i in str_Input:
    if i=='p':
        count=count+1
print(count)
        


# In[10]:



# Q. Write a Python Program, to print all the indexes of all occurences of
# letter 'p' appeared in the string using loop:-
str='peter piper picked a peck of pickled peppers.'
# Output:-
# 0
# 6
# 8
# 12
# 21
# 29
# 37
# 39
# 40
s_len=len(str)
for i in range(s_len):
    if str[i]=='p':
        print(i)


# In[11]:


# Q. Write a python program to find below output using loop:-
# Input:- 'peter piper picked a peck of pickled peppers.'
# Output:- ['peter', 'piper', 'picked', 'a', 'peck', 'of', 'pickled',
# 'peppers']
out_lst=[]
out_str=''
for i in str:
    if i==' ' or i=='.':
        out_lst.append(out_str)
        out_str=''
    else:
        out_str +=i
print(out_lst)
    


# In[12]:



# Q. Write a python program to find below output using loop:-
str= 'piter piper picked a peck of pickled peppers.'
# Output:- 'peppers pickled of peck a picked piper peter'
out_lst=[]
out_str=''
for i in str:
    if i==' ' or i=='.':
        out_lst.insert(0,out_str)
        out_str=''
    else:
        out_str += i
rev_str= ''
for j in out_lst:
    rev_str=rev_str+' '+j
print(rev_str)


# In[13]:


# Q. Write a python program to find below output using loop:-
# Input:- 'peter piper picked a peck of pickled peppers.'
# Output:- '.sreppep delkcip fo kcep a dekcip repip retep'
le=len(str)
out_str=''
for i in range(le):
    out_str=out_str+str[le-1]
    le=le-1
print(out_str)


# In[14]:


# Q. Write a python program to find below output using loop:-
str='peter piper picked a peck of pickled peppers.'
# Output:- 'retep repip dekcip a kcep fo delkcip sreppep'
out_lst=[]
out_str=''
for i in str:
    if i==' ' or i=='.':
        out_lst.append(out_str)
        out_str=''
    else:
        out_str +=i
rev_str=''
le=len(out_lst)
for j in range(le):
    le2=len(out_lst[j])
    for k in range(le2):
        rev_str=rev_str+out_lst[j][le2-1]
        le2=le2-1
    rev_str+=' '
print(rev_str)


# In[15]:


# Q. Write a python program to find below output using loop:-
# Input:- 'peter piper picked a peck of pickled peppers.'
# Output:- 'Peter Piper Picked A Peck Of Pickled Peppers'
op_str=''
for i in str:
    if i=='a':
        op_str=op_str+'A'
    else:
        op_str=op_str+i
print(op_str)


# In[16]:


# Q. Write a python program to find below output using loop:-
str2='Peter Piper Picked A Peck Of Pickled Peppers.'
# Output:- 'Peter piper picked a peck of pickled peppers'
op_str=''
for i in str2:
    if i=='A':
        op_str=op_str+'a'
    else:
        op_str=op_str+i
print(op_str)


# In[17]:


# Q. Write a python program to implement index method using loop. If
# sub_str is found in my_str then it will print the index
# of first occurrence of first character of matching string in my_str:-
my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str = 'Pickl'
# Output:- 29
s=0
e=len(sub_str)
e2=len(sub_str)
x=0
for i in range(len(my_str)):
    my_op=my_str[s:e:]
   # print(my_op)
    s=s+1
    e=e+1
    if sub_str==my_op:
        x=1
        ind=my_str.index(my_op)
        print(s-1)
if x==0:
    print('Sub_str not found in main_str')

        


# In[18]:


# Q. Write a python program to implement replace method using loop.
# If sub_str is found in my_str then it will replace the first
# occurrence of sub_str with new_str else it will will print sub_str not
# found:-
my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str = 'Peck'
new_str = 'Pack'
# Output:- 'Peter Piper Picked A Pack Of Pickled Peppers.'
s=0
e=len(sub_str)
e2=len(sub_str)
for i in range(len(my_str)):
    my_op=my_str[s:e:]
   # print(my_op)
    s=s+1
    e=e+1
    if sub_str==my_op:
        ind=my_str.index(my_op)
        #print(s-1)
ind2=ind+len(sub_str)
my_str[:ind]+new_str+my_str[ind2:]


# In[19]:



# Q. Write a python program to find below output (implements rjust and
# ljust) using loop:-
my_str='Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str ='Peck'
# Output:- '*********************Peck********************'
sub_str ='Peck'
s=0
e=len(sub_str)
e2=len(sub_str)
for i in range(len(my_str)):
    my_op=my_str[s:e:]
   # print(my_op)
    s=s+1
    e=e+1
    if sub_str==my_op:
        ind=my_str.index(my_op)    
#rjust
op=sub_str.rjust(ind+e2,'*')
for i in range(ind+e2,len(my_str)):
    op=op+'*'
print(op)

#ljust
op2=''
for j in range(ind):
    op2+='*'
print(op2+sub_str.ljust(len(my_str)-ind,'*'))


# In[20]:


# Q. Write a python program to find below output using loop:-
str='This is Python class'
sep = 'is'
#Output:- ['This', 'is', 'Python class']
out_lst=[]
out_str=''
count=0
for i in str:
    if i==' ' or i=='.':
        out_lst.append(out_str)
        out_str=''
        count=count+1
    else:
        out_str +=i
        count=count+1
    if out_str==sep:
        out_lst.append(out_str)
        out_lst.append(str[count+1:])
        print(out_lst)


# In[ ]:




