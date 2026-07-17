"""
marks=int(input("marks : "))
if(marks >= 90):
    print("distinction")
elif(marks <= 50 ):
    print("pass")
elif(marks<=35):
    print("fail")
    
a = 10
b = 20
sum = (a + b)
print(sum)

ar1=int(input("area1 is:"))
ar2=int(input("area2 is:"))
print("area of square is :" , ar1* ar2)

str1=input("usser first name: ")
print(str1.__len__())   

"""

user= int(input("Enter number"))
if(user % 10==0):
    print("Even")
elif(user % 10!=0):
    print("odd")