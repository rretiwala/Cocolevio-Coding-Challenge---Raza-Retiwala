# Finds optimal profit given a selection of fabric buyers


def createLists(infile):

    # One list to store each thing
    companies = []
    buying = []
    prices = []
    # Go line by line in infile and take the items out

    for line in infile:
        line = line.strip()
        line = line.split()

        companies.append(line[0])
        buying.append(int(line[1]))
        prices.append(int(line[2]))
    return companies, buying, prices


def createMatrix(available, needed, prices, n):
    K = [[0 for x in range(available + 1)] for x in range(n + 1)]


    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(available + 1):
            if i == 0 or w == 0:
                K[i][w] = 0

            elif needed[i - 1] <= w:
                K[i][w] = max(prices[i - 1] + K[i - 1][w - needed[i - 1]], K[i - 1][w])

            else:
                K[i][w] = K[i - 1][w]

    return K


def backTrack(K, buying):
    n = len(K)-1
    end = len(K[0])-1
    indexes = []

    for item in K:
        print (item)

    while K[n][end] != 0:
        if K[n][end] != K[n-1][end]:
            print (buying)
            end -= buying[n-1]
            indexes.append(n)

        n-=1
        print(n, end)
        print()


    return indexes


def main():

    # # Takes in the file
    # infile = open('Input.txt', 'r')
    # # Convert the file input into a dictionary of information
    # companies, buying, prices = createLists(infile)
    #
    # # Prompt user for amount available to sell

    while True:

        available = int(input("How much material are you selling?: "))
        # print(companies)
        # print(buying)
        # print(prices)

        prices = [1, 4, 5, 7]
        buying = [1, 3, 4, 5]


        matrix = createMatrix(available, buying, prices, len(buying))
        maxPrice = matrix[-1][-1]
        indexes = backTrack(matrix, buying)

        print ('The max price is', maxPrice)
        print(indexes)


main()