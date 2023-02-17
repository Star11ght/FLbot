import os

def changes(qq,things,choose):
    check = os.getcwd()
    location = 'D:/go-cqhttp_windows_amd64/code/usersdata/' + str(qq) + '.txt'
    if not os.path.exists(location):
        with open(file=location, mode='w', encoding="utf-8") as data:
            data.write(str(qq)+"\n")
            data.write("iamnameless\n")
            data.write("0\n")
            data.write("0\n")
            data.write("0\n")
            data.write("0\n")
            data.write("0\n")
            data.write("0\n")
            data.write("0\n")
            data.close()
    
    with open(file=location, mode='r', encoding="utf-8") as data:
        qq = data.readline()
        name = data.readline()
        love = data.readline()
        rpmax = data.readline()
        rpdate = data.readline()
        money = data.readline()
        qddate = data.readline()
        qdren = data.readline()

   
    if choose == 1:
        name = str(things)+"\n"
        
    elif choose == 2:
        love = str(things)+"\n"

    elif choose == 3:
        rpmax = str(things)+"\n"
        
    elif choose == 4:
        rpdate = str(things)+"\n"
        
    elif choose == 5:
        moneys = round(float(things),2)
        money = str(moneys)+"\n"
        
    elif choose == 6:
        qddate = str(things)+"\n"
        
    elif choose == 7:
        qdren = str(things)+"\n"
        
    with open(file=location, mode='w', encoding="utf-8") as data:
        data.write(qq)
        data.write(name)
        data.write(love)
        data.write(rpmax)
        data.write(rpdate)
        data.write(money)
        data.write(qddate)
        data.write(qdren)
        data.close()


    if choose == 5:
        rankqq = [0 for x in range(0,100)]
        rankmoney = [0 for x in range(0,100)]
        rankren = [0 for x in range(0,100)]
        locate = -1
        with open(file="moneyrank.txt", mode='r', encoding="utf-8") as data:
            rankqq[0] = data.readline()
            x=0
            while(rankqq[x] != "0\n"):
                rankmoney[x] = data.readline()
                rankren[x] = data.readline()
                x = x + 1
                rankqq[x] = data.readline()
            
        for i in range (x):
            if rankqq[i]==qq:  #找到QQ号的位置
                locate = i
                break
        
        if locate != -1:     #如果不是第一次拥有积分
            for i in range(locate,x+1):  
                rankqq[i] = rankqq[i+1] #后一个往前移动
                rankmoney[i] = rankmoney[i+1] 
                rankren[i] = rankren[i+1]
            x = x - 1

        i = 0
        money = money.strip()
        while float(rankmoney[i])>float(money) and i < x:
            i = i + 1
            #i为排行榜的积分中大于等于自己的积分的“最小积分”的下一位置（即排名）

        x = x + 1
        for y in range(x,i,-1):
            rankqq[y] = rankqq[y-1]
            rankmoney[y] = rankmoney[y-1]
            rankren[y] = rankren[y-1]

        rankqq[i] = qq
        rankmoney[i] = money
        rankren[i] = qdren

        with open(file="moneyrank.txt", mode='w', encoding="utf-8") as rank:
            a = 0
            while(rankqq[a]!="0\n"):
                rank.write(str(rankqq[a]))
                rankmoney[a] = rankmoney[a].strip()
                rank.write(str(rankmoney[a])+"\n")
                rank.write(str(rankren[a]))
                a = a + 1
            rank.write("0\n")
            rank.close