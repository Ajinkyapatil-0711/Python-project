'''
Created on 27 Sept 2025

@author: Administrator
'''
from test.test_pprint import list2

'''
user=str(input("enter movie name"))
user1=str(input("movies"))
l1=[]
l1.append(user)
l1.append(user1)
print(l1)

'''

list1 = [1,2,3,2,1,4]
list2 = list1.copy()
list2.reverse()

if(list1==list2):
    print("Palindrome")
else:
    print("not palindrome")
    