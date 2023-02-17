from PIL import Image
import math

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


def writein(location,color,time):
    file = Image.open('D:/go-cqhttp_windows_amd64/data/images/123456/'+ str(time-1)+'.png')
    last = Image.open('last.png')
    x = int(ord(location[0])-64)
    y = int(location[1:])
    interval = 42
    lox = 305 + interval * (x - 8)
    loy = 304 + interval * (y - 8)
    location = (loy, lox)
    lastlo = (loy + 7, lox + 7)
    if color == 1:
        chess = transPNG('black.png')
    elif color == -1:
        chess = transPNG('white.png')
    file = mix(file, chess, location)
    file = mix(file, last, lastlo) 
    file.save('D:/go-cqhttp_windows_amd64/data/images/123456/'+str(time)+'.png')

writein("H7",1,3)

