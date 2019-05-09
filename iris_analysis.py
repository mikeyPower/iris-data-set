# Predict the class of the flower based on available attributes.

import math
import pandas
import sklearn
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Function to find common stats about plant species
# Parameter: a 2-d array consisting of the species of the plant
# Returns: a 1-d array of common statistical information
def summary_stats(species):
    # Initalize some varialbles

    size = len(species)

    sepal_length_avg=0
    sepal_width_avg=0
    petal_length_avg=0
    petal_width_avg=0

    # Shouldn't initalize the below variables to 0 as 0 may not be part of the population giving us incorrect results so initalize to first relevant data point
    sepal_length_max=species[0][0]
    sepal_width_max=species[0][1]
    petal_length_max=species[0][2]
    petal_width_max=species[0][3]

    sepal_length_min=species[0][0]
    sepal_width_min=species[0][1]
    petal_length_min=species[0][2]
    petal_width_min=species[0][3]

    type =''
    if (species[0][-1]==1.0):
        type = 'Iris Setosa'

    elif(species[0][-1]==2.0):
        type = 'Iris Versicolor'
    else:
        type = 'Iris Virginica'


    # Calculate the average, min and max of iris_setosa and other species
    for i in species:
        sepal_length_avg+=i[0]
        sepal_width_avg+=i[1]
        petal_length_avg+=i[2]
        petal_width_avg+=i[3]

        if(sepal_length_max < i[0]):
           sepal_length_max=i[0]
        elif(sepal_length_min > i[0]):
           sepal_length_min=i[0]



        if(sepal_width_max < i[1]):
           sepal_width_max=i[1]
        elif(sepal_width_min > i[1]):
           sepal_width_min=i[1]


        if(petal_length_max < i[2]):
           petal_length_max=i[2]
        elif(petal_length_min > i[2]):
           petal_length_min=i[2]



        if(petal_width_max < i[3]):
           petal_width_max=i[3]
        elif(petal_width_min > i[3]):
           petal_width_min=i[3]

    stats = [sepal_length_avg/size,sepal_width_avg/size,petal_length_avg/size,petal_width_avg/size,
        sepal_length_max,sepal_width_max,petal_length_max,petal_width_max,
        sepal_length_min,sepal_width_min,petal_length_min,petal_width_min]
    print(type +" Data :")
    print("Number of Samples :", size)
    print("Average sepal length :", stats[0])
    print("Average sepal width :" ,stats[1])
    print("Average petal length :",stats[2])
    print("Average petal width :",stats[3])

    print("Max sepal length :",stats[4])
    print("Max sepal width :",stats[5])
    print("Max petal length :",stats[6])
    print("Max petal width :",stats[7])

    print("Minimum sepal length :",stats[8])
    print("Minimum sepal width :",stats[9])
    print("Minimum petal legth :",stats[10])
    print("Minimum petal width :",stats[11])

    print("Standard Deviation sepal length :",standard_dev(species,stats[0],0))
    print("Standard Deviation sepal width :",standard_dev(species,stats[1],1))
    print("Standard Deviation petal legth :",standard_dev(species,stats[2],2))
    print("Standard Deviation petal width :",standard_dev(species,stats[3],3))

    print()

    return stats

# Function to calculate the correlation between to sets of data
# Parameters : 2-d array, int, int
# Returns : float
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



# Function to calculate the standard deviation
# Parameter : 2-d array, float, int
# Returns : float
def standard_dev(flower,mean,column):

    # Calculate the standard deviation by summing the each value from subtracted by the mean and squaring the result
    total = 0.0
    sum=0.0
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
    flower_data_name=[]
    iris_setosa=[]
    iris_versicolour=[]
    iris_virginica=[]

    # Remove known errors from data
    #errors = []
    #errors.append(lines[34])
    #errors.append(lines[37])
    #lines.pop(34)
    #lines.pop(37)

    # Loop through all lines except the last line as it's empty
    for line in lines[:-1]:

        # For each line remove any trailing whitespace e.g. newline characters \n and split it by , creating a list
        row = line.rstrip().split(',')

        # Want to keep the original data set but with the numbers converted to floats and as well as the class name in string
        flower_data_name.append([float(x) for x in row[:-1]])
        flower_data_name[-1]+=[row[-1]]

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


    # Get summary of stats regarding each species
    summary_stats(iris_setosa)
    summary_stats(iris_versicolour)
    summary_stats(iris_virginica)


    # Find the correlation from species to each numeric attribute of the plant species
    print("Correlations :")
    print("Correlation between Species and Sepal Length :",correlation(flower_data,0,4))
    print("Correlation between Species and Sepal Width :",correlation(flower_data,1,4))
    print("Correlation between Species and Petal Length :",correlation(flower_data,2,4))
    print("Correlation between Species and Petal Width :",correlation(flower_data,3,4))

    print()

    # hist plots
    dataset = pandas.DataFrame(flower_data_name)
    #print(dataset)
    dataset.hist()
    #plt.show()
    plt.savefig('hist_plot.png')

    scatter_matrix(dataset)
    plt.savefig('scatter_plot.png')


    # Split-out validation dataset
    array = dataset.values

    # Everything but the last column stored as a 2d array
    X = array[:,0:4]

    # Just the last column stored as a 1d array
    Y = array[:,4]

    # We will split the loaded dataset into two, 80% of which we will use to train our models and 20% that we will hold back as a validation dataset.
    validation_size = 0.20
    seed = 7
    X_train, X_validation, Y_train, Y_validation = sklearn.model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)


    # Test options and evaluation metric
    seed = 7
    scoring = 'accuracy'

    # Spot Check Algorithms
    models = []
    models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
    models.append(('LDA', LinearDiscriminantAnalysis()))
    models.append(('KNN', KNeighborsClassifier()))
    models.append(('CART', DecisionTreeClassifier()))
    models.append(('NB', GaussianNB()))
    models.append(('SVM', SVC(gamma='auto')))

    # evaluate each model in turn
    results = []
    names = []
    for name, model in models:
        kfold = sklearn.model_selection.KFold(n_splits=10, random_state=seed)
        cv_results = sklearn.model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
        results.append(cv_results)
        names.append(name)
        msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
        print(msg)


    # Compare Algorithms
    fig = plt.figure()
    fig.suptitle('Algorithm Comparison')
    ax = fig.add_subplot(111)
    plt.boxplot(results)
    ax.set_xticklabels(names)
    plt.savefig('algorithm_comparison.png')


    # Make predictions on validation dataset
    # We can run the KNN model directly on the validation set and summarize the results as a final accuracy score,
    # a confusion matrix and a classification report.
    knn = KNeighborsClassifier()
    knn.fit(X_train, Y_train)
    predictions = knn.predict(X_validation)
    print()
    print("KNN model")
    print("Accuracy Score :",accuracy_score(Y_validation, predictions))
    print()
    print("Confusion Matrix :\n",confusion_matrix(Y_validation, predictions))
    print()
    print("Classification Report :\n",classification_report(Y_validation, predictions))

if __name__ == '__main__':
    main()
