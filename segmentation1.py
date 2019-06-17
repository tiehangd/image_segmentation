# -*- coding: utf-8 -*-
import numpy as np;
#from numpy import insert;
import cv2;
import scipy;
from scipy import misc;
from scipy.misc import imread; 

imag=cv2.imread('F:\program file\canopy\Home_Work4\Peppers.jpg',0);

[row,col]=imag.shape;
row2=int(row*0.5);
col2=int(col*0.5);
row3=int(row2*0.5);
col3=int(col2*0.5);
row4=int(row3*0.5);
col4=int(col3*0.5);
row5=int(row4*0.5);
col5=int(col4*0.5);
row6=int(row5*0.5);
col6=int(col5*0.5);

imag_haar1=np.zeros(shape=(row,col));
haar_front1=np.zeros(shape=(row,row));
haar_back1=np.zeros(shape=(col,col));
haar_front2=np.zeros(shape=(row2,row2));
haar_back2=np.zeros(shape=(col2,col2));
haar_front3=np.zeros(shape=(row3,row3));
haar_back3=np.zeros(shape=(col3,col3));
haar_front4=np.zeros(shape=(row4,row4));
haar_back4=np.zeros(shape=(col4,col4));




##########################################
#first scale

for i in range(0,row):
    for j in range(0,row):
        if i<row2 and (j==2*i or j==2*i+1):
            haar_front1[i][j]=0.5;
        elif i>=row2 and j==2*(i-row2): 
            haar_front1[i][j]=-0.5;
        elif i>=row2 and j==2*(i-row2)+1:
            haar_front1[i][j]=0.5;


for i in range(0,col):
    for j in range(0,col):
        if i<col2 and (j==2*i or j==2*i+1):
            haar_back1[i][j]=0.5;
        elif i>=col2 and j==2*(i-col2): 
            haar_back1[i][j]=-0.5;
        elif i>=col2 and j==2*(i-col2)+1:
            haar_back1[i][j]=0.5;

haar_back1=haar_back1.transpose();

haar_front1=np.mat(haar_front1);
haar_back1=np.mat(haar_back1);

imag_haar1=haar_front1*imag*haar_back1;

imag_haar_abs1=np.zeros(shape=(row,col));
for i in range(0,row):
    for j in range(0,col):
        Num=abs(imag_haar1.item((i,j)));
        imag_haar_abs1[i][j]=Num;



imag_haar_edge1=np.zeros(shape=(row,col));
for i in range(0,row):
    for j in range(0,col):
        if i<row2 and j<col2:
             imag_haar_edge1[i][j]=0;
        else:  
            imag_haar_edge1[i][j]=imag_haar_abs1.item((i,j));



imag_haar_edge_compute1=np.linalg.inv(haar_front1)*imag_haar_edge1*np.linalg.inv(haar_back1);



##########################################
#second scale

imag2=np.zeros(shape=(row2,col2));
for i in range(0,row2):
    for j in range(0,col2):
        imag2[i][j]=imag_haar1.item((i,j));


for i in range(0,row2):
    for j in range(0,row2):
        if i<row3 and (j==2*i or j==2*i+1):
            haar_front2[i][j]=0.5;
        elif i>=row3 and j==2*(i-row3): 
            haar_front2[i][j]=-0.5;
        elif i>=row3 and j==2*(i-row3)+1:
            haar_front2[i][j]=0.5;
            


for i in range(0,col2):
    for j in range(0,col2):
        if i<col3 and (j==2*i or j==2*i+1):
            haar_back2[i][j]=0.5;
        elif i>=col3 and j==2*(i-col3): 
            haar_back2[i][j]=-0.5;
        elif i>=col3 and j==2*(i-col3)+1:
            haar_back2[i][j]=0.5;


haar_back2=haar_back2.transpose();

haar_front2=np.mat(haar_front2);
haar_back2=np.mat(haar_back2);

imag_haar2=haar_front2*imag2*haar_back2;
imag_haar_abs2=np.zeros(shape=(row2,col2));

for i in range(0,row2):
    for j in range(0,col2):
        Num=abs(imag_haar2.item((i,j)));
        imag_haar_abs2[i][j]=Num;



