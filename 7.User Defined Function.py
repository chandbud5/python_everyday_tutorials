# USER defined function

# max(vals)

def add(a,b):
    c = a+b
    return c


x = add(5,7)
y = add(9,7)
z = add(5,8)
print(x**2,y,z)
# Retruning and Non returning

# BODY MASS INDEX
def bmi():
    weight = float(input("WHat is your weight(in kg)?\n"))
    height = float(input("WHat is your Height(in m)?\n"))
    x = height*height
    c = weight/x

    print("BMI is ",c)

bmi()

# Variable length arguments
def smart_add(a, *b):
    print(a+b)
    s = 0
    for i in b:
        s+=i

    print("Sum is ",a+s)

smart_add(2,0,8,5,6)

# Keyword Argument
# Position Argument


# Task - Sum of 3 digits of a number
#23 - 2+3 = 5
#289 - 2+8+9 = 19
