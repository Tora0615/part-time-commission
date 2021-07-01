# -*- coding: utf-8 -*-

#字串中學堂

mylist = [] #宣告空的陣列

while True:  #重複執行
    temp = input() #讀入並存到temp
    if (temp == '0'):  #若temp符合跳出條件
        break  #則跳出迴圈
    #若沒跳出，繼續執行以下
    temp_split = temp.split(' ') #將讀入的內容，以空格進行分割。
    # 分割好的格式會像['Have','1']
    mylist.append(temp_split) #並把分割好的內容存到mylist中
    # mylist 的格式會像[['day','4'],['a','2'],['Have','1'],['good','3']]
    
    
    
total_len = len(mylist) #取得總長
for i in range (total_len): #假設總長為4，就要按照順序分四次把內容印出來
    for j in range(total_len): #如何知道這次要順序幾的字呢? 四個字指定的順序都看一下
        
        #把四個字指定的順序都看一下 與 這次要順序幾 比對
        #假設i為0，指定的順序就是i+1(因為指定順序從1開始)。看過所有指定順序找到現在要的
        if (str(i+1) == mylist[j][1]): #符合條件
            print (mylist[j][0],end='') #印出字
            if (str(total_len) == mylist[j][1]): #判斷是否到句尾
                print (".",end='') #到句尾，字後面印逗號，不印空格
            else: #不是句尾
                print (" ",end='') #字後面印空格，不印句號

# 註 : end='' 代表印出來結果不換行