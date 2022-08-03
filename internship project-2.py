#Recognizing Handwritten Digits with scikit-learn
#Hypothesis to be tested : The Digits data set of scikit-learn library provides numerous data-sets that are useful for testing many problems of data analysis and prediction of the results. Some Scientist claims that it predicts the digit accurately 95% of the times. Perform data Analysis to accept or reject this Hypothesis.
#Code:------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier 
a=pd.read_csv('train.csv')
#print(a.shape)
x=a.iloc[:,1:].values
#print(x.shape)
y=a.iloc[:,0:].values
#print(y.shape)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=9)

#print(x_train.shape)
from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier()
dtc.fit(x_train,y_train)
#print(y_test[100])
plt.imshow(x_test[100].resahpe(28,28))
print(dtc.predict(x_test[100].reshape(1,784)))
plt.show()

#Conclusion:---------------------------------------------
#Given the large quantity of elements contained in the Digits dataset, we certainly obtain a very effective model, i.e., one that’s capable of recognizing with good certainty the handwritten number.

#I am thankful to mentors at https://internship.suvenconsultants.com for providing awesome problem statements and giving many of us a Coding Internship Experience. Thank you www.suvenconsultants.com
