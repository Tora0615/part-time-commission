# -*- coding: utf-8 -*-

# 迴文

mylist = []

while True:
    temp = input() #接收輸入到temp中
    if (temp == "-----"): #符合退出條件則退出
        break
    else:
        mylist.append(temp) #不符合則把temp存到mylist陣列中
    
for i in range(len(mylist)): # 有幾次輸入做幾次(不包含退出條件那行)
    words = mylist[i] #讀入第n次輸入的內容到words
    loop = True #設定是否有迴文的預設值為是
    total_len = len(words) #看這行字有多長
    for i in range(int(total_len/2)): #因為可以同時比較最前跟最後對應的字，因此處理次數為這行字總長的一半
        if(words[i] == words[total_len-1-i]): #如果字比對一樣
            continue #不做任何事，等下次迴圈繼續往中間比
        else: #如果比對有不一樣
            loop = False #迴文標籤標為否
            break #後續不用再比，可以直接退出
               
    # 如果比到最後都相同，回文標籤會如預設值一樣為是
    if (loop == True): #依照迴文標籤印出資料
        print("YES")
    else:
        print("NO")
                
#  可能情況分析
#
#  奇數個
#  ABCBA
#  01234 -> total_len = 5
#  
#  前後對應 : i & total_len-1-i 
#  ->i為0，對應為4 
#  ->i為1，對應為3 
#  ->i為2，對應為2 (自己)

#  偶數個
#  ABBA
#  0123 -> total_len = 4
#  
#  前後對應 : i & total_len-1-i 
#  ->i為0，對應為3
#  ->i為1，對應為2 
