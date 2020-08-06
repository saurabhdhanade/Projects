#pyramid pattern
def pattern(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("*", end=" ")
        print()


pattern(5)

#reverse pyramid
def reversepyra(n):
    k = n * 2 - 2
    for i in range (n,-1,-1):
        for j in range (k,0,-1):
            print(end=" ")
        k=k+1
        for j in range (0,i+1):
            print("*",end=" ")
        print()

reversepyra(5)

#right side tringle pattern
def pattern(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("*", end=' ')
        print()
    for i in range(n, 0, -1):
        for j in range(0, i + 1):
            print("*", end=' ')
        print()


pattern(5)

#hourglass pattern
def pattern(n):
    k = n - 2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("*", end=" ")
        print()
    k = 2 * n - 2
    for i in range(0, n + 1):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("*", end=" ")
        print()
        
pattern(5)

#right angle tringle pattern
def rightangle(n):
    for i in range(0,n):
        for j in range(0,1+i):
            print("*", end=" ")
        print()
rightangle(5)

#right side right angle tringle
def pattern(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("*", end=" ")
        print()


pattern(5)

