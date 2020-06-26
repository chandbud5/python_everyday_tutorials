# sum of all elements using loop 

lst = [3,5,6,7,8,1]
s = 0
for i in lst:
    s = s+i

print("Sum of all elements is ",s)

# Factorial of a Number - given by user
n = int(input())
i = 1
while n>1:
    i = i*n
    n = n-1

print(i)

# Print pattern
#   ****
#   ***
#   **
#   *

n = 4
for i in range(n):
    for j in range(n-i,0,-1):
        print(j, end="")
    print("")
