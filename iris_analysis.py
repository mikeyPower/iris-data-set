# Predict the class of the flower based on available attributes.




def main():

    file = open("iris.data", "r")
    data =[]

    for line in file:
        print(line.rstrip().split(','))


if __name__ == '__main__':
    main()
