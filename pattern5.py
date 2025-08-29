N=int(input("enter the number"))
for i in range(0,N+1):
    for j in range(1,N+1):
        if(j==1)or(j==N):
            print("*",end=" ")
        else:
            print("_",end=" ")
    print()    