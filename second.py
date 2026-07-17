#Decision making statement
from pickle import TRUE

a= 10
b= 20

if b < a:   
    print("hello")  

else:
    print("bye") 
    

#While loop    

while True:
    print("While loop")
    break

d1= 1234
print(type(d1))

a1 = True
print(type(a1))

b1="poorna"
print(type(b1))

c1= 6+9j
print(type(c1))

e1=''' This is code '''
print(e1)
           #012345678910111213141516
my_String= "my_name_is_poorna"
print(my_String[4])

print(my_String[3:7])
print(my_String[11:17])

fruit= "I like apples,mango,banana,grapes,cherries"
print(fruit.split(","))

tupl=("true","a", 100, "false", "b")
print(type(tupl))

l1=[1, "a", 2, "true", 3]
l1[0]=100
print(l1)

l1.append(45)
print(l1)

l1.pop(0)
print(l1)


my_dict={
    
    "name" : "ajinkya",
    "age"  : 25,
    "city" : "pune"
    
    }

print(my_dict)


#----------------------------------

a=10
b=20
c=30

if (a >b & b>c):
    print("a is the greatest")
elif (b > a & c >a):
    print("b is greatest")
else:
    print("c is greatest")
    
#------------------------------------------

L1=[1,2,3,4,5]
if L1[4]==6:
    L1[1]=L1[1]+100
    print(L1)
else:
    L1[4]=L1[4]+500
    print(L1)
#-------------------------------------------------------

i=1
n=2
while i<=10:
    print(n, "*", i, "=", n*i)
    i=i+1
        