'''
Created on 6 Aug 2025

@author: Administrator
'''


n_terms = 10  # You can change this number

a, b = 0, 1
count = 0

print("Fibonacci sequence:")
# Print Fibonacci sequence in one line
while count < n_terms:
    print(a, end=' ')
    a, b = b, a + b
    count += 1
    
 #   print(end=' ')
    # Print x only once
x=10
print(x)