# user number prime/ not prime

n = int(input())

for i in range(2,n):
    if n%i==0:
        print("Not Prime")
        break
else:
    print("Prime")


# with Boolean
f = False
for i in range(2,n):    # 2-n
    if n%i==0:  # divisible
        f = True

if f:
    print("Not Prime")
else:
    print("Prime")