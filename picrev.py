import os
import uuid
import sys
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageDraw
from ffmpy import FFmpeg

os.makedirs('./image/', exist_ok=True)

def jti(img_1, img_2, numbe, flag=0): 
    img1 = Image.open(img_1)
    img2 = Image.open(img_2)
    size1, size2 = img1.size, img2.size
    if flag == 0:
        joint = Image.new("RGB", (size1[0] + size2[0], size1[1]))
        loc1, loc2 = (0, 0), (size1[0], 0)
    else :
        joint = Image.new("RGB", (size1[0] , size1[1] + size2[1]))
        loc1, loc2 = (0, 0), (0, size1[1])
        
    joint.paste(img1, loc1)
    joint.paste(img2, loc2)
    joint.save('D:/go-cqhttp_windows_amd64/data/images/picrev_' + str(numbe) + '.png')
    #0是水平1是垂直

def picrev(picurl,choose):
    with open(file='D:/go-cqhttp_windows_amd64/code/picture/number.txt', mode='r', encoding="utf-8") as data:
        numbe = int(data.readline())
    numbe = numbe + 1
    with open(file='D:/go-cqhttp_windows_amd64/code/picture/number.txt', mode='w', encoding="utf-8") as data:
        data.write(str(numbe))
        
    from urllib.request import urlretrieve
    urlretrieve(picurl, 'D:/go-cqhttp_windows_amd64/code/picture/' + str(numbe) + '.png')

    os.getcwd()
    im_path = os.path.join(os.getcwd(), 'D:/go-cqhttp_windows_amd64/code/picture/' + str(numbe) + '.png')
    img = Image.open(im_path)
    w = img.width       #图片的宽
    h = img.height      #图片的高
    print(w, h)

    if choose == 5:
        img5 = cv2.imread(im_path)
        img5 = cv2.cvtColor(img5,cv2.COLOR_BGR2RGB)
        img5 = cv2.bitwise_not(img5)
        cv2.imwrite('D:/go-cqhttp_windows_amd64/data/images/picrev_' + str(numbe) + '.png', img5)
        return numbe

    if choose <= 2:
        reverse = img.transpose(Image.FLIP_LEFT_RIGHT)  # 水平翻转
    else :
        reverse = img.transpose(Image.FLIP_TOP_BOTTOM)  # 垂直翻转
    revpath = 'D:/go-cqhttp_windows_amd64/code/picture/' + str(numbe) + 'rev.png'
    reverse.save(revpath)

    img2 = Image.open(revpath)
    if choose == 1:
        revori = img.crop((0,0,w/2,h))
        revoripath = 'D:/go-cqhttp_windows_amd64/code/picture/' + str(numbe) + 'revori.png'
        revcut = img2.crop((w/2,0,w,h))
        revcutpath = 'D:/go-cqhttp_windows_amd64/code/picture/' + str(numbe) + 'revcut.png'
        revori.save(revoripath)
        revcut.save(revcutpath)
        jti(revoripath , revcutpath, numbe, 0)
    elif choose == 2:
        revcut = img2.crop((0,0,w/2,h))
        revcutpath = 'D:/go-cqhttp_windows_amd64/code/picture/' + str(numbe) + 'revori.png'
        revori = img.crop((w/2,0,w,h))
        revoripath = 'D:/go-cqhttp_windows_amd64/code/picture/' + str(numbe) + 'revcut.png'
        revori.save(revoripath)
        revcut.save(revcutpath)
        jti(revcutpath , revoripath, numbe, 0)
    elif choose == 3:
        revori = img.crop((0,0,w,h/2))
        revoripath = 'D:/go-cqhttp_windows_amd64/code/picture/' + str(numbe) + 'revori.png'
        revcut = img2.crop((0,h/2,w,h))
        revcutpath = 'D:/go-cqhttp_windows_amd64/code/picture/' + str(numbe) + 'revcut.png'
        revori.save(revoripath)
        revcut.save(revcutpath)
        jti(revoripath , revcutpath, numbe, 1)
    elif choose == 4:
        revcut = img2.crop((0,0,w,h/2))
        revcutpath = 'D:/go-cqhttp_windows_amd64/code/picture/' + str(numbe) + 'revori.png'
        revori = img.crop((0,h/2,w,h))
        revoripath = 'D:/go-cqhttp_windows_amd64/code/picture/' + str(numbe) + 'revcut.png'
        revori.save(revoripath)
        revcut.save(revcutpath)
        jti(revcutpath , revoripath, numbe, 1)
    return numbe


