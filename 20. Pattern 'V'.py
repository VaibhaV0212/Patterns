i=0
j=6
for row in range(4):
    for col in range(7):
        if (col==row):
                #or ((row==2 and col==4) or (row==1 and col==5) or (row==0 and col==6)):
            print('*',end="")
        elif (row==i and col==j):
            print('*', end="")
            i=i+1
            j=j-1
        else:
            print(end=" ")
    print("")