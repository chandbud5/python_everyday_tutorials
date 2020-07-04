# USER DEFINED FUNCTION

# 1.Define
# 2.Call
#    1. def 
#    2. function_name
#    3. arguments ()

def welcome():
    print("Hey, welcome")

welcome()

# 4 types
# 1. Postional Argument
# 2. Keyword Argument
# 3. Default Argument
# 4. Variable Length Argument

def Person(name,age=20):
    print("Name is ",name)
    print("Age is ", age)

# Positional
Person(19, "Chand")

# Keyword
Person(age=19, name="Chand")

# Default
Person("Chand")

# Variable Length
# 2*5*7*3
def mul(*b):
    x = 1
    for i in b: #()
        x*=i
    print("Multiplicaiton is ",x)

mul(6,3,1)