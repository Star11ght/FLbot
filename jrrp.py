import datetime
import random
import string
import getdata
import change

def getjrrp(qq,times):
    locate = -1
    checks = 0
    checksv = 0
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")

    jrrp = open(file="jrrp.txt", mode='r', encoding="utf-8")
    ct = jrrp.readline()

    date=date.strip()
    ct=ct.strip()
    if date!=ct:
        with open(file="jrrp.txt", mode='w', encoding="utf-8") as jrrp:
            jrrp.write(date+"\n")
            with open(file="jrrpnum.txt", mode='w', encoding="utf-8") as jrrpnum:
                jrrpnum.write("0\n")
            jrrpnum.close()
            jrrp.close()
        jrrp = open(file="jrrp.txt", mode='r', encoding="utf-8")
        ct = jrrp.readline()
    
    jrrpnum = open(file="jrrpnum.txt", mode='r', encoding="utf-8")
    ctx = int(jrrpnum.readline())
    #ctx记录今天测过人品的人数

    for x in range(int(ctx)):
        qid = jrrp.readline()
        rpx = jrrp.readline()

        qid = qid.strip()
        rpx = rpx.strip()
        if qid == str(qq):
            if times == 1:
                return rpx #已经测过直接返回值
            else:
                locate = x
                break
        elif qid =="":
            break

    listqq = [0 for x in range(int(ctx)+2)]
    listjrrp = [0 for x in range(int(ctx)+2)]
    
    with open(file="jrrp.txt", mode='r', encoding="utf-8") as data:
        date = data.readline()
        for x in range(0,int(ctx)):
            listqq[int(x)] = data.readline()
            listjrrp[int(x)] = data.readline()

    originrp = int(listjrrp[locate])
    
    rp = random.randint(1,10020)
    n = 0
    if(times == 2):
        if rp <= int(listjrrp[locate]):
            return rp
        else:
            ctx = ctx - 1
            for x in range(locate,int(ctx)):
                listqq[int(x)] = listqq[int(x+1)]
                listjrrp[int(x)] = listjrrp[int(x+1)]

    while rp<int(listjrrp[n]) and n<int(ctx):
        n = n + 1

    for x in range(int(ctx),n,-1):
        listqq[x] = listqq[x-1]
        listjrrp[x] = listjrrp[x-1]
            
    listqq[n] = str(qq) + "\n"
    listjrrp[n]= str(rp) + "\n"

    with open(file="jrrp.txt", mode='w', encoding="utf-8") as jrrp:
        jrrp.write(date)
        for x in range(0,int(ctx)+1):
            jrrp.write(str(listqq[int(x)]))
            jrrp.write(str(listjrrp[int(x)]))
        jrrp.close
        
    if times == 1:
        with open(file="jrrpnum.txt", mode='w', encoding="utf-8") as jrrpnum:
            ctn=int(ctx)+1
            jrrpnum.write(str(ctn)+"\n")
            jrrpnum.close()


    if rp>int(getdata.getsd(qq,3)):
        date = date.strip()
        change.changes(qq,rp,3)
        change.changes(qq,date,4)
        


    rankqq = [0 for x in range(0,25)]
    rankjrrp = [0 for x in range(0,25)]
    rankdate = [0 for x in range(0,25)]

    dt = date.strip()
    with open(file="rprank.txt", mode='r', encoding="utf-8") as data:
        for x in range(0,20):
            if checksv != 1:
                checks = 0
            rankqq[x] = data.readline()
            rqq = rankqq[x].strip()
            if str(qq) == rqq:
                checks = checks + 1
            rankjrrp[x] = data.readline()
            rankdate[x] = data.readline()
            rdt = rankdate[x].strip()
            if rdt == dt:
                checks = checks + 1
            if checks == 2 and checksv == 0:
                checksv = 1
                originrank = x
                print(originrank)

    if rp>int(rankjrrp[19]):
        n = 0
        while rp<int(rankjrrp[n]):
            n = n + 1

        if(times == 1 or checks != 2):
            for x in range(19,n-1,-1):
                rankqq[x] = rankqq[x-1]
                rankjrrp[x] = rankjrrp[x-1]
                rankdate[x] = rankdate[x-1]

        else:
            for x in range(originrank,n-1,-1):
                rankqq[x] = rankqq[x-1]
                rankjrrp[x] = rankjrrp[x-1]
                rankdate[x] = rankdate[x-1]

        rankqq[n] = str(qq) + "\n"
        rankjrrp[n] = str(rp) + "\n"
        rankdate[n] = date + "\n"

        with open(file="rprank.txt", mode='w', encoding="utf-8") as rank:
            for x in range(0,20):
                rank.write(str(rankqq[x]))
                rank.write(str(rankjrrp[x]))
                rank.write(str(rankdate[x]))
            rank.close
    
    if times==2:
        return rp

    print("times=1")
    with open(file="rplowrank.txt", mode='r', encoding="utf-8") as data:
        for x in range(0,20):
            rankqq[x] = data.readline()
            rankjrrp[x] = data.readline()
            rankdate[x] = data.readline()

    if rp<int(rankjrrp[19]):
        n = 0
        while rp>int(rankjrrp[n]):
            n = n + 1

        for x in range(19,n-1,-1):
            rankqq[x] = rankqq[x-1]
            rankjrrp[x] = rankjrrp[x-1]
            rankdate[x] = rankdate[x-1]
                
        rankqq[n] = str(qq) + "\n"
        rankjrrp[n] = str(rp) + "\n"
        rankdate[n] = date

        with open(file="rplowrank.txt", mode='w', encoding="utf-8") as rank:
            for x in range(0,20):
                rank.write(str(rankqq[x]))
                rank.write(str(rankjrrp[x]))
                rank.write(str(rankdate[x]))
            
            rank.close
            
    return rp