imag_haar_edge2=np.zeros(shape=(row2,col2));
for i in range(0,row2):
    for j in range(0,col2):
        if i<row3 and j<col3:
             imag_haar_edge2[i][j]=0;
        else:  
            imag_haar_edge2[i][j]=imag_haar_abs2.item((i,j));



imag_haar_edge_compute2=np.linalg.inv(haar_front2)*imag_haar_edge2*np.linalg.inv(haar_back2);



##########################################
#third scale

imag3=np.zeros(shape=(row3,col3));
for i in range(0,row3):
    for j in range(0,col3):
        imag3[i][j]=imag_haar2.item((i,j));


for i in range(0,row3):
    for j in range(0,row3):
        if i<row4 and (j==2*i or j==2*i+1):
            haar_front3[i][j]=0.5;
        elif i>=row4 and j==2*(i-row4): 
            haar_front3[i][j]=-0.5;
        elif i>=row4 and j==2*(i-row4)+1:
            haar_front3[i][j]=0.5;
            

for i in range(0,col3):
    for j in range(0,col3):
        if i<col4 and (j==2*i or j==2*i+1):
            haar_back3[i][j]=0.5;
        elif i>=col4 and j==2*(i-col4): 
            haar_back3[i][j]=-0.5;
        elif i>=col4 and j==2*(i-col4)+1:
            haar_back3[i][j]=0.5;


haar_back3=haar_back3.transpose();

haar_front3=np.mat(haar_front3);
haar_back3=np.mat(haar_back3);

imag_haar3=haar_front3*imag3*haar_back3;
imag_haar_abs3=np.zeros(shape=(row3,col3));

for i in range(0,row3):
    for j in range(0,col3):
        Num=abs(imag_haar3.item((i,j)));
        imag_haar_abs3[i][j]=Num;






imag_haar_edge3=np.zeros(shape=(row3,col3));
for i in range(0,row3):
    for j in range(0,col3):
        if i<row4 and j<col4:
             imag_haar_edge3[i][j]=0;
        else:  
            imag_haar_edge3[i][j]=imag_haar_abs3.item((i,j));



imag_haar_edge_compute3=np.linalg.inv(haar_front3)*imag_haar_edge3*np.linalg.inv(haar_back3);






##########################################
#fourth scale

imag4=np.zeros(shape=(row4,col4));
for i in range(0,row4):
    for j in range(0,col4):
        imag4[i][j]=imag_haar3.item((i,j));


for i in range(0,row4):
    for j in range(0,row4):
        if i<row5 and (j==2*i or j==2*i+1):
            haar_front4[i][j]=0.5;
        elif i>=row5 and j==2*(i-row5): 
            haar_front4[i][j]=-0.5;
        elif i>=row5 and j==2*(i-row5)+1:
            haar_front4[i][j]=0.5;
            


for i in range(0,col4):
    for j in range(0,col4):
        if i<col5 and (j==2*i or j==2*i+1):
            haar_back4[i][j]=0.5;
        elif i>=col5 and j==2*(i-col5): 
            haar_back4[i][j]=-0.5;
        elif i>=col5 and j==2*(i-col5)+1:
            haar_back4[i][j]=0.5;
            
            
haar_back4=haar_back4.transpose();            

haar_front4=np.mat(haar_front4);
haar_back4=np.mat(haar_back4);

imag_haar4=haar_front4*imag4*haar_back4;
imag_haar_abs4=np.zeros(shape=(row4,col4));

for i in range(0,row4):
    for j in range(0,col4):
        Num=abs(imag_haar4.item((i,j)));
        imag_haar_abs4[i][j]=Num




imag_haar_edge4=np.zeros(shape=(row4,col4));
for i in range(0,row4):
    for j in range(0,col4):
        if i<row5 and j<col5:
             imag_haar_edge4[i][j]=0;
        else:  
            imag_haar_edge4[i][j]=imag_haar_abs4.item((i,j));



imag_haar_edge_compute4=np.linalg.inv(haar_front4)*imag_haar_edge4*np.linalg.inv(haar_back4);



