# Enter 5 values in a list
vals = []
n = int(input("Ketli value apso"))  # 5
for i in range(0,n):
    x = int(input("Enter value"))
    vals.insert(i, x)

print(vals[0])
print(vals)

# List in for loop

vals = [4,6,8,42,1]
for i in vals:
    print(i*2)
