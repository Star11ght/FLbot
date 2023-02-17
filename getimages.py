from PIL import Image
import math
import os

def transPNG(srcImageName):
    img = Image.open(srcImageName)
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = list()
    for item in datas:
        newData.append(item)
    img.putdata(newData)
    return img

def mix(img1,img2,coordinator):
    im = img1
    mark = img2
    layer = Image.new('RGBA', im.size, (0, 0, 0, 0))
    layer.paste(mark, coordinator)
    out = Image.composite(layer, im, layer)
    return out


def writein(location,color,time,room):
    file = Image.open('D:/go-cqhttp_windows_amd64/data/images/'+ str(room) + "/" + str(time-1)+'.png')
    x = int(ord(location[0])-96)
    y = int(location[1:])
    interval = 42
    lox = 305 + interval * (x - 8)
    loy = 304 + interval * (y - 8)
    location = (loy, lox)
    if color == 1:
        chess = transPNG('D:/go-cqhttp_windows_amd64/data/images/black.png')
    elif color == 2:
        chess = transPNG('D:/go-cqhttp_windows_amd64/data/images/white.png')
        
    file = mix(file, chess, location)
    roomdata = 'D:/go-cqhttp_windows_amd64/code/gochess/' + str(room) + '.txt'
    
    with open(file=roomdata, mode='r', encoding="utf-8") as data:
        people = data.readline()
        rounds = data.readline()
        qqblack = int(data.readline())
        qqwhite = int(data.readline())

    if time != 1 :
        qqdata = 'D:/go-cqhttp_windows_amd64/code/gochess/'
        if time % 2 == 1:
            qqdata = qqdata + str(qqwhite) + '.txt'
        elif time % 2 == 0:
            qqdata = qqdata + str(qqblack) + '.txt'
        with open(file=qqdata, mode='r', encoding="utf-8") as data:
            lastnx = data.readline()
            lastnx = lastnx.strip()
            lastx = int(ord(lastnx)-96)
            lasty = int(data.readline())
            lox = 305 + interval * (lastx - 8)
            loy = 304 + interval * (lasty - 8)
            location = (loy, lox)
            if color == 1:
                chess = transPNG('D:/go-cqhttp_windows_amd64/data/images/whitelast.png')
            elif color == 2:
                chess = transPNG('D:/go-cqhttp_windows_amd64/data/images/blacklast.png')
            file = mix(file, chess, location)

    file.save('D:/go-cqhttp_windows_amd64/data/images/'+ str(room) + "/" + str(time)+'.png')
    file.save('D:/go-cqhttp_windows_amd64/data/images/'+ str(room) + "_" + str(time)+'.png')

            
    
def start(room):
    os.mkdir("D:/go-cqhttp_windows_amd64/data/images/" + str(room))
    file = Image.open('D:/go-cqhttp_windows_amd64/data/images/Board.jpg')
    file.save('D:/go-cqhttp_windows_amd64/data/images/'+ str(room) + "/0.png")
    file.save('D:/go-cqhttp_windows_amd64/data/images/'+ str(room) + "_0.png")

def getadd(rounds):
    r = int(rounds)
    if r >= 0 and r < 9:
        return "0"
    if r >= 9 and r < 15:
        return "50.0"
    if r >= 15 and r < 21:
        return "40.0"
    if r >= 21 and r < 27:
        return "30.0"
    if r >= 27 and r < 33:
        return "25.0"
    if r >= 33 and r < 39:
        return "20.0"
    if r >= 39 and r < 51:
        return "15.0"
    if r >= 51 and r < 100:
        return "10.0"
    if r >= 100 and r < 150:
        return "30.0"
    if r >= 150 and r < 200:
        return "100.0"
    if r >= 200 and r< 225:
        return "200.0"
    if r == 225:
        return "500.0"
    
