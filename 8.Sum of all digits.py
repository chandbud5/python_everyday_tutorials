n = int(input("Enter a number"))
# 9432
s = 0
while n>=1:
    x = n%10
    s += x
    n = n // 10

print("Sum of all digits is ",s)