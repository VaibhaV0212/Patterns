'''
for row in range(7):
    for col in range(5):
        if (col==0) or (col==1 and (row>2 and row<4)) or (col==2 and (row>1 and row<5 and row!=3)):
            print('*',end="")
        else:
            print(end=" ")
    print("")
'''
i=0
j=4
for row in range(7):
    for col in range(5):
        if (col==0) or (row==col+2 and col>1):
            print('*',end="")
        elif (row==i and col==j):
            print('*',end="")
            i=i+1
            j=j-1
        else:
            print(end=" ")
    print("")