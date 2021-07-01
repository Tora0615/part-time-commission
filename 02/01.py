# -*- coding: utf-8 -*-


a = input() #先接收要做幾次
mylist = [] #存結果用

#對應迴圈次數接收輸入
for i in range(int(a)): #a輸入是字串，轉成int
    temp = input() #輸入
    
    #利用切割函式切割(預設從空格切)，切完覆蓋原本temp
    temp = temp.split() # 100 2 切完會變成 ['100', '2']
    
    try :
        cal_ans = int(temp[0])*int(temp[1]) #嘗試換成int計算
        mylist.append('Total amount: ' + str(cal_ans)) #沒問題存入list   
    
    #只有一個數字，切出來長['100']，讀temp[1]的值會有IndexError的錯誤
    except IndexError: 
        mylist.append('Please type a number.') #結果存入list
        
    #不可換成int的值嘗試換成int，會有ValueError的錯誤
    except ValueError:
        mylist.append('You should type an integer.') #結果存入list

    
# 用迴圈印出
for i in range(int(a)):
    print(mylist[i])