imag5=np.zeros(shape=(row5,col5));
for i in range(0,row5):
    for j in range(0,col5):
        imag5[i][j]=imag_haar4.item((i,j));



































imag=imag2;
row=row2;
col=col2;
#[row,col]=imag.shape;

labels=np.zeros((row,col),dtype=int);
count=int(2);

T1=2;

def labelregion(imag,labels,row,col,i,j):
    if i+1<row and j+1<col:
        if imag[i+1][j]-imag[i][j]<T1 and labels[i+1][j]==int(0):
            labels[i+1][j]=int(labels.item((i,j)));
            labelregion(imag,labels,row,col,i+1,j);
        if imag[i][j+1]-imag[i][j]<T1 and labels[i][j+1]==int(0):
            labels[i][j+1]=int(labels.item((i,j)));
            labelregion(imag,labels,row,col,i,j+1);
        if imag[i+1][j+1]-imag[i][j]<T1 and labels[i+1][j+1]==int(0):
            labels[i+1][j+1]=int(labels.item((i,j)));
            labelregion(imag,labels,row,col,i+1,j+1);
    if i+1>=row and j+1<col:
        if imag[i][j+1]-imag[i][j]<T1 and labels[i][j+1]==0:
            labels[i][j+1]=int(labels.item((i,j)));
            labelregion(imag,labels,row,col,i,j+1);
    if i+1<row and j+1>=col:
        if imag[i+1][j]-imag[i][j]<T1 and labels[i+1][j]==0:
            labels[i+1][j]=int(labels.item((i,j)));
            labelregion(imag,labels,row,col,i+1,j); 
            
    if i-1>=0 and j-1>=0:
        if imag[i-1][j]-imag[i][j]<T1 and labels[i-1][j]==int(0):
            labels[i-1][j]=int(labels.item((i,j)));
            labelregion(imag,labels,row,col,i-1,j);
        if imag[i][j-1]-imag[i][j]<T1 and labels[i][j-1]==int(0):
            labels[i][j-1]=int(labels.item((i,j)));
            labelregion(imag,labels,row,col,i,j-1);
        if imag[i-1][j-1]-imag[i][j]<T1 and labels[i-1][j-1]==int(0):
            labels[i-1][j-1]=int(labels.item((i,j)));
            labelregion(imag,labels,row,col,i-1,j-1);
    if i-1>=0 and j-1<0:
        if imag[i-1][j]-imag[i][j]<T1 and labels[i-1][j]==int(0):
            labels[i-1][j]=int(labels.item((i,j)));
            labelregion(imag,labels,row,col,i-1,j);
    if i-1<0 and j-1>=0:
        if imag[i][j-1]-imag[i][j]<T1 and labels[i][j-1]==int(0):
            labels[i][j-1]=int(labels.item((i,j)));
            labelregion(imag,labels,row,col,i,j-1);
        
        
                    
    return;
    
    
    
    

for i in range(0,row):
    for j in range(0,col):
        if i==0 and j==0:
            labels[i][j]=1;
            labelregion(imag,labels,row,col,i,j);
        elif labels[i][j]==0:
            labels[i][j]=count;
            labelregion(imag,labels,row,col,i,j);
            count=int(count+1);

print labels;

action=int(1);

adj_max=2000;

adj_r=np.zeros(shape=(count,adj_max),dtype=int);
cursor=np.zeros(shape=(count,1),dtype=int);
su_m=np.zeros(shape=(count,1));
num=np.zeros(shape=(count,1));
mean=np.zeros(shape=(count,1));
eliminated=np.zeros(shape=(count,1),dtype=int);



for i in range(0,row-1):
    for j in range(0,col-1):
        if labels.item((i,j+1))!=labels.item((i,j)):
            adj_r[labels.item((i,j))][cursor.item((labels.item((i,j)),0))]=labels.item((i,j+1));
            cursor[labels.item((i,j))][0]=cursor.item((labels.item((i,j)),0))+1;
        if labels.item((i+1,j))!=labels.item((i,j)):
            adj_r[labels.item((i,j))][cursor.item((labels.item((i,j)),0))]=labels.item((i+1,j));
            cursor[labels.item((i,j))][0]=cursor.item((labels.item((i,j)),0))+1;
        if labels.item((i+1,j+1))!=labels.item((i,j)):
            adj_r[labels.item((i,j))][cursor.item((labels.item((i,j)),0))]=labels.item((i+1,j+1));
            cursor[labels.item((i,j))][0]=cursor.item((labels.item((i,j)),0))+1;

