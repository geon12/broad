"""
Uses Random KNN to predict gene expression levels
"""
#libraries to import
import numpy as np

import pandas as pd

import sys

from sklearn import neighbors

#seed pseudo-random number generator for repeatable results
np.random.seed(7)

random_pool = []


print "working"

train_file = sys.argv[1]
test_file = sys.argv[2]
out_file = sys.argv[3]


def randomSample():
    #choose size of model
    rand_col = randomColumn(30000)    
       
    train_df = pd.read_csv(train_file,nrows=970, header=None, usecols=rand_col)
    label_df = pd.read_csv(train_file,skiprows=970, header=None, usecols=rand_col)
       
    train_df = train_df.transpose()
    label_df = label_df.transpose()
    
    #chose how many genes are used in each model
    rand_gen = randomGene(300)
    random_pool.append(rand_gen)
    train_df = train_df[rand_gen]
    
    #print("working")
    
    return train_df, label_df
    
#Pick random sample nummbers    
def randomColumn(sample_size):
    rand_samp = np.random.randint(0, high=100000, size=sample_size)
    rand_samp = rand_samp.tolist()
    
    return rand_samp

#pick random landmark genes
def randomGene(gene_num):
    rand_gene = np.random.randint(0, high=970, size=gene_num)
    rand_gene = rand_gene.tolist()
    
    return rand_gene


#Create a Knearest neighbor model using random data/features
def randomKNN():
    
    trains_df, labels_df = randomSample()
    reg = neighbors.KNeighborsRegressor()
    reg = reg.fit(trains_df, labels_df)
    return reg

#Import Test Data
test_df = pd.read_csv(test_file, header=None)
test_df = test_df.transpose()
  
#Bring Ensemble together by averaging predictions for each knn model
def Ensemble(num_reg):
    for x in range(0,num_reg):
        knn = randomKNN()
        if (x==0):
            pred = knn.predict(test_df[random_pool[x]])
        else:
            pred += knn.predict(test_df[random_pool[x]])
        print str(x)
            
    pred = np.true_divide(pred, float(num_reg))
    pred = pred.transpose()
    
    return pred



#Implement prediction    
prediction = Ensemble(120)

#Save to CSV file
prediction = np.asarray(prediction)
np.savetxt(out_file, prediction, delimiter=",", fmt='%.3f')