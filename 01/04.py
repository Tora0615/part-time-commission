# -*- coding: utf-8 -*-

#計算字串間隔距離

mylist = [] #空陣列
head = -1 #指定字的預設序列為-1。因為電腦從0開始數，用以區別目前位置用


words = input().upper() #讀入長句子，並同時全轉為大寫
key = input().upper() #讀入關鍵字，並轉為大寫


for i in range(len(words)): #長句子從頭掃到尾
    if (words[i] == key): #如果字符合關鍵字
        if (head == -1): #如果關鍵字位置還沒設定
            head = i #設為現在位置
        else: #曾經設定過了
            mylist.append(str(i-head)) #把這個位置與上個位置的長度差先存到陣列
            head = i #把關鍵字開頭位置設到現在位置


for i in range(len(mylist)): #讀所有存起來的間隔長度
    if (i == len(mylist)-1): #如果是最後一個要印出來的元素
        print(mylist[i],end = '') #印現在讀到的長度紀錄就好
    else: #不是最後一個
        print(mylist[i]+" ",end = '') #印 現在讀到的長度紀錄 + 一個空格

# 測試資料
# ABCDAAEFeDaBDCBCBcBCbCBBd

# 註 : end='' 代表印出來結果不換行