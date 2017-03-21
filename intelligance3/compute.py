
import json
import numpy as np
import  cPickle as pickle
import xml.etree.cElementTree as ET
import pandas as pd
from pandas import DataFrame
from sklearn import metrics
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.neighbors import KNeighborsClassifier,KNeighborsRegressor
from sklearn.grid_search import GridSearchCV
from sklearn.svm import SVC, SVR
from sklearn import ensemble
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

import json
import time
from pylab import*
url="http://www.micex.ru/issrpc/marketdata/stock/index/history/" \
    "by_ticker/index_history_MICEXINDEXCF.csv?secid=MICEXINDEXCF&lang=ru"
url_r="http://www.micex.ru/issrpc/marketdata/stock/index/history/" \
      "by_ticker/index_history_MICEXBORRON.csv?secid=MICEXBORRON&lang=ru"
def fetchPreMarket(link,a,b):
    micex = pd.read_csv(link, sep=';', index_col=2, parse_dates = [2])
    t=micex[a].resample('Q', how=b)
    v=np.concatenate([t[-2:]])
    d=pd.DataFrame({'g':v})
    d.to_excel('/home/first/data/Java_study/marketplus/intelligance3/Data/m.xlsx')

    return d

while True:
    a = pd.read_excel('/home/first/data/Java_study/marketplus/intelligance3/Data/Data_mlv_rost_multireg_perebor.xlsx')
    b=pd.read_excel('/home/first/data/Java_study/marketplus/intelligance3/Data/Data_mlv_rost_multireg_perebor.xlsx')
    b.columns= \
        ['A1']+['A2']+['classA3']+['A4']+['classA5'] \
        +['A6']+['A7']+['classA8'] +['classA9']+['A10']+['classA11'] \
        +['classA12']+['B13']+['B14']+['B15']+['B16']+['B17']+['B18'] \
        +['classB19']+['classB20']+['classB21']+['classB22']+['A23'] \
        +['A24']+['classB25']+['classB26']
    a.columns= \
        ['A1']+['A2']+['classA3']+['A4']+['classA5'] \
        +['A6']+['A7']+['classA8'] +['classA9']+['A10']+['classA11'] \
        +['classA12']+['B13']+['B14']+['B15']+['B16']+['B17']+['B18'] \
        +['classB19']+['classB20']+['classB21']+['classB22']+['A23'] \
        +['A24']+['classB25']+['classB26']
    a.at[a['B13']==-1,'B13']='negative'
    a.at[a['B13']==1,'B13']='positive'
    a.at[a['B14']==-1,'B14']='negative'
    a.at[a['B14']==1,'B14']='positive'
    a.at[a['B15']==-1,'B15']='negative'
    a.at[a['B15']==1,'B15']='positive'
    a.at[a['B16']==-1,'B16']='negative'
    a.at[a['B16']==1,'B16']='positive'
    a.at[a['B17']==-1,'B17']='negative'
    a.at[a['B17']==1,'B17']='positive'
    a.at[a['B18']==-1,'B18']='negative'
    a.at[a['B18']==1,'B18']='positive'
    a.at[a['classB19']==-1,'classB19']='negative'
    a.at[a['classB19']==1,'classB19']='positive'
    a.at[a['classB20']==-1,'classB20']='negative'
    a.at[a['classB20']==1,'classB20']='positive'
    a.at[a['classB21']==-1,'classB21']='negative'
    a.at[a['classB21']==1,'classB21']='positive'
    a.at[a['classB22']==-1,'classB22']='negative'
    a.at[a['classB22']==1,'classB22']='positive'
    a.at[a['classB25']==-1,'classB25']='negative'
    a.at[a['classB25']==1,'classB25']='positive'
    a.at[a['classB26']==-1,'classB26']='negative'
    a.at[a['classB26']==1,'classB26']='positive'
    categorical_columns=[c for c in a.columns if a[c].dtype.name=='object']
    numerical_columns=[c for c in a.columns if a[c].dtype.name !='object']
    a=a.fillna(a.median(axis=0),axis=0)
    a['B13']=a['B13'].fillna('negative')
    a_describe=a.describe(include=[object])
    for c in categorical_columns:
        a[c]=a[c].fillna(a_describe[c]['top'])
    binary_columns=[c for c in categorical_columns if a_describe[c]['unique']==2]
    a.at[a['B13']=='negative', 'B13']=0
    a.at[a['B13']=='positive', 'B13']=1
    a_describe=a.describe(include=[object])
    for c in binary_columns[1:]:
        top=a_describe[c]['top']
        top_items=a[c]==top
        a.loc[top_items,c]=0
        a.loc[np.logical_not(top_items),c]=1
    a_numerical=a[numerical_columns]
    a_numerical=(a_numerical-a_numerical.mean())/a_numerical.std()
    a=pd.concat((a_numerical,a[binary_columns]),axis=1)
    a = pd.DataFrame(a, dtype=float)
    X=a.drop(['classA3'],axis=1)
    X=X.drop(['classA5'],axis=1)
    X=X.drop(['classA8'],axis=1)
    X=X.drop(['classA9'],axis=1)
    X=X.drop(['classA11'],axis=1)
    X=X.drop(['classA12'],axis=1)
    X=X.drop(['classB19'],axis=1)
    X=X.drop(['classB20'],axis=1)
    X=X.drop(['classB21'],axis=1)
    X=X.drop(['classB22'],axis=1)
    X=X.drop(['classB25'],axis=1)
    X=X.drop(['classB26'],axis=1)
    #X=X.drop(['A1'],axis=1)
    # #X=X.drop(['A2'],axis=1)
    X=X.drop(['A6'],axis=1)
    X=X.drop(['A7'],axis=1)
    #X=X.drop(['A4'],axis=1)
    X=X.drop(['A10'],axis=1)
    #X=X.drop(['A23'],axis=1)
    # #X=X.drop(['A24'],axis=1)
    # #X=X.drop(['B13'],axis=1)
    # #X=X.drop(['B14'],axis=1)
    # #X=X.drop(['B15'],axis=1)
    # #X=X.drop(['B16'],axis=1)
    #X=X.drop(['B17'],axis=1)
    #X=X.drop(['B18'],axis=1)
    neo=a['classA3']
    err=a['classA5']
    y2=a['classA8']
    y3=a['classA9']
    y6=a['classB19']
    y7=a['classB20']
    y8=a['classB21']
    y9=a['classB22']
    y10=a['classB25']
    y11=a['classB26']
    #testModels1=DataFrame()
    testModels=DataFrame()
    tmp={}
    tmp2={}
    tmp3={}
    tmp4={}
    X0_train,X0_test,y0_train,y0_test= \
        train_test_split(X,err,test_size=0.1,random_state=11)
    X_train,X_test,y_train,y_test= \
        train_test_split(X,neo,test_size=0.1,random_state=11)
    X1_train,X1_test,y1_train,y1_test= \
        train_test_split(X,y10,test_size=0.2,random_state=11)
    X2_train,X2_test,y2_train,y2_test= \
        train_test_split(X,y6,test_size=0.2,random_state=11)
    t0= fetchPreMarket(url,'CLOSE','min')
    a1=pd.read_excel('/home/first/data/Java_study/marketplus/intelligance3/Data/m.xlsx')
    indmin_rp=((a1.loc[1,'g']-a1.loc[0,'g'])/a1.loc[0,'g']) \
              /abs((a1.loc[1,'g']-a1.loc[0,'g'])/a1.loc[0,'g'])
    t1= fetchPreMarket(url,'CLOSE','max')
    a1=pd.read_excel('/home/first/data/Java_study/marketplus/intelligance3/Data/m.xlsx')
    indmax=a1.loc[1,'g']
    indmax_rp=((a1.loc[1,'g']-a1.loc[0,'g'])/a1.loc[0,'g']) \
              /abs((a1.loc[1,'g']-a1.loc[0,'g'])/a1.loc[0,'g'])
    t2= fetchPreMarket(url,'VALUE','min')
    a1=pd.read_excel('/home/first/data/Java_study/marketplus/intelligance3/Data/m.xlsx')
    volmin=a1.loc[1,'g']
    volmin_rp=((a1.loc[1,'g']-a1.loc[0,'g'])/a1.loc[0,'g']) \
              /abs((a1.loc[1,'g']-a1.loc[0,'g'])/a1.loc[0,'g'])
    t3= fetchPreMarket(url,'VALUE','max')
    a1=pd.read_excel('/home/first/data/Java_study/marketplus/intelligance3/Data/m.xlsx')
    volmax=a1.loc[1,'g']
    volmax_rp=((a1.loc[1,'g']-a1.loc[0,'g'])/a1.loc[0,'g']) \
              /abs((a1.loc[1,'g']-a1.loc[0,'g'])/a1.loc[0,'g'])
    t4= fetchPreMarket(url_r,'CLOSE','median')
    a1=pd.read_excel('/home/first/data/Java_study/marketplus/intelligance3/Data/m.xlsx')
    remed=a1.loc[1,'g']
    remed_rp=((a1.loc[1,'g']-a1.loc[0,'g'])/a1.loc[0,'g']) \
             /abs((a1.loc[1,'g']-a1.loc[0,'g'])/a1.loc[0,'g'])
    t5= fetchPreMarket(url_r,'CLOSE','min')
    a1=pd.read_excel('/home/first/data/Java_study/marketplus/intelligance3/Data/m.xlsx')
    remin=a1.loc[1,'g']
    remin_rp=((a1.loc[1,'g']-a1.loc[0,'g'])/a1.loc[0,'g']) \
             /abs((a1.loc[1,'g']-a1.loc[0,'g'])/a1.loc[0,'g'])
    #X=[indax,indmin_rp,indmin_rp]
    X1=pd.DataFrame({'A1':(volmax*0.014777/9.36-b['A1'].mean())
                          /b['A1'].std(),
                     'A2':(volmin*0.014777/9.36-
                           b['A2'].mean())/b['A2'].std(),
                     'A4':(indmax*0.014777/9.36-
                           b['A4'].mean())/b['A4'].std(),
                     'B13':volmax_rp,'B14':volmin_rp,'B15':indmax_rp,
                     'B16':indmin_rp,'B17':remed_rp,'B18':remin_rp,
                     'A23':(remed-
                            b['A23'].mean())
                           /b['A23'].std(),
                     'A24':(remin-b['A24'].
                            mean())/b['A24'].std()},index=[1],dtype=float)
    X1.at[X1['B13']==-1,'B13']=0
    X1.at[X1['B14']==-1,'B14']=0
    X1.at[X1['B15']==-1,'B15']=0
    X1.at[X1['B16']==-1,'B16']=0
    X1.at[X1['B17']==-1,'B17']=0
    X1.at[X1['B18']==-1,'B18']=0
    m5 = str('abs error and omission(c)')
    tmp4['Value'] = m5
    rfr=RandomForestRegressor(n_estimators=100, max_features ='sqrt')
    rfr.fit(X0_train,y0_train)
    #t=(X1['A1']-a_numerical['A1'].mean())/a_numerical['A1'].std()
    tmp4['predict']=rfr.predict(X1)*4534.15124+8959.386364
    value1=rfr.predict(X1)*4534.15124+8959.386364
    m2 = str('abs error and omission')
    tmp['Value'] = m2
    rfr=RandomForestRegressor(n_estimators=100, max_features ='sqrt')
    rfr.fit(X_train,y_train)
    #t=(X1['A1']-a_numerical['A1'].mean())/a_numerical['A1'].std()
    tmp['predict']=rfr.predict(X1)*2046.246446+3909.624242
    value2=rfr.predict(X1)*2046.246446+3909.624242
    m3=str('capital flight')
    tmp2['Value']=m3
    rf=ensemble.RandomForestClassifier(n_estimators=10,random_state=11)
    rf.fit(X1_train,y1_train)
    if rf.predict(X1)<1:
        tmp2['predict']='-'
    else:
        tmp2['predict']='+'
    if rf.predict(X1)<1:
        value3='-'
    else:
        value3='+'
    n_neighbors_array=(1,12) # maybe [1,2,3,4,5,6,7,8,9,10,11]
    knn=KNeighborsClassifier()
    grid=GridSearchCV(knn,param_grid=dict(n_neighbors=n_neighbors_array))
    grid.fit(X2_train,y2_train)
    #best_cv_err=1-grid.best_score_
    best_n_neighbors=grid.best_estimator_.n_neighbors
    # get error
    m1 = str('rise/fall abs error/omission')
    tmp3['Value'] = m1
    knn=KNeighborsClassifier(algorithm='auto',
                             leaf_size=30,metric='minkowski',
                             metric_params=None,n_neighbors=best_n_neighbors,
                             p=2,weights='uniform')
    knn.fit(X2_train,y2_train)

    if knn.predict(X1)<1:
        tmp3['predict']='fall'
    else:
        tmp3['predict']='rise'
    if knn.predict(X1)<1:
        value4='fall'
    else:
        value4='rise'


    #tt0=dfdf.dfdf('D:/work/data1/movomax.csv',"B1")
    #tt=pd.read_excel('D:\work\data1\movomax.csv')
    #ttt=(int(tt.values)-int(tt0.values))/int(tt0.values)
    #tt1=pd.read_excel('D:\work\data1\moinmax.csv', parse_cols="B")
    testModels=testModels.append([tmp4,tmp,tmp2,tmp3])
    print(testModels)

    #f = open(r'data.txt', 'wb')
    #obj = testModels.append([tmp4,tmp,tmp2,tmp3])
    #pickle.dump(obj, f)
    #f.close()
    #f = open(r'data.txt','rb')
    #obj=pickle.load(f)
    #print obj

    #f.close()
    #testModels.to_excel('/home/tatar/Yandex.Disk/Java_study/market/intelligance/Data/predict.xlsx')
    #print(testModels)
    #time.sleep(60)
    #break
    root=ET.Element("root")
    doc=ET.SubElement(root, "doc")
    ET.SubElement(doc, "field1").text=str(value1[0])
    ET.SubElement(doc, "field2").text=str(value2[0])
    ET.SubElement(doc, "field3").text=value3
    ET.SubElement(doc, "field4").text=value4
    tree=ET.ElementTree(root)
    tree.write("/home/first/data/Java_study/marketplus/data.xml")
    #time.sleep(10)
















