# -*- coding: utf-8 -*-

import math
import operator

#題目給的函式，v1 v2 可傳入 list
def dot_product2(v1, v2):
    return sum(map(operator.mul, v1, v2)) #返回v1 * v2
    #map(函數，資料) --> 會把資料丟到函數做映射

#題目給的函式，v1 v2 可傳入 list
def cosineSimilarity(v1, v2):
    # v1 放入doc, v2 放 query
    prod = dot_product2(v1, v2)
    len1 = math.sqrt(dot_product2(v1, v1))
    len2 = math.sqrt(dot_product2(v2, v2))
    return prod/(len1 * len2)


docs = input() #文件數量
word_set = set() #空的set
doc_list = [] #存所有doc內容

# 做幾次
for i in range(int(docs)):
    temp = input().lower() #輸入轉小寫給temp
    doc_list.append(temp.split(':')[1].split()) #把一句話拆成詞存到list中，後面比對用
    word_set = word_set | set(temp.split(':')[1].split()) #找出所有不重複的詞
    


# 把不重複詞的set轉list。有唯一序，可拿來比對
word_list = list(word_set)
word_list_len = len(list(word_set))



# 初始化二維list(存結果用)
vector_list = []
for i in range (int(docs)):
    vector_list.append([])


# 把這些doc關鍵字所出現次數填入list
for i in range(int(docs)): #代表現在是哪個doc
    for j in range(word_list_len): #把不重複詞list一個一個取出
        if word_list[j] in doc_list[i]:  #看取出的詞有沒有在對應list中
            vector_list[i].append(1)
        else:
            vector_list[i].append(0)


# 查詢
query_words = input()
query_words = query_words.split() #空格切割

# 跟上面類似，把query_words比對結果存到list中 (詳情看最後解說)
query_vector=[]
for j in range(word_list_len): #把不重複詞list一個一個取出
        if word_list[j] in query_words:  #看取出的詞有沒有在對應list中
            query_vector.append(1)
        else:
            query_vector.append(0)


best_index = -1  #存比對成果最好那個的順序
best_score = -1  #存最好的成績

# 把所有doc比對結果跟query做運算
for i in range(int(docs)):
    # cosineSimilarity(v1, v2) : v1 放入doc, v2 放 query
    temp_score = cosineSimilarity(vector_list[i], query_vector)
    temp_score = round(temp_score,4) #四捨五入
    print("doc"+ str(i+1) +" " + str(temp_score)) #印出
    
    #看這次分數有沒有比以前最好的高
    if temp_score > best_score : 
        best_score = temp_score
        best_index = i
    

# 印best
print('best:doc'+str(best_index+1))




#測試資料(要一行一行輸入，不然會出錯)
'''
7
doc1:My name is sjdai
doc2:My school is nccu
doc3:My department is MIS
doc4:I major cs
doc5:my school is in taipei
doc6:sjdai is a student in nccu
doc7:nccu is a school in taipei

sjdai in
'''


"""
輸入
doc1:My name is sjdai
doc2:My school is nccu

不重複字
['my', 'nccu', 'school', 'is', 'sjdai', 'name']

以上面不重複字的順序筆對每一個doc的結果
[1, 0, 0, 1, 1, 1] (['my(O)', 'nccu(x)', 'school(x)', 'is(O)', 'sjdai(O)', 'name(O)'])
[1, 1, 1, 1, 0, 0] (['my(O)', 'nccu(O)', 'school(O)', 'is(O)', 'sjdai(x)', 'name(x)'])
"""








