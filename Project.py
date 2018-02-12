# Finds optimal profit given a selection of fabric buyers

# Code adapted from https://www.geeksforgeeks.org/knapsack-problem/

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
    # Finds the ideal solution for every weight given remaining fabric
    # limit       0 1 2 3 4 5 6 7
    # val, weight
    # 1    1      0|1|1|1|1|1|1|1|
    # 4    3      0|1|1|4|5|5|5|5|
    # 5    4      0|1|1|4|5|6|6|9|
    # 7    5      0|1|1|4|5|7|8|9|
    
    for i in range(n + 1):
        for w in range(available + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
               
            #If the needed weights for a company are less than or equal the index, find the max
            elif needed[i - 1] <= w:
                #Compares the profit with using a particular weight vs. the ideal profit without using that specific 
                K[i][w] = max(prices[i - 1] + K[i - 1][w - needed[i - 1]], K[i - 1][w])

            else:
                K[i][w] = K[i - 1][w]

    return K


def backTrack(K, buying):
    n = len(K)-1
    end = len(K[0])-1
    indexes = []


    while K[n][end] != 0:
        if K[n][end] != K[n-1][end]:
            end -= buying[n-1]
            indexes.append(n-1)

        n-=1

    return indexes


def main():

    # Takes in the file
    infile = open('Input.txt', 'r')
    # Convert the file input into a dictionary of information
    companies, buying, prices = createLists(infile)

    # Prompt user for amount available to sell

    while True:

        available = int(input("How much material are you selling?: "))

        matrix = createMatrix(available, buying, prices, len(buying))
        maxPrice = matrix[-1][-1]
        indexes = backTrack(matrix, buying)
        for item in reversed(indexes):
            print ("Company", companies[item], "will pay", prices[item], "and purchase", buying[item])

        print ('The max price is', maxPrice)



main()
