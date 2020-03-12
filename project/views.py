from django.shortcuts import render
from django.http import HttpRequest ,HttpResponseRedirect
import pickle
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier


dataset=pd.read_csv('data.csv')
model=pickle.load(open('model_dtree.pkl','rb'))
x=dataset.drop(columns=[dataset.iloc[:,0].name,dataset.iloc[:,1].name,dataset.iloc[:,2].name,dataset.iloc[:,-1].name])
len=len(x.columns)

def home(request):
    dataset_cols=x.columns
    len_x=x.columns

    print(len_x)

    return render(request,'forms.html',{'dataset_cols':dataset_cols,'len_x':len_x})



def predict(request):
    j={}
    for i in x.columns:
        j[i]=request.POST.get(i)
    kam=pd.DataFrame([j])
    pred=model.predict(kam)
    print("the :model says", pred)
    #pred=0

    return render(request,'result.html',{'kam':kam,'pred':pred})


