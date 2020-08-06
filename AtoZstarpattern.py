"programme for word to star pattern"

w = []
a = input("Enter spelling : ").upper()
for i in a:
    w.append(i)

for j in w:
    if j == "A":
        for i in range(7):
            for j in range(6):
                if i == 0 and j in {1, 2, 3, 4}:
                    print("#", end=" ")
                elif i in {1, 2, 4, 5, 6} and j in {0, 5}:
                    print("#", end=" ")
                elif i == 3:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()

    elif j == "E":
        for i in range(7):
            for j in range(5):
                if i in {0, 6} and j in {0, 1, 2, 3, 4}:
                    print("#", end=" ")
                elif i == 3 and j in {0, 1, 2, 3}:
                    print("#", end=" ")
                elif j == 0:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()
        print("\n")

    elif j == "B":
        for i in range(7):
            for j in range(5):
                if i in {0, 6} and j in {0, 1, 2, 3}:
                    print("#", end=" ")
                elif i in {1, 2, 4, 5} and j in {0, 4}:
                    print("#", end=" ")
                elif i == 3 and j in {0,1,2,3}:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()
        print("\n")

    elif j == "C":
        for i in range(7):
            for j in range(5):
                if i in {0,6} and j in {1,2,3,4}:
                    print("#",end=" ")
                elif i in {1,2,3,4,5} and j == 0:
                    print("#", end=" ")
                else:
                    print(" ",end=" ")
            print()

    elif j == "D":
        for i in range(7):
            for j in range(5):
                if i in {0,1,2,3,4,5,6} and j == 0:
                    print("#", end=" ")
                elif i in {0,6} and j in {1,2,3}:
                    print("#", end=" ")
                elif i in {1,2,3,4,5} and j == 4:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()

    elif j == "F":
        for i  in range(7):
            for j in range(5):
                if i in {0,1,2,3,4,5,6} and j == 0:
                    print("#", end=" ")
                elif i == 0:
                    print("#", end=" ")
                elif i == 3 and j in {1,2,3}:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()

    elif j == "G":
        for i in range(7):
            for j in range(6):
                if j in {1,2,3} and i in {0,6}:
                    print("#", end=" ")
                elif i in {1,2,3,4,5} and j == 0:
                    print("#", end=" ")
                elif i in {1,2} and j == 4:
                    print("#", end=" ")
                elif i in {4,5} and j == 4:
                    print("#", end=" ")
                elif i == 4 and j in {4,3,5}:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()

    elif j == "H":
        for i in range(7):
            for j in range(5):
                if i in {0,1,2,4,5,6} and j in {0,4}:
                    print("#", end=" ")
                elif i == 3:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()

    elif j == "I":
        for i in range(7):
            for j in range(5):
                if j == 2:
                    print("#", end=" ")
                elif i in {0,6} and j in {0,1,2,3,4}:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()


    elif j == "J":
        for i in range(7):
            for j in range(6):
                if i == 0:
                    print("#", end=" ")
                elif i in {1,2,3,4,5} and j == 3:
                    print("#", end=" ")
                elif i == 6 and j in {1,2}:
                    print("#", end=" ")
                elif i in {4,5} and j == 0:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()

    elif j == "K":
        for i in range(7):
            for j in range(7):
                if j == 0:
                    print("#", end=" ")
                elif i == 3 and j == 1:
                    print("#", end=" ")
                elif i in {2,4} and j == 2:
                    print("#", end=" ")
                elif i in {1,5} and j == 3:
                    print("#", end=" ")
                elif i in {0,6} and j == 4:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()



    elif j == "L":
        for i in range(7):
            for j in range(5):
                if j == 0:
                    print("#", end=" ")
                elif i == 6 and j in {1,2,3,4}:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()

    elif j == "M":
        for i in range(7):
            for j in range(7):
                if j in {0,6} and i in {0,1,2,3,4,5,6}:
                    print("#", end=" ")
                elif i == 1 and j in {1,5}:
                    print("#", end=" ")
                elif i == 2 and j in {2,4}:
                    print("#", end=" ")
                elif i == 3 and j == 3:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()


    elif j == "N":
        a = 1
        b = 1
        for i in range(7):
            for j in range(7):
                if j == 0 or j == 6:
                    print("#", end=" ")
                elif i == a and j == b:
                    print("#", end=" ")
                    a+=1
                    b+=1
                else:
                    print(" ", end=" ")
            print()

    elif j == "O":
        for i in range(7):
            for j in range(5):
                if i in {0,6} and j in {1,2,3}:
                    print("#", end=" ")
                elif i in {1,2,3,4,5} and j in {0,4}:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()

    elif j == "P":
        for i in range(7):
            for j in range(5):
                if j == 0:
                    print("#", end=" ")
                elif i in {0,3} and j in {1,2,3}:
                    print("#", end=" ")
                elif i in {1,2} and j == 4:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()

    elif j == "Q":
        for i in range(8):
            for j in range(7):
                if i in {0, 6} and j in {1, 2, 3}:
                    print("#", end=" ")
                elif i in {1, 2, 3, 4, 5} and j in {0, 4}:
                    print("#", end=" ")
                elif i == 5 and j == 3:
                    print("#", end=" ")
                elif (i == 6 ) and j == 4 :
                    print("#", end=" ")
                elif (i == 7 ) and j == 5 :
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()

    elif j == "R":
        for i in range(7):
            for j in range(6):
                if j == 0:
                    print("#", end=" ")
                elif i in {0, 3} and j in {1, 2, 3}:
                    print("#", end=" ")
                elif i in {1, 2} and j == 4:
                    print("#", end=" ")
                elif i == 4 and j == 1:
                    print("#", end=" ")
                elif i == 5 and j == 2:
                    print("#", end=" ")
                elif i == 6 and j == 3:
                    print("#", end=" ")
                elif i == 6 and j == 4:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()

    elif j == "S":
        for i in range(7):
            for j in range(6):
                if i in {0,3,6} and j in {1,2,3,4}:
                    print("#", end=" ")
                elif i in {1,2} and j == 0:
                    print("#", end=" ")
                elif i in {4,5} and j == 5:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()

    elif j == "T":
        for i in range(7):
            for j in range(7):
                if i == 0:
                    print("#", end=" ")
                elif j == 3:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()

    elif j == "U":
        for i in range(7):
            for j in range(6):
                if j in {0,5} and i in {0,1,2,3,4}:
                    print("#", end=" ")
                elif i == 5 and j in {1,2,3,4}:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()

    elif j == "V":
        for i in range(7):
            for j in range(7):
                if i in {0,1,2} and j in {0,6}:
                    print("#", end=" ")
                elif i == 3 and j in {1,5}:
                    print("#", end=" ")
                elif i == 4 and j in {2,4}:
                    print("#", end=" ")
                elif i == 5 and j == 3:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()

    elif j == "W":
        for i in range(7):
            for j in range(8):
                if i in {0,1,2,3,4,5,6} and j in {0,7}:
                    print("#", end=" ")
                elif i == 5 and j in {1,6}:
                    print("#", end=" ")
                elif i == 4 and j in {2,5}:
                    print("#", end=" ")
                elif i == 3 and j in {3,4}:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()

    elif j == "X":
        for i in range(7):
            for j in range(7):
                if i == 0 and j in {0,6}:
                    print("#", end=" ")
                elif i == 1 and  j in {1,5}:
                    print("#", end=" ")
                elif i == 2 and j in {2,4}:
                    print("#", end=" ")
                elif i == 3 and j == 3:
                    print("#", end=" ")
                elif i == 4 and j in {2,4}:
                    print("#", end=" ")
                elif i == 5 and j in {1,5}:
                    print("#", end=" ")
                elif i == 6 and  j in {0,6}:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()

    elif j == "Z":
        i=1
        j=4
        for ii in range(7):
            for jj in range(7):
                if ii == 0 or ii == 5:
                    print("#", end=" ")
                elif ii == i and jj == j:
                    print("#", end=" ")
                    i+=1
                    j-=1
                else:
                    print(" ", end=" ")
            print()

    elif j == "Y":
        for i in range(7):
            for j in range(7):
                if i == 0 and j in {0,6}:
                    print("#", end=" ")
                elif i == 1 and j in {1,5}:
                    print("#", end=" ")
                elif i == 2 and j in {2,4}:
                    print("#", end=" ")
                elif j == 3 and i in {3,4,5,6}:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()

    elif j == " ":
        for i in range(3):
            for j in range(3):
                if i in {0,1,2} and j in {0,1,2}:
                    print(" ", end=" ")
            print()




































































































