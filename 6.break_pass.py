#break
s = 5
while s>0:
    print(s)
    if s==3:
        print("Break statement")
        break
    s = s-1

# continue
s = 5
while s>0:
    if s==3:    #3
        s =s-1  #2
        print("cont statement")
        continue
    s = s-1
    print(s)

# pass
s=5
while s>0:
    print(s)
    if s==3:
        s=s-1
    else:
        pass
    s = s-1

# Task - 1
lst = []
while True:
    x = input("enter")
    if x == 'q':
        break

    lst.append(int(x))

