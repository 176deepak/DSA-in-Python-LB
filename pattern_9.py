from re import I


N = int(input())
i = 1

while(i <= N):
    j = 1
    while(j <= i):

        print(i+j-1, end = " ")
        j+= 1
    print()
    i+= 1