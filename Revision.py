# while - condition
# Condition / Bool
# 1) Variable intialise
# 2) Condition
# 3) Variable Inc/Dec

i=0
while i<5:
    print(i*i)
    i = i+1 # i+=1

b = True
while b:
    print("Hello")
    b = False


# For Loop
# 1) Range / List

for i in range(0,7):    # AP 5,4,3,2,1,0
    print(i)

vals = [1,2,4,0,6,4,2]
for a in vals:
    if a%3!=0:
        print(a)

# Sum of first 20 numbers 1 to 20
# while / for
# for - fix
# while - vary

s = 1
i = 1
while i<21:
    s = s*i
    i += 1  # i=i+1

print("pro of 1 to 20 ",s)# n(n+1)/2

#       4
#     3 4
#   2 3 4
# 1 2 3 4
#4,0     0,5
for i in range(4,0,-1):

    for k in range(i-1,0,-1):
        print(" ",end="")
    for j in range(i,5):
        print(j, end="")
    print("")

i=4
while i>0:
    k = i-1
    while k>0:
        print(" ",end="")
        k-=1
    j = i
    while j<5:
        print(j, end="")
        j+=1
    print("")

    i-=1