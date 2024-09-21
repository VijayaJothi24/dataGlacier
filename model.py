import pickle

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split

# Load the csv file
df = pd.read_csv("toy.csv")
print (df.head())
df.head()

A= df[["Length1Cm", "Width1Cm","Length2Cm", "Width2Cm"]]
B= df ["Toy Color"]

# Split the dataset into train and test
A_train,A_test,B_train,B_test = train_test_split(A,B,test_size= 0.35,random_state= 49)

#feature scaling
stsc = StandardScaler()
A_train =stsc.fit_transform(A_train)
A_test =stsc.transform(A_test)

# Instantiate the model
classifier_m = RandomForestClassifier()

# fit the model
classifier_m.fit(A_train,B_train)

# Make pickle file of the model
pickle.dump(classifier_m,open("model.pkl", "wb"))