# Predict the class of the flower based on available attributes.




def main():

    file = open("iris.data", "r")
    lines = file.readlines()
    data =[]
    iris_setosa=[]
    iris_versicolour=[]
    iris_virginica=[]

    errors = []
    errors.append(lines[34])
    errors.append(lines[37])
    lines.pop(34)
    lines.pop(37)


    for line in lines[:-1]:
        row = line.rstrip().split(',')
        data.append(row)
        if(row[4]=="Iris-setosa"):
            iris_setosa.append([float(x) for x in row[:-1]])
        elif(row[4]=="Iris-versicolor"):

            iris_versicolour.append([float(x) for x in row[:-1]])
        else:
            iris_virginica.append([float(x) for x in row[:-1]])

    setosa_len = len(iris_setosa)
    versicolour_len = len(iris_versicolour)
    virginica_len = len(iris_virginica)

   # print(len(data))
    #print(len(iris_setosa))
    #print(len(iris_versicolour))
    #print(len(iris_virginica))

    setosa_sepal_length_avg=0
    setosa_sepal_width_avg=0
    setosa_petal_length_avg=0
    setosa_petal_width_avg=0

    setosa_sepal_length_max=iris_setosa[0][0]
    setosa_sepal_width_max=iris_setosa[0][1]
    setosa_petal_length_max=iris_setosa[0][2]
    setosa_petal_width_max=iris_setosa[0][3]

    setosa_sepal_length_min=iris_setosa[0][0]
    setosa_sepal_width_min=iris_setosa[0][1]
    setosa_petal_length_min=iris_setosa[0][2]
    setosa_petal_width_min=iris_setosa[0][3]

    #for i in iris_setosa:
        #print(i)



    for i in iris_setosa:
        setosa_sepal_length_avg+=i[0]
        setosa_sepal_width_avg+=i[1]
        setosa_petal_length_avg+=i[2]
        setosa_petal_width_avg+=i[3]

        if(setosa_sepal_length_max < i[0]):
           setosa_sepal_length_max=i[0]
        elif(setosa_sepal_length_min > i[0]):
           setosa_sepal_length_min=i[0]



        if(setosa_sepal_width_max < i[1]):
           setosa_sepal_width_max=i[1]
        elif(setosa_sepal_width_min > i[1]):
           setosa_sepal_width_min=i[1]


        if(setosa_petal_length_max < i[2]):
           setosa_petal_length_max=i[2]
        elif(setosa_petal_length_min > i[2]):
           setosa_petal_length_min=i[2]



        if(setosa_petal_width_max < i[3]):
           setosa_petal_width_max=i[3]
        elif(setosa_petal_width_min > i[3]):
           setosa_petal_width_min=i[3]





    versicolour_sepal_length_avg=0
    versicolour_sepal_width_avg=0
    versicolour_petal_length_avg=0
    versicolour_petal_width_avg=0

    versicolour_sepal_length_max=iris_versicolour[0][0]
    versicolour_sepal_width_max=iris_versicolour[0][1]
    versicolour_petal_length_max=iris_versicolour[0][2]
    versicolour_petal_width_max=iris_versicolour[0][3]
    versicolour_sepal_length_min=iris_versicolour[0][0]
    versicolour_sepal_width_min=iris_versicolour[0][1]
    versicolour_petal_length_min=iris_versicolour[0][2]
    versicolour_petal_width_min=iris_versicolour[0][3]
    for i in iris_versicolour:


        versicolour_sepal_length_avg+=i[0]
        versicolour_sepal_width_avg+=i[1]
        versicolour_petal_length_avg+=i[2]
        versicolour_petal_width_avg+=i[3]


        if(versicolour_sepal_length_max < i[0]):
           versicolour_sepal_length_max=i[0]
        elif(versicolour_sepal_length_min > i[0]):
           versicolour_sepal_length_min=i[0]



        if(versicolour_sepal_width_max < i[1]):
           versicolour_sepal_width_max=i[1]
        elif(versicolour_sepal_width_min > i[1]):
           versicolour_sepal_width_min=i[1]


        if(versicolour_petal_length_max < i[2]):
           versicolour_petal_length_max=i[2]
        elif(versicolour_petal_length_min > i[2]):
           versicolour_petal_length_min=i[2]



        if(versicolour_petal_width_max < i[3]):
           versicolour_petal_width_max=i[3]
        elif(versicolour_petal_width_min > i[3]):
           versicolour_petal_width_min=i[3]










    virginica_sepal_length_avg=0
    virginica_sepal_width_avg=0
    virginica_petal_length_avg=0
    virginica_petal_width_avg=0

    virginica_sepal_length_max=iris_virginica[0][0]
    virginica_sepal_width_max=iris_virginica[0][1]
    virginica_petal_length_max=iris_virginica[0][2]
    virginica_petal_width_max=iris_virginica[0][3]
    virginica_sepal_length_min=iris_virginica[0][0]
    virginica_sepal_width_min=iris_virginica[0][1]
    virginica_petal_length_min=iris_virginica[0][2]
    virginica_petal_width_min=iris_virginica[0][3]
    for i in iris_virginica:

        virginica_sepal_length_avg+=i[0]
        virginica_sepal_width_avg+=i[1]
        virginica_petal_length_avg+=i[2]
        virginica_petal_width_avg+=i[3]


        if(virginica_sepal_length_max < i[0]):
           virginica_sepal_length_max=i[0]
        elif(virginica_sepal_length_min > i[0]):
           virginica_sepal_length_min=i[0]



        if(virginica_sepal_width_max < i[1]):
           virginica_sepal_width_max=i[1]
        elif(virginica_sepal_width_min > i[1]):
           virginica_sepal_width_min=i[1]


        if(virginica_petal_length_max < i[2]):
           virginica_petal_length_max=i[2]
        elif(virginica_petal_length_min > i[2]):
           virginica_petal_length_min=i[2]



        if(virginica_petal_width_max < i[3]):
           virginica_petal_width_max=i[3]
        elif(virginica_petal_width_min > i[3]):
           virginica_petal_width_min=i[3]

    print("Setosa Data :")
    print("Average sepal length :", setosa_sepal_length_avg/setosa_len)
    print("Average sepal width :",setosa_sepal_width_avg/setosa_len)
    print("Average petal length :",setosa_petal_length_avg/setosa_len)
    print("Average petal width :",setosa_petal_width_avg/setosa_len)

    print("Max sepal length :",setosa_sepal_length_max)
    print("Max sepal width :",setosa_sepal_width_max)
    print("Max petal length :",setosa_petal_length_max)
    print("Max petal width :",setosa_petal_width_max)

    print("Minimum sepal length :",setosa_sepal_length_min)
    print("Minimum sepal width :",setosa_sepal_width_min)
    print("Minimum petal legth :",setosa_petal_length_min)
    print("Minimum petal width :",setosa_petal_width_min)
    print()


    print("Versicolour Data :")
    print("Average sepal length :", versicolour_sepal_length_avg/setosa_len)
    print("Average sepal width :",versicolour_sepal_width_avg/setosa_len)
    print("Average petal length :",versicolour_petal_length_avg/setosa_len)
    print("Average petal width :",versicolour_petal_width_avg/setosa_len)

    print("Max sepal length :",versicolour_sepal_length_max)
    print("Max sepal width :",versicolour_sepal_width_max)
    print("Max petal length :",versicolour_petal_length_max)
    print("Max petal width :",versicolour_petal_width_max)

    print("Minimum sepal length :",versicolour_sepal_length_min)
    print("Minimum sepal width :",versicolour_sepal_width_min)
    print("Minimum petal legth :",versicolour_petal_length_min)
    print("Minimum petal width :",versicolour_petal_width_min)
    print()

    print("Virginica Data :")
    print("Average sepal length :", virginica_sepal_length_avg/setosa_len)
    print("Average sepal width :",virginica_sepal_width_avg/setosa_len)
    print("Average petal length :",virginica_petal_length_avg/setosa_len)
    print("Average petal width :",virginica_petal_width_avg/setosa_len)

    print("Max sepal length :",virginica_sepal_length_max)
    print("Max sepal width :",virginica_sepal_width_max)
    print("Max petal length :",virginica_petal_length_max)
    print("Max petal width :",virginica_petal_width_max)

    print("Minimum sepal length :",virginica_sepal_length_min)
    print("Minimum sepal width :",virginica_sepal_width_min)
    print("Minimum petal legth :",virginica_petal_length_min)
    print("Minimum petal width :",virginica_petal_width_min)

if __name__ == '__main__':
    main()
