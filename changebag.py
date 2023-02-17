import os

def changebags(qq,thing,choose):
    check = os.getcwd()
    location = 'D:/go-cqhttp_windows_amd64/code/bag/' + str(qq) + '.txt'
    if not os.path.exists(location):
        with open(file=location, mode='w', encoding="utf-8") as data:
            data.write("-1\n")
            data.close()
    
    things = [0 for i in range(100)]

    with open(file=location, mode='r', encoding="utf-8") as data:
        while(1):
            x = int(data.readline())
            if x == -1 :
                break
            things[x] = int(data.readline())

    things[int(choose)] = int(thing)

    with open(file=location, mode='w', encoding="utf-8") as data:
        for i in range(1,9):
            if things[i] != 0 :
                data.write(str(i) + "\n")
                data.write(str(things[i]) + "\n")
        data.write("-1\n")
        data.close()
