# Soduko algrethom
#
#
#
#

import random
import numpy

def main():
    seedOne = [
        [4, 3, 5, 2, 6, 9, 7, 8, 1],
        [6, 8, 2, 5, 7, 1, 4, 9, 3],
        [1, 9, 7, 8, 3, 4, 5, 6, 2],

        [8, 2, 6, 1, 9, 5, 3, 4, 7],
        [3, 7, 4, 6, 8, 2, 9, 1, 5],
        [9, 5, 1, 7, 4, 3, 6, 2, 8],

        [5, 1, 9, 3, 2, 6, 8, 7, 4],
        [2, 4, 8, 9, 5, 7, 1, 3, 6],
        [7, 6, 3, 4, 1, 8, 2, 5, 9]]
    seedTwo = [
        [6, 2, 5, 8, 7, 4, 1, 3, 9],
        [4, 1, 3, 7, 2, 9, 5, 8, 6],
        [1, 8, 7, 6, 5, 3, 2, 9, 4],

        [5, 6, 2, 3, 9, 7, 4, 1, 8],
        [7, 9, 1, 2, 3, 6, 8, 4, 5],
        [2, 3, 4, 5, 8, 1, 9, 6, 7],

        [9, 5, 6, 4, 1, 8, 3, 7, 2],
        [8, 4, 9, 1, 6, 5, 7, 2, 3],
        [3, 7, 8, 9, 4, 2, 6, 5, 1]]

    '''
        seedTwo = [
            8 1 4 2 7 9 3 6 5
            1 5 9 7 6 3 2 8 4
            4 6 2 3 9 1 7 5 8
            7 2 3 8 1 4 5 9 6
            9 4 5 1   7 6 2 3
            3 9 6 4 5 8 1 7 2
            2 8 7 6 4 5 9 3 1
            6 7 8 5 3 2 4 1 9
            5 3 1 9 2 6 8 4 7
    '''


        # Test case 1

    # N being Dimensions of sqaure array
    N = 9
    mat = [[0 for x in range(N)] for y in range(N)]

    seedList = [seedOne, seedTwo]

    randomSeedNmb = random.randrange(0, len(seedList))


    def rotateMatrix(mat):
        # Consider all squares one by one
        for x in range(0, int(N / 2)):
            for y in range(x, N - x - 1):
                # store current cell in temp variable
                temp = mat[x][y]

                # move values from right to top
                mat[x][y] = mat[y][N - 1 - x]

                # move values from bottom to right
                mat[y][N - 1 - x] = mat[N - 1 - x][N - 1 - y]

                # move values from left to bottom
                mat[N - 1 - x][N - 1 - y] = mat[N - 1 - y][x]

                # assign temp to left
                mat[N - 1 - y][x] = temp

            # Function to print the matrix

    #Displays Matrix
    def displayMatrix(mat):
        for i in range(0, N):
            for j in range(0, N):
                if mat[i][j] == 0:
                    print(" ", end = ' ')
                else:
                    print(mat[i][j], end=' ')
            print("")


    def FlipAndRotate():
        rotationCheck = random.randrange(0, 3)

        if rotationCheck == 1:
            rotateMatrix(seedList[randomSeedNmb])

        elif rotationCheck == 2:
            rotateMatrix(seedList[randomSeedNmb])
            rotateMatrix(seedList[randomSeedNmb])

        elif rotationCheck == 3:
            rotateMatrix(seedList[randomSeedNmb])
            rotateMatrix(seedList[randomSeedNmb])
            rotateMatrix(seedList[randomSeedNmb])

        verticalFlip = random.randrange(0, 2)
        horizontalFlip = random.randrange(0, 2)

        if verticalFlip == 1:
            numpy.flip(seedList[randomSeedNmb])
        if horizontalFlip == 1:
            numpy.fliplr(seedList[randomSeedNmb])

        tempArray2 = numpy.array(seedList[randomSeedNmb])

        collumn = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        random.shuffle(collumn)

        row = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        random.shuffle(row)

        # Randomizes the colloumns ||
        result = tempArray2[:,collumn]

        # randomizes the rows ==
        result = tempArray2[:,row]

        seedList[randomSeedNmb] = result

    def Delete(amount, tempArray):
        secondaryArray = tempArray.copy()

        secondaryArray[4][4] = '0'

        while amount > 0:
            x = random.randint(0, 8)
            y = random.randint(0, 8)


            secondaryArray[x][y] = "0"
            amount = amount - 1

        displayMatrix(secondaryArray)

    # do at end to display

    hardness = int(input("Please Enter Number of Tiles To Be Removed: \n"))-1
    i = int(input("Please Enter Number of Boards To Be Generated: \n"))
    storageAmount = hardness


    while i > 0:
        print("____________________________________________")
        print()
        FlipAndRotate()
        print()
        Delete(hardness, seedList[randomSeedNmb])
        print("sodoku Number: ", i)
        i = i - 1
        print("____________________________________________")

main()
