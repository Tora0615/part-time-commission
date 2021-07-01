# -*- coding: utf-8 -*-

#太鼓達人


# game 是第一行代表遊戲音符出現的順序
# player 是第二行代表玩家打擊的順序
game = input()
player = input()


# 設定初值皆為0，
# combo是遊戲當下連續打擊數
# score是總分，Max_combo是這局最大連續打擊數
combo = 0
score = 0
Max_combo = 0


# 設個為game字串長度的迴圈
for i in range(len(game)):
    if(game[i]=='-'): #如果遊戲音符出現"-"，做什麼都不影響分數 
        continue  #因此跳過"這次"迴圈
    elif game[i] == player[i]: #當玩家跟譜是一樣的
        combo = combo + 1 #當下連續打擊數+1 
        score = score + combo*100 #並累加分數
    else: #若打錯
        if (combo > Max_combo): #檢查先一次連續打擊數是否超過之前其他次最高的紀錄
            Max_combo = combo #有超過的話，最高紀錄更新
        combo = 0 #因為打錯，當下combo要歸零

# 印出結果。
# 由於score 和 Max_combo 是數字，不能直接跟空格" "合併，因此先轉成字串
print(str(score)+" "+str(Max_combo))



# 要注意的打擊狀況 : 
# 有出現 "-" 要注意
# 有他不管做什麼都不影響其他
#
#
#      RRRR-RRRR
#      BRRRRRRRb
# 打對  ^^^ ^^^   
# 連擊  123 456
# 分數  100+200+300+400+500+600
#





