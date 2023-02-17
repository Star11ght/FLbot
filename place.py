import os
import timecheck

def changeplace(qq,choose):
    check = os.getcwd()
    location = 'D:/go-cqhttp_windows_amd64/code/place/' + str(qq) + '.txt'
    if not os.path.exists(location):
        with open(file=location, mode='w', encoding="utf-8") as data:
            data.write("0\n")
            data.close()

    with open(file=location, mode='w', encoding="utf-8") as data:
        data.write(choose + "\n")

    if(choose=="0" or choose =="2-0"):
        return 2
    
    url = 'D:/go-cqhttp_windows_amd64/code/place/First_' + choose + '.txt'

    date = str(timecheck.times())

    with open(file=url, mode='r', encoding="utf-8") as data:
        lastdate = data.readline()
        lastdate = lastdate.strip()
        lasts = lastdate
        
        xn = ['' for x in range(50)]
        n = 0
        while lasts != "-1" and date == lastdate: 
            lasts = data.readline()
            lasts = lasts.strip()
            if lasts == qq:
                return 2    #2表示不是首次去这个地方
            xn[n] = lasts
            n = n + 1

        with open(file=url, mode='w', encoding="utf-8") as data2:
            data2.write(str(date) + "\n")
            for x in range(0,n-1):
                data2.write(str(xn[x]) + "\n")
            data2.write(str(qq) + "\n")
            data2.write("-1\n")
            return 1         #1表示首次去这个地方

def checkplace(qq):
    check = os.getcwd()
    location = 'D:/go-cqhttp_windows_amd64/code/place/' + str(qq) + '.txt'
    if not os.path.exists(location):
        with open(file=location, mode='w', encoding="utf-8") as data:
            data.write("0\n")
            data.close()
    
    with open(file=location, mode='r', encoding="utf-8") as data:
        place = data.readline()
        place = place.strip()
    
    return place
