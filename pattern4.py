n = 5
num = 1
for i in range(1, n + 1):
    for j in range(i):
        if j % 2 == 0:
            print(num, end=" ")
            num += 2
        else:
            print("*", end=" ")
    print()
