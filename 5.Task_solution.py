# Task-1 : Take 3 integers as input from user and try to find greatest among them using ladder if else

a = int(input("Enter a num"))
b = int(input("Enter a num"))
c = int(input("Enter a num"))

if a>b and a>c:
    print("A is greatest")

elif b>a and b>c:
    print("B is greatest")

else:
    print("C is greatest")


# Task-2 : Print all the numbers divisible by 3 in 1 to 100

for i in range(1,101):
    if i%3==0:
        print(i)

# Task - 3 :  Print all the numbers divisible by 5 in 1 to 100 While loop
i=0
while i<=100:
    if i%5==0:
        print(i)
    i = i+1

# Task - 4 : Print only those numbers which are divisible by both 4 and 6 from 0 to 100
for i in range(0,101):
    if i%4==0 and i%6==0:
        print(i)