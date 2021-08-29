My solution to CMap Challenge(2016)
=======

https://cmap.topcoder.com/

In the KNearest Neighbors regression algorithm, the closest k number of training data points to the test point you’re trying to predict are averaged. I used the closest 5 training examples(k=5). The closest 5 nearest neighbors of the test data were determined using the euclidean metric and averaged.

I created 120 different KNearestNeighbors(KNN) regressors. Each KNN regressor used 30,000 training data points chosen at random(with replacement) from the 100,000 training examples. Also, each model only uses 300 of the 970 landmark genes. These 300 genes are randomly chosen(with replacement) for each model. 

The results of every KNN regression model are calculated and averaged to predict the expression levels for the other 11,350 genes. The approach is similar to random forest, except it uses KNN models instead of decision trees. I read that as a rule of thumb random forest regression uses about ⅓ of the possible features on each model, so I decided to try something similar with KNN and chose 300 genes.

Steps of the codes:
The main program cmapregression.py is written in python, specifically python 2.7. The code should work for python 3, although you may have to comment out, change or remove the extraneous print statements in line 19 and line 80. These are there for diagnostic purposes to make sure the code is working properly.

To compile and install scientific libraries needed for the program(numpy, scipy, pandas, and sklearn), compile.sh can be executed in a linux terminal. To run the program, run.sh can be executed after along with the appropriate file names or if you have the necessary libraries already installed, you can just directly execute cmapregression.py.

Lines 5 to 11 of cmapregression.py import the modules needed to run the code. The data is imported into data structure known as DataFrames so the data can be manipulated by the pandas and numpy libraries. Line 90 initiates the whole process, calling the Ensemble function. Ensemble takes in the number of KNN regression models you want to combine to produce a prediction. 

In this case, 120 models was chosen. The Ensemble function at line 73 has a loop that goes over all 120 models. For 120 times, a KNN regression model is produced(line 75) using the randomKNN() function. A prediction array is produced and each KNN model’s prediction is added to the array, so they can be averaged by dividing by the total number of regression models(line 82).

On line 61, randomKNN() takes a random sample of the data using the randomSample() function and fits it using a function provided by the open source library, scikitlearn.

This function is called KNeighborsRegressor. KNeighborsRegressors can create a search tree, so the closest neighbors can be found quickly KNeighborsRegressor’s output can be saved after it’s fitted, so this process does not need to be repeated. I didn’t do that here, but it saves time, so you don’t need to retrain data.

To take a random sample of the data for each KNN model, the function randomSample() on line 26 is used. It reads in the training data and separates the landmark genes into a DataFrame called train_df and the genes whose expression levels need predicting into a DataFrame called
label_df. It only uses 30,000 random training examples which are selected using a function called randomColumn. randomColumn uses a function from the numpy library to produce the list of 30,000 random training examples. 

randomGene uses the same function to select the 300 random landmark genes, which will be used in the regression model. These random numbers were produced by numpy’s pseudorandom number generator which was seeded at line 14, so the results could be reproducible. The random genes are saved in a list, so they can be used in the Ensemble function to make sure the testing only uses the landmark genes that model was trained on.

To sum up, Ensemble has a loop that 120 times calls randomKNN() to produce a KNN regression model that will be used to make a prediction about gene expression levels. randomKNN() produces its regression model by randomly sampling data using randomSample.

The predictions of the regression models are averaged and written to a csv.