# If - Else
# Number positive k negative

# Simple

x = 6
if x>0:
    print("positive")
else:
    print("Negative")

# Ladder
if x>0:
    print("positive")

#else if
elif x==0:
    print("zero")

else:
    print("Negative")


# Find greatest number among 3 integers
# Nested
a = 6
b = 7
c = 9

if a>b:
    if a>c:
        print("A is greatest")

    else:
        print("c is gretest")

else:
    if b>c:
        print("b is greatest")
    else:
        print("C is greatest")

# Task-1 : Take 3 integers as input from user and try to find greatest among them using ladder if else
# Task-2 : Print all the numbers divisible by 3 in 1 to 100