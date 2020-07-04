# 992

def welcome(i):
    print("Hello ", i)
    welcome(i+1)

#welcome(1)

# 5! = 5.4! = 5.4.3! 5.4.3.2.1

def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

factorial(8)