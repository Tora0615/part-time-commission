# -*- coding: utf-8 -*-

# 回合
round = int(input())

# 輸入技能，回傳攻擊力
def get_skill_attack_power(skill):
    if skill == 'Sugar Attack':
        return 3
    if skill == 'Spicy Boomer':
        return 6
    if skill == 'Hot Splash':
        return 9
    
def new_game():    
    p1_hp = 30
    p2_hp = 30
    p1_atk = 0
    p2_atk = 0
    
    while True:
        if p1_hp <= 0 or p2_hp <= 0:
            break
        
        trun_to = input()
        if trun_to == 'stop':
            break
        skill_atk = get_skill_attack_power(input()) 
        
        
        # 攻擊
        if trun_to == 'player1':
            p2_hp = p2_hp - p1_atk - skill_atk
        elif trun_to == 'player2':
            p1_hp = p1_hp - p2_atk - skill_atk
            
        
        # 比較血量，加攻擊力
        if p1_hp > p2_hp:
            p2_atk += 1
        elif p2_hp > p1_hp:
            p1_atk += 1
            
    
    # 印勝負
    if p1_hp > p2_hp:
        print("Player1 wins.")
    elif p2_hp > p1_hp:
        print("Player2 wins.")
    else:
        print("Draw.")
        
    
    # 印最終兩人HP
    print("Player1 HP: " + str(p1_hp))        
    print("Player2 HP: " + str(p2_hp))       





# 看有幾回合，執行幾次
for i in range(round):
    new_game()




#測試資料單字
"""
player1
player2
Sugar Attack
Spicy Boomer
Hot Splash
"""
        
        
        
        