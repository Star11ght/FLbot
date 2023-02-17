import os

def changebank(qq,choose):
    check = os.getcwd()
    location = 'D:/go-cqhttp_windows_amd64/code/bank/' + str(qq) + '.txt'
    if not os.path.exists(location):
        with open(file=location, mode='w', encoding="utf-8") as data:
            data.write("0\n")
            data.close()

    with open(file=location, mode='w', encoding="utf-8") as data:
        data.write(str(choose) + "\n")

def checkbank(qq):
    check = os.getcwd()
    location = 'D:/go-cqhttp_windows_amd64/code/bank/' + str(qq) + '.txt'
    if not os.path.exists(location):
        with open(file=location, mode='w', encoding="utf-8") as data:
            data.write("0\n")
            data.close()
    
    with open(file=location, mode='r', encoding="utf-8") as data:
        place = data.readline()
        place = place.strip()
    
    return place