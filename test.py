import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import pydotplus
from IPython.display import Image
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandarScaler
import export_graphviz

sns.set()
%matplotlib inline

diamonds_pricerange = pd.cut(df.price,[300,1000,3000,5000,10000,19000],
label = ["supercheap","cheap","middle","expensive","superexpensive"])
diamonds_pricerange.value_counts()
x = dt.drop(["price"],axis - 1)
y = diamonds_pricerange
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 20)
dtt = DecisionTreeClassifier(criterion = "entropy",max_depth = 3, splitter = "best". random_state = 20)
dtt.fit(x_train,y_train)
DecisionTreeClassifier(criterion ="entropy",max_depth = 3,random_state = 20)