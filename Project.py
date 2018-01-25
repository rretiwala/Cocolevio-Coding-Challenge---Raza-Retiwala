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


def findMax(available, needed, prices, n):
    K = []
    for i in range(n+1):
        K.append([])
        for l in range(available + 1):
            K[i].append(0)

    for item in K:
        print(item)

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(available + 1):
            if i == 0 or w == 0:
                K[i][w] = 0

            elif needed[i - 1] <= w:
                K[i][w] = max(prices[i - 1] + K[i - 1][w - needed[i - 1]], K[i - 1][w])

            else:
                K[i][w] = K[i - 1][w]

    return K[n][available]


def main():

    # Takes in the file
    infile = open('Input.txt', 'r')
    # Convert the file input into a dictionary of information
    companies, buying, prices = createLists(infile)

    # Prompt user for amount available to sell
    available = int(input("How much material are you selling?: "))
    print(companies)
    print(buying)
    print(prices)

    maxPrice = findMax(available, buying, prices, len(companies))

    print(maxPrice)

main()