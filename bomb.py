import random

location = 'D:/go-cqhttp_windows_amd64/code/bomb/player.txt'
num = 'D:/go-cqhttp_windows_amd64/code/bomb/num.txt'

def checkingame(qq):
    with open(file=num, mode='r', encoding="utf-8") as data:
        people = int(data.readline())
        print(people)
    with open(file=location, mode='r', encoding="utf-8") as data:
        for a in range(people+1):
            x = data.readline()
            x = x.strip()
            if(int(x) == qq):
                print("已找到该QQ号正在参与游戏2")
                return 1
        return 0

def joingame(qq):
    with open(file=num, mode='r', encoding="utf-8") as data:
        people = int(data.readline())
        
    with open(file=location, mode='r', encoding="utf-8") as data:
        number = int(data.readline())
        
    if number == 0:
        number = random.randint(1,100000)
        with open(file=location, mode='w', encoding="utf-8") as data:
            data.write(str(number)+"\n")
            data.close()
            
    with open(file=location, mode='a', encoding="utf-8") as data:
        data.write(str(qq)+"\n")
        data.close()

    with open(file=num, mode='w', encoding="utf-8") as data:
        data.write(str(people+1))

def exitgame(qq):
    with open(file=num, mode='r', encoding="utf-8") as data:
        people = int(data.readline())
    
    with open(file=location, mode='r', encoding="utf-8") as data:
        lists = [0 for x in range(50)]
        qqlo = 0
        for a in range(people + 1):
            x = data.readline()
            x = x.strip()
            lists[a] = int(x)
            if(lists[a] == qq):
                qqlo = a
            a = a + 1

    with open(file=num, mode='w', encoding="utf-8") as data:
        data.write(str(people-1))
        
    with open(file=location, mode='w', encoding="utf-8") as data:
        if people - 1 == 0:
            data.write("0\n")
            data.close()
        else:
            for i in range (a):
                if i != qqlo:
                    data.write(str(lists[i])+"\n")
            data.close()
        
    
        
def gameend():
    with open(file=num, mode='w', encoding="utf-8") as data:
        data.write("0\n")
        data.close()
    with open(file=location, mode='w', encoding="utf-8") as data:
        data.write("0\n")
        data.close()

