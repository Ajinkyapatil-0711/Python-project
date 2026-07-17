'''
number= 1
while number <=100:
    print(number)
    number +=1
    
   
num=100
while num >=0:
    print(num)
    num-=1
    
    print("--------------------------------------------------------")
    
    
i=1
n=2
while i<=10:
    print(n*i)
    i+=1
    
    lis= [1, 4, 9, 26,32, 46,89,25]
indx=0
while indx < len(lis):
    print(lis[indx])
    indx+=1
'''
num = (1, 2, 3, 4, 5, 6, 7, 8, 9)
x = 4
i = 0

while i < len(num):
    if num[i] == x:
        print("Found", x, "at index", i)
        break
    else:
        print("Finding...")
    i += 1

