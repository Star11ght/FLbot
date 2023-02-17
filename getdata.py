import os

def getsd(qq,choose):
    check = os.getcwd()
    location = 'D:/go-cqhttp_windows_amd64/code/usersdata/' + str(qq).strip() + '.txt'
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
            data.close()

    with open(file=location, mode='r', encoding="utf-8") as data:
        lists = [data.readline() for x in range(0,8)]
        
    return lists[choose]