for i in range(0,count):
    array1=np.unique(adj_r[i]);
    if len(array1)==1:
        continue;
    for j in range(0,cursor[i][0]):
        if j<len(array1)-1:
            adj_r[i][j]=array1[j+1];
        else:
            adj_r[i][j]=0;
    cursor[i][0]=len(array1)-1;


for i in range(0,row):
    for j in range(0,col):
        su_m[labels.item((i,j))][0]=su_m.item((labels.item((i,j)),0))+imag.item((i,j));
        num[labels.item((i,j))][0]=num.item((labels.item((i,j)),0))+1;
        

for i in range(0,count):
    if int(num.item((i,0)))!=0:
        mean[i][0]=su_m.item((i,0))/num.item((i,0));





stop_sign=0;
count_total=0;
while action==int(1):
    action=0;
    if stop_sign==int(1):
        break;
    
    for i in range(0,count):
        if count_total>60000:
            stop_sign=int(1);
            break;
        if int(eliminated.item((i,0)))==int(1):
             continue;
        temp=0;
        while int(adj_r.item((i,temp)))!=int(0):
            if eliminated.item((adj_r.item((i,temp)),0))==int(1):
                temp=temp+1;
                continue;
            
            if mean.item((i,0))-mean.item((adj_r.item((i,temp)),0))<T1 and int(mean.item((i,0)))!=0 and int(mean.item((adj_r.item((i,temp)),0)))!=0:
                action=int(1);
                count_total=count_total+1;
                merged=i;
                elimed=adj_r.item((i,temp));
                print i;
                for p in range(0,row):
                     for q in range(0,col):
                         if int(labels.item((p,q)))==int(elimed):
                             labels[p][q]=i;
                
                for p in range(0,count):
                    for q in range(0,cursor[p][0]):
                        if adj_r[p][q]==elimed:
                             adj_r[p][q]=merged;
                
                
                for p in range(0,cursor[elimed][0]):
                    if int(adj_r[elimed][p])==int(0):
                        break;
                    unique=int(1);
                    for q in range(0,cursor.item((i,0))):
                         if int(adj_r.item((elimed,p)))==int(adj_r.item((i,q))):
                             unique=int(0);
                             
                    if unique==int(1):        
                         adj_r[i][cursor[i][0]]=adj_r.item((elimed,p));
                         cursor[i][0]=cursor.item((i,0))+1;
                         adj_r[elimed][p]=int(0);
                
                array2=np.unique(adj_r[i]);
                if len(array2)!=1:
                   for j in range(0,cursor[i][0]):
                      if j<len(array2)-1:
                         adj_r[i][j]=array2[j+1];
                      else:
                         adj_r[i][j]=0;
                         cursor[i][0]=len(array2)-1;
                    
                
                su_m[i][0]=su_m.item((i,0))+su_m.item((adj_r.item((i,temp)),0));
                su_m[adj_r.item((i,temp))][0]=0;
                num[i][0]=num.item((i,0))+num.item((adj_r.item((i,temp)),0));   
                num[adj_r.item((i,temp))][0]=0;  
                if num.item((i,0))!=0:
                     mean[i][0]=su_m.item((i,0))/num.item((i,0));
                     
                eliminated[elimed][0]=int(1);   
            temp=temp+1;





print labels;


segmentation=np.zeros((row,col));
for i in range(0,row-1):
    for j in range(0,col-1):
        if labels.item((i,j))!=labels.item((i+1,j)) or labels.item((i,j))!=labels.item((i,j+1)) or labels.item((i,j))!=labels.item((i+1,j+1)):
            segmentation[i][j]=0;
        else:
            segmentation[i][j]=255;




cv2.imwrite('Segm.png',segmentation);





