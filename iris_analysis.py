# Predict the class of the flower based on available attributes.

import math


# Function to calculate the correlation between to sets of data
def correlation(data, column_a, column_b):

    # Find the mean of the two columns we are going to get the correlation for
    sum_x=0.0
    sum_y=0.0
    for i in data:
        sum_x+=i[column_a]
        sum_y+=i[column_b]

    avg_x = sum_x/len(data)
    avg_y = sum_y/len(data)

    # Calculate the a - mean & b - mean for all the values in the list
    a=[]
    b=[]
    for i in data:
        a.append(i[column_a]-avg_x)
        b.append(i[column_b]-avg_y)

    # Calculate a*b, a^2 & b^2 for all values in both columns
    a_b=0.0
    a_squared=0.0
    b_squared=0.0
    for i in range(len(data)):
        a_b+=a[i]*b[i]
        a_squared+=a[i]*a[i]
        b_squared+=b[i]*b[i]

    # Work out the square root of a^2 x b^2
    a_b_sqrt = math.sqrt(a_squared*b_squared)

    # Divide a*b to the answer above
    return(a_b/a_b_sqrt)




def standard_dev(flower,mean,column):

    # Calculate the standard deviation by summing the each value from subtracted by the mean and squaring the result
    total = 0.0
    for i in flower:

        sum=i[column]-mean

        square=sum*sum
        total+=square

    # divide the toal by the population
    s_dev = total/len(flower)

    # return the square root to get the standard deviation
    return math.sqrt(s_dev)



def main():

    # Open the file
    file = open("iris.data", "r")

    # read each line of the file and put it into a list
    lines = file.readlines()

    # Initalize some variables
    flower_data =[]
    iris_setosa=[]
    iris_versicolour=[]
    iris_virginica=[]

    # Remove known errors from data
    errors = []
    errors.append(lines[34])
    errors.append(lines[37])
    lines.pop(34)
    lines.pop(37)

    # Loop through all lines except the last line as it's empty
    for line in lines[:-1]:

        # For each line remove any trailing whitespace e.g. newline characters \n and split it by , creating a list
        row = line.rstrip().split(',')

        # Seperate each list based on the species
        if(row[4]=="Iris-setosa"):
            iris_setosa.append([float(x) for x in row[:-1] + [1.0]])

            # Add some sort of indicator for each species e.g. 1.0 for iris setosa etc..
            flower_data.append([float(x) for x in row[:-1] + [1.0]])
        elif(row[4]=="Iris-versicolor"):

            iris_versicolour.append([float(x) for x in row[:-1] + [2.0]])
            flower_data.append([float(x) for x in row[:-1] + [2.0]])
        else:
            iris_virginica.append([float(x) for x in row[:-1] + [3.0]])
            flower_data.append([float(x) for x in row[:-1] + [3.0]])

    # calculate size of population for each species
    setosa_len = len(iris_setosa)
    versicolour_len = len(iris_versicolour)
    virginica_len = len(iris_virginica)

    # Initalize some varialbles
    setosa_sepal_length_avg=0
    setosa_sepal_width_avg=0
    setosa_petal_length_avg=0
    setosa_petal_width_avg=0

    # Shouldn't initalize the below variables to 0 as 0 may not be part of the population giving us incorrect results so initalize to first relevant data
    setosa_sepal_length_max=iris_setosa[0][0]
    setosa_sepal_width_max=iris_setosa[0][1]
    setosa_petal_length_max=iris_setosa[0][2]
    setosa_petal_width_max=iris_setosa[0][3]

    setosa_sepal_length_min=iris_setosa[0][0]
    setosa_sepal_width_min=iris_setosa[0][1]
    setosa_petal_length_min=iris_setosa[0][2]
    setosa_petal_width_min=iris_setosa[0][3]

    # Calculate the average, min and max of iris_setosa and other species
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

    print("Standard Deviation sepal length :",standard_dev(iris_setosa,setosa_sepal_length_avg/setosa_len,0))
    print("Standard Deviation sepal width :",standard_dev(iris_setosa,setosa_sepal_width_avg/setosa_len,1))
    print("Standard Deviation petal legth :",standard_dev(iris_setosa,setosa_petal_length_avg/setosa_len,2))
    print("Standard Deviation petal width :",standard_dev(iris_setosa,setosa_petal_width_avg/setosa_len,3))

    print()

    print("Versicolour Data :")
    print("Average sepal length :", versicolour_sepal_length_avg/versicolour_len)
    print("Average sepal width :",versicolour_sepal_width_avg/versicolour_len)
    print("Average petal length :",versicolour_petal_length_avg/versicolour_len)
    print("Average petal width :",versicolour_petal_width_avg/versicolour_len)

    print("Max sepal length :",versicolour_sepal_length_max)
    print("Max sepal width :",versicolour_sepal_width_max)
    print("Max petal length :",versicolour_petal_length_max)
    print("Max petal width :",versicolour_petal_width_max)

    print("Minimum sepal length :",versicolour_sepal_length_min)
    print("Minimum sepal width :",versicolour_sepal_width_min)
    print("Minimum petal legth :",versicolour_petal_length_min)
    print("Minimum petal width :",versicolour_petal_width_min)

    print("Standard Deviation sepal length :",standard_dev(iris_versicolour, versicolour_sepal_length_avg/versicolour_len,0))
    print("Standard Deviation sepal width :",standard_dev(iris_versicolour, versicolour_sepal_width_avg/versicolour_len,1))
    print("Standard Deviation petal legth :",standard_dev(iris_versicolour, versicolour_petal_length_avg/versicolour_len,2))
    print("Standard Deviation petal width :",standard_dev(iris_versicolour, versicolour_petal_width_avg/versicolour_len,3))

    print()

    print("Virginica Data :")
    print("Average sepal length :", virginica_sepal_length_avg/virginica_len)
    print("Average sepal width :",virginica_sepal_width_avg/virginica_len)
    print("Average petal length :",virginica_petal_length_avg/virginica_len)
    print("Average petal width :",virginica_petal_width_avg/virginica_len)

    print("Max sepal length :",virginica_sepal_length_max)
    print("Max sepal width :",virginica_sepal_width_max)
    print("Max petal length :",virginica_petal_length_max)
    print("Max petal width :",virginica_petal_width_max)

    print("Minimum sepal length :",virginica_sepal_length_min)
    print("Minimum sepal width :",virginica_sepal_width_min)
    print("Minimum petal legth :",virginica_petal_length_min)
    print("Minimum petal width :",virginica_petal_width_min)

    print("Standard Deviation sepal length :",standard_dev(iris_virginica,virginica_sepal_length_avg/virginica_len,0))
    print("Standard Deviation sepal width :",standard_dev(iris_virginica,virginica_sepal_width_avg/virginica_len,1))
    print("Standard Deviation petal legth :",standard_dev(iris_virginica,virginica_petal_length_avg/virginica_len,2))
    print("Standard Deviation petal width :",standard_dev(iris_virginica,virginica_petal_width_avg/virginica_len,3))

    print()


    print("Correlation between Species and Sepal Length :",correlation(flower_data,0,4))
    print("Correlation between Species and Sepal Width :",correlation(flower_data,1,4))
    print("Correlation between Species and Petal Length :",correlation(flower_data,2,4))
    print("Correlation between Species and Petal Width :",correlation(flower_data,3,4))
if __name__ == '__main__':
    main()
