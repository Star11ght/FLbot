import os

def getbags(qq,choose):
    check = os.getcwd()
    location = 'D:/go-cqhttp_windows_amd64/code/bag/' + str(qq).strip() + '.txt'
    if not os.path.exists(location):
        with open(file=location, mode='w', encoding="utf-8") as data:
            data.write("-1\n")
            data.close()
        print(0)
        return 0

    with open(file=location, mode='r', encoding="utf-8") as data:
        while(1):
            x = int(data.readline())
            if x == -1 :
                break
            have = int(data.readline())
            if(choose == x):
                print(have)
                return have
        print(0)
        return 0
