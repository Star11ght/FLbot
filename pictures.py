import requests
import time
import json
import re

def search():
    try:
        r = requests.get(urls).content.decode('UTF-8')
        start = r.find("https")
        end = r.find("}}]}")
        imglo = r.find("img-master")
        print(start,end)
        if start == -1 or end == -1:
            requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(picgroup),r'芙兰没有找到规定的图片！换个tag试试吧orz（tag之间要用中文逗号隔开哦！）'))
            getpicture = 0
            trytime = 0
            continue
        end = end - 1
        mas = r.find("square")
        originalpic = "https://i.pixiv.re/" + r[imglo:mas] + "master1200.jpg"
        print(r[start:end])
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(picgroup),r'[CQ:image,' r'file=' + str(r[start:end]) + r']'))
        getpicture = 0
        trytime = 0
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(picgroup),r'已找到图片！若过长时间内未收到可能被tx吞了，请再试一次！图片网址：'+ originalpic))
    except:
        trytime = trytime + 1
        if trytime > 30:
            requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(picgroup),r'请求失败次数过多！请再试一次orz'))
            getpicture = 0
            trytime = 0
        print("Failed."+str(trytime))
        time.sleep(0.2)
        continue
    
