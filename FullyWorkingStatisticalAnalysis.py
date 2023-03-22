import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sorc = input('Enter ("s")Singleplayer or ("c")Computer: ')

dt = 0
pt = 0
tie = 0
bb = 0
total = 0


s0 = 0
s1 = 0
s2 = 0

commonS = -1
successS = -1

if sorc == 'c':
    

    hypothesis = input("Please enter Strategy 1,2: ")
    while not hypothesis.isdigit() or int(hypothesis) not in [1,2]:
        hypothesis = input("Please enter Strategy 1,2: ")
    
    if int(hypothesis) == 1:
        data = pd.read_csv("simulation1.csv")
    elif int(hypothesis) == 2:
        data = pd.read_csv("simulation2.csv")
        
    df2=data.loc[data['Strategy'] == int(hypothesis),'Outcome']
   # print(df2)
    for i,j in df2.items():
        if j == 'Dealer':
            dt += 1
        if j == 'Player':
            pt += 1
        if j == 'Tie':
            tie += 1
        if j == 'Both Bust':
            bb += 1
              
    pdt=(dt / 1000)*100
    ppt=(pt/1000)*100
    ptie=(tie/1000)*100
    pbb=(bb/1000)*100

    data = {'Dealer Total':pdt,'Player Total':ppt,'Tie':ptie,'Both Bust':pbb}
    keys = list(data.keys())
    values = list(data.values())

    plt.ylabel("Percentage Wins ")
    plt.title("Strategy " + str(hypothesis))
    plt.bar(keys,values, color = 'blue')
    plt.show()
    


else: #singleplayer
    data = pd.read_csv("singleplayer.csv")
    chooseNametoAnalyse = input('Enter the Name you would like to analyse: ')
    
    df2=data.loc[data['Name'] == chooseNametoAnalyse,'Outcome']
    #print(df2)
    
    for i,j in df2.items():
        if j == 'Win':
            dt += 1
        if j == 'Loss':
            pt += 1
        if j == 'Tie':
            tie += 1
        if j == 'Both Bust':
            bb += 1
        total +=1
        
        
    
    pdt=(dt / total)*100
    ppt=(pt/total)*100
    ptie=(tie/total)*100
    pbb=(bb/total)*100

    dataa = {'Dealer Total':pdt,'Player Total':ppt,'Tie':ptie,'Both Bust':pbb}
    keys = list(dataa.keys())
    values = list(dataa.values())

    plt.ylabel("Percentage Wins ")
    plt.title("Strategy " )
    plt.bar(keys,values, color = 'blue')
   # plt.show()
    
    
    df2=data.loc[data['Name'] == chooseNametoAnalyse,'Strategy']
  
    #number of times user has played each strategy
    for i,j in df2.items():
        if j == 0:
            s0 += 1 
        if j == 1:
            s1 += 1
        if j == 2:
            s2 += 1
    
        total +=1
    
    if s0 > s1 and s0 > s2:
        commonS = 0
    elif s1 > s0 and s1 > s2:
        commonS = 1
    elif s2 > s1 and s2>s0:
        commonS = 2
    else:
        commonS = -1
        
    df3=data.loc[(data['Name'] == chooseNametoAnalyse) & (data['Outcome'] == 'Win'),'Strategy']    
    print(df3)
    
    s0 = 0
    s1 = 0
    s2 = 0
    
    for i,j in df3.items():
        if j == 0:
            s0 += 1 # s0 = strategy 0
        if j == 1:
            s1 += 1
        if j == 2:
            s2 += 1
    
        total +=1
    
    if s0 > s1 and s0 > s2:
        successS = 0
    elif s1 > s0 and s1 > s2:
        successS = 1
    elif s2 > s1 and s2>s0:
        successS = 2
    
    
    
    if (commonS  != -1):
        print('Modal analysis indicates that you are using strategy' , commonS , 'the most often and you are having the most success using strategy' , successS)
    else:
        print('Modal analysis indicates you are having the most success using strategy' , successS)