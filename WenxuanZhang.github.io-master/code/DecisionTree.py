
# coding: utf-8

# In[7]:

from sklearn.externals.six import StringIO  
import pydot
from sklearn import tree
from sklearn.datasets import load_iris
import numpy as np

def generate(n):
    b =[]
    for i in range(n):
        x=[np.random.randint(2),
           np.random.randint(2),
           np.random.randint(2),
           np.random.randint(5)]
        b.append(x)
    return np.array(b)

n=50
X=generate(n)
Y=np.random.randint(2,size=n)
    
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data) 
graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
graph.write_pdf("ad.pdf") 
clf.predict([1,1,0,1])


# In[ ]:



