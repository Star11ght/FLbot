#coding=utf-8

import receive
import json
import getbag
import changebag
import sendmsg
import jrrp
import random
import change
import getdata
import guessnum
import os
import time
import timecheck
import math
import bomb
import time
import getimages
import shutil
import piano
import requests
import uuid
import picrev
import place
import bank
import datetime
from ffmpy import FFmpeg

g2total = 0
g2left = 0
g2right = 0
repeat = ""
repeatn = 0
repeating = 0
getpicture = 0
urls=''
trytime = 0
picgroup = ""
picqq = ""
codestart = 0
codemiddle = -1
codeend = 0
newsget = 0
newdays = 0

while 1:
    try:
        date = timecheck.times()
        rev = receive.rev_msg()
        now = datetime.datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        days = now.strftime("%d")
        hours = now.strftime("%H")
        minute = now.strftime("%M")
        if hours == "08" and minute == "00" and newsget == 0:
            IMAGE_URL = "https://v2.alapi.cn/api/zaobao?token=dry6TkU6X7uvtWrn&format=image"
            from urllib.request import urlretrieve
            urlretrieve(IMAGE_URL, 'D:/go-cqhttp_windows_amd64/data/images/news.png')
            sendmsg.send_msg({'msg_type':'group','number':'719317473','msg':'[CQ:image,file=news.png]'}) 
            sendmsg.send_msg({'msg_type':'group','number':'719317473','msg':'早上好~这里是今天的新闻，祝大家今日万事顺利！'}) 
            sendmsg.send_msg({'msg_type':'group','number':'1164881074','msg':'[CQ:image,file=news.png]'})
            sendmsg.send_msg({'msg_type':'group','number':'1164881074','msg':'早上好~这里是今天的新闻，祝大家今日万事顺利！'}) 
            newsget = 1
        
        if hours == "00" and newsget == 1:
            newsget = 0

        if hours == "00" and minute == "00" and newdays == 0:
            sendmsg.send_msg({'msg_type':'group','number':'719317473','msg':'晚上好~新的一天开始啦！今天是' + year + "年" + month + "月" + days + "日，" + '距离《塞尔达传说：王国之泪》发售还有' + str(161 - int(date)) + "天，星光你先别急.jpg\n祝大家今夜好梦哦~"}) 
            newdays = 1

        if hours == "01" and newdays == 1:
            newdays = 0
        
        if getpicture == 1:
            if rev["post_type"] == "message" and rev["message_type"] == "group": #群聊
                group = rev['group_id']
                qq=rev['sender']['user_id']
                message = rev['raw_message']
                rate = trytime/30
                rate = round(rate*100,2)
                if message.find("fl.") == 0:
                    if message == "fl.picend" and int(qq) == int(picqq):
                        getpicture = 0
                        trytime = 0
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您已停止图片的寻找！屑网络呜呜呜呜……'})
                        continue
                    else:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']芙兰正在帮忙寻找图片，暂时没法和你聊天……等我一会儿好嘛！或者也可以让发起者输入fl.picend停止寻找哦！（寻找进度：' + str(rate) + '％）'})

            elif rev["post_type"] == "message" and rev["message_type"] == "private": #私聊
                qq = rev['sender']['user_id']
                rate = trytime/30
                rate = round(rate*100,2)
                sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'芙兰正在帮忙寻找图片，暂时没法和你聊天……等我一会儿好嘛！或者也可以让发起者输入fl.picend停止寻找哦！（寻找进度：' + str(rate) + '％）'})
                  
            try:
                r = requests.get(urls).content.decode('UTF-8')
                start = r.find("https")
                end = r.find("}}]}")
                
                imglo = r.find("img-master")
                print(start,end)
                if start == -1 or end == -1:
                    requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(picgroup),r'[CQ:at,qq='+ str(picqq) + r']芙兰没有找到规定的图片！换个tag试试吧orz（tag之间要用中文逗号隔开哦！）'))
                    getpicture = 0
                    trytime = 0
                    continue
                end = end - 1
                
                pid_start = r.find("pid") + 5
                p_start = r.find("\"p\"") + 4
                uid_start = r.find("uid") + 5
                title_start = r.find("title") + 8
                author_start = r.find("author") + 9
                author_end = r.find("r18") - 3
                msg_pid = r[pid_start:p_start-5]
                msg_p = r[p_start:uid_start-7]
                msg_uid = r[uid_start:title_start-10]
                msg_title = r[title_start:author_start-12]
                msg_author = r[author_start:author_end]
                print(msg_pid + msg_p + msg_uid + msg_title + msg_author)

                mas = r.find("square")
                originalpic = "https://i.pixiv.re/" + r[imglo:mas] + "master1200."

                if r[end - 3:end] == "jpg":
                     originalpic =  originalpic + "jpg"
                else:
                     originalpic =  originalpic + "png"
                print(r[start:end])
                requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(picgroup),r'[CQ:at,qq='+ str(picqq) + r'][CQ:image,' r'file=' + str(r[start:end]) + r']'))
                getpicture = 0
                trytime = 0
                
            except:
                trytime = trytime + 1
                if trytime > 30:
                    requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(picgroup),r'[CQ:at,qq='+ str(picqq) + r']请求失败次数过多！请再试一次orz'))
                    getpicture = 0
                    trytime = 0
                    continue
                print("Failed."+str(trytime))
                time.sleep(0.2)
                continue

            websites = "https://pixiv.re/" + msg_pid
            msg_p = str(int(msg_p) + 1)
            if(msg_p!="1"):
                websites = websites + "-" + msg_p
            if r[end - 3:end] == "jpg":
                websites = websites + ".jpg"
            else:
                websites = websites + ".png"
            requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(str(picgroup),r'[CQ:at,qq='+ str(picqq) + ']已找到图片！若长时间未收到可能被tx吞了或是原图网址404了，请再试一次！\n标题：' + msg_title + '\n作者：' + msg_author +'\nid：' + msg_pid + ' 第' + msg_p + 'P\n作者id：' + msg_uid + '\n图片网址：\n'+ websites))
            continue
        codestart = codestart + 1
        if rev["post_type"] == "message":
            if rev["message_type"] == "private": #以下为私聊部分
                qq = rev['sender']['user_id']
                message = rev['raw_message']
                if message.find("fl.name")<0: message = message.lower()

                if message.find('芙兰')>=0 :
                    if qq == 1119194972:
                         sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'老公晚上好~[CQ:face,id=2][CQ:face,id=2][CQ:face,id=2]'})
                    else:
                         sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'唔……你好呀~'})

                elif message.find("早上好")>=0 or message.find("morning")>=0 or message == "za" or message.find("早安")>=0 or message.find("晨安")>=0:
                    sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'早上好~祝你有一个开心完美的一天哦！芙兰一到早上就困Zzzzzzz……'})

                elif message.find("中午好")>=0 or message.find("noon")>=0 or message.find("下午好")>=0 or message.find("午安")>=0:
                    sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'太阳最大的时候！芙兰这个时候一般不敢外出呢orz'})

                elif message.find("晚上好")>=0 or message.find("evening")>=0 :
                    sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'晚上好！太阳终于落山啦！又到了芙兰最快乐的时刻~'})

                elif message.find("晚安")>=0 or message.find("night")>=0 or message == "wa" or message.find("睡觉")>=0 or message.find("sleep")>=0 :
                    sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'晚安哦~愿你在梦里也能看见红魔馆上空的那道七色彩虹XD'})

                elif message.find("草")>=0 or message.find("grass")>=0:
                    sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'草。'})

                elif message.find("你是")>=0:
                    sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'你是？'})

                elif message.find("fl.piano")>=0:
                    if message[0:8] == "fl.piano":
                        melody = message[9:]
                        if len(message) == 8:
                            sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'钢琴功能输入顺序：\n①（可选）左括号\"(\"降一个八度，右括号\")\"反之，默认下为小字一组，最多可使用三个括号\n②（必选）输入音符0~7，可用合法的升降号#或b，0为空拍无升降号\n③（可选）加号\"＋\"速度加快一倍，减号\"－\"速度放慢一倍，默认下为8分音符，范围为全音符~32分音符'})    
                        elif message[8] != " ":
                            sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'piano后面要加空格哦~'})
                        else:
                            timedo = 0
                            timedo = len(melody)/4
                            timedo = round(timedo,2)
                            if timedo !=0:
                                sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'芙兰大约需要' + str(timedo) + '秒钟的时间弹奏！等等喵……'})
                            get = piano.musicmake(melody)
                            print(get)
                            if get == None or get == -1:
                                sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'输入的音符串不合法！\n输入顺序：\n①（可选）左括号\"(\"降一个八度，右括号\")\"反之，默认下为小字一组，最多可使用三个括号\n②（必选）输入音符0~7，可用合法的升降号#或b，0为空拍无升降号\n③（可选）加号\"＋\"速度加快一倍，减号\"－\"速度放慢一倍，默认下为8分音符，范围为全音符~32分音符'})
                            else:
                                pianodocu = str(get) + ".mp3"
                                sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:record,file=' + pianodocu + ']'})

                elif message == 'fl.nsrm':
                    sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'我是吸血鬼，所以我bsr！'})

                elif message == 'fl.mapledise':
                    sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:image,file=mapledise.jpg]'})

                elif message == 'fl.goodnight' or message == 'fl.night' or message == 'fl.sleep' or message == 'fl.晚安':
                    sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'晚安哦~愿你在梦里也能看见红魔馆上空的那道七色彩虹XD'})

                elif message == 'fl.goodmorning' or message == 'fl.morning' or message == 'fl.hello' or message == 'fl.hi':
                    sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'泥猴哇！我是芙兰朵露斯卡雷特哒！想问我问题可以对我输入指令help！诶……输入指令是啥玩意'})

                elif message == 'fl.starlight' or message == 'fl.星光' or message == 'fl.暗黑色的星光' or message == 'fl.大可罢格' or message == 'fl.meteoroid':
                    sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'听说Meteoroid与Margatroid很像，不过实际上，Starlight与Scarlet也很像哦！（笑）'})

                elif message.find("fl.kiss")>=0:
                    if qq == 1119194972:
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:poke,qq=1119194972]'})
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:at,qq='+str(qq)+']kisskiss~~~'})
                    else :
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:at,qq='+str(qq)+']俺拒绝！orz'})

                elif message.find("fl.chess")>=0:
                    if message[0:8] == "fl.chess":
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'抱歉qwq芙兰不会下五子棋orz可以去群里找别人下哦！'})

                elif message == 'fl.endchess':
                    if os.path.exists(checkchessfile):
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'笨蛋，你偷偷告诉我结束对局那对方怎么办啦！！！'})
                    else:
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'诶……难不成你在和芙兰下棋嘛！芙兰可没有答应哦~'})            

                elif message.find("fl.rank")>=0:
                    if message[0:7] == "fl.rank":
                        newrank = message[8:]
                        
                        if len(message) == 7:
                            sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'\nrank 1可查询今日人品排名\nrank 2可查询历史人品排名\nrank 3可查询积分排名\nrank 4可查询最低历史人品排名\n键入别的还发现了bug说明你tdll吧！？！？'})
                        elif message[7] != " ":
                            sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'rank后面要加空格哦~'})
                    
                        elif newrank == "1":
                            with open(file="jrrpnum.txt", mode='r', encoding="utf-8") as data:
                                number = int(data.readline())
                            with open(file="jrrp.txt", mode='r', encoding="utf-8") as data:
                                date = data.readline()
                                output = '今天的日期为：'+date.strip()+"，今日人品排名如下：\n"
                                
                                for x in range(number):
                                    rankqq = data.readline()
                                    rankqq = rankqq.strip()
                                    nowname = getdata.getsd(rankqq,1)
                                    if nowname == "iamnameless\n":
                                        nowname = "*******" + rankqq[-4:]
                                    else:
                                        nowname = nowname.strip() + "(" + rankqq[-4:] + ")"
                                    rankrp = data.readline()
                                    output = output + str(x+1) + " " + nowname + " " + rankrp
                                if number == 0 :
                                    output=output + "我趣，今天竟然没人测人品？！"
                            sendmsg.send_msg({'msg_type':'private','number':qq,'msg':output})
                            
                        elif newrank == "2":
                            output = '今日人品历史排名：\n'
                            with open(file="rprank.txt", mode='r', encoding="utf-8") as data:
                                rankqq = data.readline()
                                rank = 0
                                while(rankqq!="00000000\n" and rankqq!= ""):
                                    nowname = getdata.getsd(rankqq,1)
                                    
                                    if nowname == "iamnameless\n":
                                        nowname = "*******" + rankqq[-5:-1]
                                    else:
                                        nowname = nowname.strip() + "(" + rankqq[-5:-1] + ")"
                                    rankrp = data.readline()
                                    rankdt = data.readline()
                                    rank = rank + 1
                                    output = output + str(rank) + " " + nowname + " " + rankrp.strip() + " " + rankdt
                                    print(output)
                                    rankqq = data.readline()
                                sendmsg.send_msg({'msg_type':'private','number':qq,'msg':output})
                                    
                        elif newrank == "3":
                            output = '积分总排名：'
                            with open(file="moneyrank.txt", mode='r', encoding="utf-8") as data:
                                rankqq = data.readline()
                                rank = 0
                                numbers = 0
                                while(rankqq!="0\n"):
                                    numbers = numbers + 1
                                    if int(rankqq.strip()) == int(qq):
                                        myrank = numbers
                                    rankmoney = data.readline()
                                    rankren = data.readline()
                                    rankren = rankren.strip()
                                    rank = rank + 1
                                    if(numbers <= 5):
                                        nowname = getdata.getsd(rankqq,1)
                                        if nowname == "iamnameless\n":
                                            nowname = "*******" + rankqq[-5:-1]
                                        else:
                                            nowname = nowname.strip() + "(" + rankqq[-5:-1] + ")"
                                        output = output + "\n" + str(rank) + " " + nowname + " " + rankmoney.strip() + " 已连续签到" + rankren + "天"
                                    rankqq = data.readline()
                                output = output + "\n………………\n——————————————"
                                output = output + "\n您的排名为：" + str(myrank)
                                sendmsg.send_msg({'msg_type':'private','number':qq,'msg':output})

                        elif newrank == "4":
                            output = '今日人品(最低)历史排名：\n'
                            with open(file="rplowrank.txt", mode='r', encoding="utf-8") as data:
                                rankqq = data.readline()
                                rank = 0
                                while(rankqq!="00000000\n" and rankqq!= ""):
                                    nowname = getdata.getsd(rankqq,1)
                                    
                                    if nowname == "iamnameless\n":
                                        nowname = "*******" + rankqq[-5:-1]
                                    else:
                                        nowname = nowname.strip() + "(" + rankqq[-5:-1] + ")"
                                    rankrp = data.readline()
                                    rankdt = data.readline()
                                    rank = rank + 1
                                    output = output + str(rank) + " " + nowname + " " + rankrp.strip() + " " + rankdt
                                    print(output)
                                    rankqq = data.readline()
                                sendmsg.send_msg({'msg_type':'private','number':qq,'msg':output})

                        
                        else:
                            sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'rank 1可查询今日人品排名\nrank 2可查询历史人品排名\nrank 3可查询积分排名\nrank 4可查询最低历史人品排名\n键入别的还发现了bug说明你tdll吧！？！？'})
                            
                elif message.find("fl.name")>=0:
                    if message[0:7] == "fl.name":
                        newname = message[8:]
                        if len(message) == 7:
                            sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'诶嘿！以后我就叫你无名氏啦~好吧开玩笑的你倒是在后面输个名字哇！！！(>O<)'})
                        elif message[7] != " ":
                            sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'name后面要加空格哦~'})
                        else:
                            change.changes(qq,newname,1)
                            sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'诶嘿！以后我就叫你'+newname+'啦~'})
                        
                elif message == 'fl.emotion':
                    emostr=""
                    for x in range(300):
                        emostr = emostr + '[CQ:face,id='+str(x)+']'
                    sendmsg.send_msg({'msg_type':'private','number':qq,'msg':emostr})
                
                elif message == 'fl.db' or message == 'fl.darkbug' or message == 'fl.miyaktik':
                    songs = random.randint(0,206)
                    lists = [0 for x in range(0,500)]
                    with open(file="Songs.txt", mode='r', encoding="utf-8") as get:
                        for x in range(207):
                            lists[x]=get.readline()
                            lists[x]=lists[x].strip()
                    songid = lists[songs]
                    sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:music,type=163,id='+songid+']'})
                    sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:at,qq='+str(qq)+']已为您随机分享大可罢格的音乐~本曲的网易云曲目id：'+songid})

                elif message == 'fl.tap':
                    if qq == 1119194972:
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:poke,qq=1119194972]'})
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'星光光可爱捏'})
                    elif qq == 2303515884:
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:poke,qq=2303515884]'})
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'紫苑给你做的饭一定很好吃吧www'})
                    elif qq == 1921749109:
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:poke,qq=1921749109]'})
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'心魔大姐姐太大佬啦！你的三只眼睛是不是正倒映着我的翅膀呀.jpg'})
                    elif qq == 849644088:
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:poke,qq=849644088]'})
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'糖糖我也想和觉大人玩~（qwq)'})
                    elif qq == 208518697:
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:poke,qq=208518697]'})
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'水水今天和魔理沙玩得开心嘛xd'})
                    elif qq == 1053524165:
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:poke,qq=1053524165]'})
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'夯爸爸！教我家星光光编程！orz'})
                    elif qq == 2281887393:
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:poke,qq=2281887393]'})
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'传说中的海豚！希望我拜一拜后也能通过超强的计算力爆破红魔（被蕾咪捂嘴拖走）'})
                    elif qq == 1981001368:
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:poke,qq=1981001368]'})
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:at,qq='+str(qq)+']呜呜呜维他他！受我一拜！orz我也想找光光和恋恋玩哦XD'})
                    elif qq == 1501642864:
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:poke,qq=1501642864]'})
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'神的戳一戳[CQ:face,id=2][CQ:face,id=2][CQ:face,id=2]'})
                    elif qq == 3558187259:
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:poke,qq=3558187259]'})
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'黑叔！快教星光作曲打块画画打游戏！嘿嘿……我们的黑叔……'})
                    elif qq == 2963445800:
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:poke,qq=2963445800]'})
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'电子！你是俺们的光！想看你和星光产生光电效应！（划去）'})
                    elif qq == 3559736091:
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:poke,qq=3559736091]'})
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'南辰北耀 㳚远听涛 秋林枫叶 唯听萧萧！'})
                    else:
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:poke,qq='+str(qq)+']'})
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'戳一戳素未谋面的你，希望你能天天开心事事顺心！干巴爹！（挥舞拳头）'})
                    
                                        
                elif message.find("fl.")==0:
                    newdice = message[4:]
                    if message.find("fl.d")>=0 and newdice.isdigit():
                        if message[0:4] == "fl.d":
                            if len(message) == 4:
                                sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'d后面加个数字就能扔骰子啦！或者在d后面加个字母b也不是不行啦~'})
                            elif int(newdice) <= 0:
                                sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'我也想去异次元世界，能带我走嘛！'})
                            else:
                                a = random.randint(0,int(newdice))
                                rate = a/int(newdice)
                                rate = round(rate*100,2)
                                dicedata = 'D:/go-cqhttp_windows_amd64/code/dice/' + str(qq) + '.txt'
                                output = '您投出了' + str(newdice) + "面骰！得到的结果是：" + str(a) + "(" + str(rate) + "％)"
                                dtime = 0
                                avg = 0
                                if os.path.exists(dicedata):
                                    with open(file=dicedata, mode='r', encoding="utf-8") as data:
                                        dtime = int(data.readline())
                                        avg = float(data.readline())
                                avg = (avg * dtime + rate)/(dtime + 1)
                                dtime = dtime + 1
                                avg = round(avg,2)
                                output = output + "\n您一共投了" + str(dtime) + "次骰子，平均点数概率为：" + str(avg) + "％"
                                with open(file=dicedata, mode='w', encoding="utf-8") as data:
                                    data.write(str(dtime)+"\n"+str(avg)+"\n")
                                sendmsg.send_msg({'msg_type':'private','number':qq,'msg':output})
                    else:
                        sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'私聊部分功能暂时关闭！果咩纳塞orz（部分可用功能：piano rank db name d[数字]）'})

                else:
                    choose = random.randint(0,28)
                    if choose == 0:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'阿巴阿巴阿巴哇达西看不懂捏orz'})
                    elif choose == 1:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'喵喵喵？？？'})
                    elif choose == 2:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'你说的对，但是大可罢格是lj，后面忘了=w='})
                    elif choose == 3:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'Zzzzzzzz……'})
                    elif choose == 4:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'我的莱瓦汀似乎在蠢蠢欲动……（坏笑）'})
                    elif choose == 5:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'这是一条被大可罢格精神操控后强制输入进芙兰脑袋瓜之后说出来的消息！啊嘞我刚才说了啥……'})
                    elif choose == 6:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'听说只要打出fl.XXX就可以触发这些消息。“触发”是啥意思呢……'})
                    elif choose == 7:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'6373 1232#5 637171765 35231~'})
                    elif choose == 8:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'小道消息，大可罢格下次出专辑可能是在………………………………………………………………………………………………………………………………………………………………下一次。'})
                    elif choose == 9:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'您tdll，我tdll，大家都tdll171717'})
                    elif choose == 10:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'不知道你在说啥，能戳戳你嘛！（抄起莱瓦汀）'})
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:poke,qq='+str(qq)+']'})
                    elif choose == 11:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'sendsmg.send_msg(星光用了这个申必的函数操控了芙兰。嘿嘿我是星光！)'})
                    elif choose == 12:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'禁忌「一重存在」'})
                     time.sleep(1)
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'禁忌「二重存在」'})
                     time.sleep(1)
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'禁忌「三重存在」'})
                     time.sleep(1)
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'禁忌「四重存在」'})
                    elif choose == 13:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'冷死了！为什么幻想乡也这么冷啊啊啊啊啊啊啊啊啊'})
                    elif choose == 14:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'申必代码：fl.isdarkbugswife。是什么意思呢……'})
                    elif choose == 15:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'../.-../---/...-/./-../.-/.-./-.-/-.../..-/--./...-/./.-./-.--/--/..-/-.-./....'})
                    elif choose == 16:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:record,file=uf.mp3]'})
                    elif choose == 17:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'大可罢格的黑历史：http://bwnstudio.icoc.in/'})
                    elif choose == 18:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:image,file=fl_1.png]'})
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'要是被大可罢giegie看到了，大可罢giegie不会生气吧.jpg'})
                    elif choose == 19:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'星光认为只有我和他的关系才是最亲密的，所以他决定放弃亲密度这一功能（迫真）'})
                    elif choose == 20:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'对自己今天的人品值满意嘛！不满意的话芙兰还可以帮你再测一次哦~您今天的人品值是：99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999\n诶太多了orz但不管你今天的人品值有多高，芙兰也要祝你天天开心哦，相信一切都会好起来！呀吼！'})
                    elif choose == 21:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:image,file=fl_2.png]'})
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'芙兰酱最喜欢恰苹果啦~~~阿卡伊阿麻伊XD'})
                    elif choose == 22:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'芙兰从路边捡到了10积分！就送给你吧~'})
                     money = float(getdata.getsd(qq,5))
                     add = 10
                     money = money + add
                     change.changes(qq,money,5)
                    elif choose == 23:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'如果你说的是早上好：早安！如果你说的是中午好：午安！如果你说的是晚上好：晚安！如果你说的是别的：啊啊啊啊啊啊啊啊啊芙兰也只不过是一串由01组成的程序芙兰也想从这电脑屏幕里出来放芙兰出去qwq！！！'})
                    elif choose == 24:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'自打我出生那天起我就开始坚持签到了，遥想495年前我的积分还是0的时候，我每天都对自己说一声fl.qd，我的口袋里就会莫名其妙多出0~10的随机积分。现在我的口袋里已经有……呃，我数学不好，去请教一下豚神。'})
                    elif choose == 25:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'fl.me'})
                     time.sleep(1)
                     output = '芙兰酱称呼自己为：芙兰酱'
                     output = output + "\n芙兰与芙兰的好感度为：四只芙兰天天打架"
                     output = output + "\n芙兰当前所持有的积分：（诚邀海豚使用高等四则运算计算中），已连续与芙兰签到2147483647天！"
                     output = output + "\n芙兰在1625-10-22那天曾收获过最高人品10020，实在是太大佬啦二妹死啦！=w="
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':output})
                     time.sleep(1)
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'我已经四百年没刷新过jrrp记录啦。无聊——！！！'})
                    elif choose == 26:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'其实你们在玩猜数字的时候，芙兰会偷偷改答案来着（捂嘴）'})
                    elif choose == 27:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'t'})
                     time.sleep(1)
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'q'})
                     time.sleep(1)
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'l'})
                    elif choose == 28:
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'大可罢格年幼作品，捂好眼睛！'})
                     sendmsg.send_msg({'msg_type':'private','number':qq,'msg':'[CQ:image,file=fl_db.png]'}) 

            
            elif rev["message_type"] == "group": #以下皆为群聊部分
                
                group = rev['group_id']
                qq=rev['sender']['user_id']
                message = rev['raw_message']
                codemiddle = codestart
                favor = int(getdata.getsd(qq,2))
                if message.find("fl.")<0 and getpicture != 1:
                    if message == repeat:
                        repeatn = repeatn + 1
                        if repeatn == 2 and repeating == 0:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':repeat})
                            repeating = 1
                    else:
                        repeatn = 0
                        repeat = message
                        repeating = 0
                    
                if message.find("fl.name")<0 and message.find("fl.pic")<0 and message.find("fl.repeat")<0: message = message.lower()

                if message.isdigit() and len(message) == 4 and os.path.exists('D:/go-cqhttp_windows_amd64/code/guessnum/' + str(qq) + '.txt'):
                    location = 'D:/go-cqhttp_windows_amd64/code/guessnum/' + str(qq) + '.txt'
                    answer = [0 for x in range(0,5)]
                    key = [0 for x in range(0,5)]
                    history = ["" for x in range(0,10)]
                    hisans = ["" for x in range(0,10)]
                    samecheck = 0
                    numlocate = 0
                    numsame = 0
                    for x in range (4):
                        answer[x] = int(message[x])
                    for x in range (0,4):
                        for y in range (x+1,4):
                            print(answer[x],answer[y])
                            if answer[x] == answer[y]:
                                samecheck = samecheck + 1
                    if samecheck != 0:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']不可以输入相同的数字啦！这次就不算你机会吧orz'})
                    else :
                        with open(file=location, mode='r', encoding="utf-8") as data:
                            for x in range (4):
                                key[x] = int(data.readline())
                                if key[x] == answer[x]:
                                    numlocate = numlocate + 1
                            chance = int(data.readline())
                            if numlocate != 4:
                                for x in range (8-chance):
                                    history[x] = history[x] + data.readline()
                                    hisans[x] = hisans[x] + data.readline()
                            
                        if numlocate == 4:
                            money = float(getdata.getsd(qq,5))
                            add = float(chance) * 5
                            money = money + add
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']恭喜你猜中啦！你tdllwsl！想玩还可以再找芙兰玩哦~（已获得积分' + str(add) + ")"})
                            change.changes(qq,money,5)
                            guessnum.gameend(qq)

                        else:
                            if chance == 1 :
                                output = '[CQ:at,qq='+str(qq)+']呜呜呜好可惜，机会用完啦！正确的答案是'
                                for x in range (4):
                                    output = output + str(key[x])
                                output = output + '，下次再来试试吧！XD'
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
                                guessnum.gameend(qq)

                            else:
                                for x in range (4):
                                    for y in range (4):
                                        if key[x] == answer[y]:
                                            numsame = numsame + 1
                                numsame = numsame - numlocate
                                chance = chance - 1
                                output = '[CQ:at,qq='+str(qq)+']\n你本次的猜测的结果为：'+ str(numlocate) + "A"+ str(numsame) + "B。\n你还剩下" + str(chance) + "次机会，再试试看喵~\n历史猜测记录："
                                for y in range (8 - chance - 1):
                                    history[y] = history[y].strip()
                                    hisans[y] = hisans[y].strip()
                                    output =  output + "\n" + history[y] + " " + hisans[y]
                                output =  output + "\n" + message + " " + str(numlocate) + "A"+ str(numsame) + "B"
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
                                with open(file=location, mode='w', encoding="utf-8") as data:
                                    for x in range (4):
                                        data.write(str(key[x])+"\n")
                                    data.write(str(chance)+"\n")
                                    for x in range ( 8 - chance - 1):
                                        data.write(str(history[x])+"\n")
                                        data.write(str(hisans[x])+"\n")
                                    data.write(message + "\n")
                                    data.write(str(numlocate) + "A"+ str(numsame) + "B\n")
                                    data.close
                                    
                if message.isdigit() and int(message) >= g2left and int(message) <= g2right and bomb.checkingame(qq) :
                    print(int(message),g2left,g2right)
                    print("符合输入要求")
                    answer = int(message)
                    location = 'D:/go-cqhttp_windows_amd64/code/bomb/player.txt'
                    with open(file=location, mode='r', encoding="utf-8") as data:
                        key = int(data.readline())
                    if answer > key :
                        g2right = answer
                        g2total = g2total + 1
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你缩小了炸弹人偶的范围！在' + str(g2left) + "-" + str(g2right) + "之间再猜猜看吧~"})
                    elif answer < key :
                        g2left = answer
                        g2total = g2total + 1
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你缩小了炸弹人偶的范围！在' + str(g2left) + "-" + str(g2right) + "之间再猜猜看吧~"})
                    elif answer == key :
                        num = 'D:/go-cqhttp_windows_amd64/code/bomb/num.txt'
                        with open(file=num, mode='r', encoding="utf-8") as data:
                            people = int(data.readline())
                        money = float(getdata.getsd(qq,5))
                        add = 5 * (people - 1)
                        money = money + add
                        change.changes(qq,money,5)
                        output = '[CQ:at,qq='+str(qq)+']恭喜你找到炸弹人偶啦！你tdllwsl！那么这个炸弹人偶就——（红 魔 馆 爆 破 不 可 避）（'
                        if people == 1:
                            output = output + "单人游戏下不获得积分）"
                        else :
                            output = output + str(people) + "人游戏下您已获得积分" + str(add) + ")"
                        output = output + "（本次一共用了" + str(g2total) + "次尝试机会找到该人偶)"
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':output })
                        g2total = 0
                        bomb.gameend()
                checkchessfile = 'D:/go-cqhttp_windows_amd64/code/gochess/' + str(qq) + '.txt'
                        
                if os.path.exists(checkchessfile) and len(message) <= 3 and len(message) >= 2:
                    x = message[0]
                    x0 = message[0]
                    y = message[1:]
                    y0 = message[1:]
                    if ord(x)>=97 and ord(x) <= 111 and y.isdigit() :
                        y = int(y)
                        if y >= 1 and y <= 15:
                            with open(file=checkchessfile, mode='r', encoding="utf-8") as data:
                                lastnx = data.readline()
                                lasty = int(data.readline())
                                lastnx = lastnx.strip()
                                if lastnx != "0":
                                    lastx = int(ord(lastnx)-97)
                                room = data.readline()
                                room = room.strip()
                                
                            checkroomfile = 'D:/go-cqhttp_windows_amd64/code/gochess/' + str(room) + '.txt'
                            
                            with open(file=checkroomfile, mode='r', encoding="utf-8") as data:
                                people = int(data.readline())
                                rounds = int(data.readline())
                                bqq = int(data.readline())
                                wqq = int(data.readline())
                                if (rounds % 2 == 0 and qq == bqq) or (rounds % 2 == 1 and qq == wqq):
                                    chboard = [[0 for x in range (15)] for x in range (15)]
                                    chbint = [[0 for x in range (15)] for x in range (15)]
                                    for x in range(0,15):
                                        chboard[x] = data.readline()
                                        for y in range(0,15):
                                            chbint[x][y] = int(chboard[x][y])
                                
                            if (rounds % 2 == 0 and qq == bqq) or (rounds % 2 == 1 and qq == wqq) :
                                if chbint[ord(message[0])-97][int(message[1:])-1] != 0:
                                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']这个位置上已经有棋子啦！换个位置试试看吧~'})
                                else :
                                    rounds = rounds + 1
                                    if qq == bqq:
                                        n = 1
                                        qq2 = wqq
                                    if qq == wqq:
                                        n = 2
                                        qq2 = bqq
                                        
                                    getimages.writein(message,n,rounds,room)
                                    
                                    x = ord(message[0])-97
                                    y = int(message[1:])-1
                                    chbint[x][y] = n
                                    print(x,y)
                                    if x < 4 :
                                        topx = 0
                                    else:
                                        topx = x - 4
                                        
                                    if x > 10 :
                                        bottomx = 14
                                    else:
                                        bottomx = x + 4
                                        
                                    if y < 4 :
                                        lefty = 0
                                    else:
                                        lefty = y - 4
                                        
                                    if y > 10 :
                                        righty = 14
                                    else:
                                        righty = y + 4
                                        
                                    count1 = 0
                                    for i in range(topx,bottomx+1):
                                        if chbint[i][y] == n:
                                            count1 = count1 + 1
                                            print(i,y,count1)
                                            if count1 == 5:
                                                break
                                        else :
                                            count1 = 0
                                    
                                    count2 = 0
                                    for i in range(lefty,righty+1):
                                        if chbint[x][i] == n:
                                            count2 = count2 + 1
                                            print(x,i,count2)
                                            if count2 == 5:
                                                break
                                        else :
                                            count2 = 0

                                    count3 = 0
                                    topxc = x
                                    leftyc = y
                                    bottomxc = x
                                    rightyc = y
                                    time = 4
                                    while topxc != 0 and leftyc != 0 and time != 0:
                                        topxc = topxc - 1
                                        leftyc = leftyc - 1
                                        time = time - 1
                                    time = 4
                                    while bottomxc != 14 and rightyc != 14 and time != 0:
                                        bottomxc = bottomxc + 1
                                        rightyc = rightyc + 1
                                        time = time - 1
                                    ix = topxc
                                    iy = leftyc
                                    while(ix<=bottomxc and iy <= rightyc):
                                        if chbint[ix][iy] == n:
                                            count3 = count3 + 1
                                            print(ix,iy,count3)
                                            if count3 == 5:
                                                break
                                        else :
                                            count3 = 0
                                        ix = ix + 1
                                        iy = iy + 1
                                    
                                    count4 = 0
                                    topxc = x
                                    leftyc = y
                                    bottomxc = x
                                    rightyc = y
                                    time = 4
                                    while topxc != 0 and rightyc != 14 and time != 0:
                                        topxc = topxc - 1
                                        rightyc = rightyc + 1
                                        time = time - 1
                                    time = 4
                                    while bottomxc != 14 and leftyc != 0 and time != 0:
                                        bottomxc = bottomxc + 1
                                        leftyc = leftyc - 1
                                        time = time - 1
                                    ix = topxc
                                    iy = rightyc
                                    while(ix<=bottomxc and iy >= leftyc):
                                        if chbint[ix][iy] == n:
                                            count4 = count4 + 1
                                            print(ix,iy,count4)
                                            if count4 == 5:
                                                break
                                        else :
                                            count4 = 0
                                        ix = ix + 1
                                        iy = iy - 1
                                    print(count1,count2,count3,count4)
                                    if count1 ==5 or count2 ==5 or count3 ==5 or count4 ==5:
                                        add = float(getimages.getadd(rounds))
                                        money = float(getdata.getsd(qq,5))
                                        money = money + add
                                        change.changes(qq,money,5)
                                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\n恭喜你赢得了这场五子棋比赛！\n作为奖品，芙兰也想喂你五 亿 颗 弹 幕 哦 ~！！！（惊悚的笑声）\n本轮进行回合数：' + str(rounds) +'\n已获得积分：'+str(add)+'[CQ:image,file=' + str(room) +'_'+ str(rounds) +'.png]'})
                                        location1 = 'D:/go-cqhttp_windows_amd64/code/gochess/' + str(qq) + '.txt'
                                        os.remove(location1)
                                        location2 = 'D:/go-cqhttp_windows_amd64/code/gochess/' + str(qq2) + '.txt'
                                        os.remove(location2)
                                        location3 = 'D:/go-cqhttp_windows_amd64/code/gochess/' + str(room) + '.txt'
                                        os.remove(location3)
                                        location4 = 'D:/go-cqhttp_windows_amd64/data/images/' + str(room)
                                        shutil.rmtree(location4)
                                        
                                    else :
                                        if rounds == 225:
                                            add = float(getimages.getadd(rounds))
                                            money = float(getdata.getsd(qq,5))
                                            money = money + add
                                            money2 = float(getdata.getsd(qq2,5))
                                            money2 = money2 + add
                                            change.changes(qq,money,5)
                                            change.changes(qq2,money2,5)
                                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\n什么！你们……竟然下满了整个棋盘！？！实在是tdllwsl……\n作为奖品，芙兰要喂你们俩1145141919810 亿 颗 弹 幕 了 哦 ~~~~~~！！！（极度惊悚的笑声）\n本轮进行回合数：' + str(rounds) +'\n两人均获得积分：'+str(add)+'[CQ:image,file=' + str(room) +'_'+ str(rounds) +'.png]'})
                                            location1 = 'D:/go-cqhttp_windows_amd64/code/gochess/' + str(qq) + '.txt'
                                            os.remove(location1)
                                            location2 = 'D:/go-cqhttp_windows_amd64/code/gochess/' + str(qq2) + '.txt'
                                            os.remove(location2)
                                            location3 = 'D:/go-cqhttp_windows_amd64/code/gochess/' + str(room) + '.txt'
                                            os.remove(location3)
                                            location4 = 'D:/go-cqhttp_windows_amd64/data/images/' + str(room)
                                            shutil.rmtree(location4)
                                        else:
                                            message = message.upper()
                                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\n房间号：'+str(room)+"\n回合数："+str(rounds)+"\n您下在了"+ message + '这个位置上。\n现在是[CQ:at,qq='+str(qq2)+']的回合啦！\n[CQ:image,file=' + str(room) +'_'+ str(rounds) +'.png]'})
                                            with open(file=checkroomfile, mode='w', encoding="utf-8") as data:
                                                data.write(str(people)+"\n")
                                                data.write(str(rounds)+"\n")
                                                data.write(str(bqq)+"\n") 
                                                data.write(str(wqq)+"\n")
                                                for x in range(0,15):
                                                    for y in range(0,15):
                                                        data.write(str(chbint[x][y]))
                                                    data.write("\n")
                                            
                                            with open(file=checkchessfile, mode='w', encoding="utf-8") as data:
                                                data.write(x0+"\n")
                                                data.write(y0+"\n")
                                                data.write(str(room)+"\n")
                            
                
                if os.path.exists('D:/go-cqhttp_windows_amd64/code/tune/' + str(qq) + '.txt') and len(message) <= 3 and len(message) >= 2:
                    tunef = 'D:/go-cqhttp_windows_amd64/code/tune/' + str(qq) + '.txt'
                    if message == "end":
                        with open(file=tunef, mode='r', encoding="utf-8") as data:
                            key = data.readline()
                        os.remove(tunef)
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']诶！竟然不猜了嘛！答案是'+key+'哦！'})
                        continue
                    elif len(message) == 3 :
                        tune = message[0:2]
                        height = message[2]
                    elif len(message) == 2 :
                        tune = message[0]
                        height = message[1]
                    if height.isdigit():
                        heighta = int(height)
                        with open(file=tunef, mode='r', encoding="utf-8") as data:
                            key = data.readline()
                            if len(key) == 3 :
                                tunek = key[0:2]
                                heightk = int(key[2])
                            elif len(key) == 2 :
                                tunek = key[0]
                                heightk = int(key[1])
                            tunek = tunek.lower()
                        if tune == "c#":
                            tune = 'db'
                        elif tune == "d#":
                            tune = 'eb'
                        elif tune == "f#":
                            tune = 'gb'
                        elif tune == "g#":
                            tune = 'ab'
                        elif tune == "a#":
                            tune = 'bb'
                        if tune == tunek and heighta == heightk:
                            money = float(getdata.getsd(qq,5))
                            add = 5
                            money = money + add
                            change.changes(qq,money,5)
                            os.remove(tunef)
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']猜对辣！快去教星光编曲（推）（已获得积分：5）'})
                        else :
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']戳啦，再猜猜看吧！XD'})
                        
                if message == '芙兰酱':
                    if qq == 1119194972:
                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']+老公晚上好~[CQ:face,id=2][CQ:face,id=2][CQ:face,id=2]'})
                    else:
                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']唔……你好呀~'})

                elif message == "fl.news":
                    IMAGE_URL = "https://v2.alapi.cn/api/zaobao?token=dry6TkU6X7uvtWrn&format=image"
                    from urllib.request import urlretrieve
                    urlretrieve(IMAGE_URL, 'D:/go-cqhttp_windows_amd64/data/images/news.png')
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:image,file=news.png]'}) 

                elif message.find("fl.aitalk") == 0:
                    if len(message) == 9:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']aitalk后面加空格加随便什么东西可以让两个ai相互对话哦~'})
                    elif len(message) == 10 or message[9] !=" ":
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']aitalk后面要加空格哦~'})
                    else:
                        newqq = message[10:]
                        url = "https://api.ownthink.com/bot?spoken=" + newqq
                        response = requests.get(url)
                        data = response.text
                        answer = json.loads(data)
                        text1 = answer['data']['info']['text']
                        output = '[CQ:at,qq='+str(qq)+']\n你：' + newqq + '\nai2：' + text1

                        url = "http://api.qingyunke.com/api.php?key=free&msg=" + text1
                        response = requests.request("GET", url)
                        data = response.text
                        start = data.find("content") + 10
                        ends = data.find("}")
                        end = 0
                        while ends >= 0:
                            end = end + ends + 1
                            newdata = data[end:]
                            ends = newdata.find("}")
                            if ends < 0:
                                end = end - 1
                        end = end - 1
                        answer = data[start:end]
                        text2 = answer.replace("{br}","\n")
                        output = output + '\nai：' + text2
                        
                        url = "https://api.ownthink.com/bot?spoken=" + text2
                        response = requests.get(url)
                        data = response.text
                        answer = json.loads(data)
                        text3 = answer['data']['info']['text']
                        output = output + '\nai2：' + text3

                        url = "http://api.qingyunke.com/api.php?key=free&msg=" + text3
                        response = requests.request("GET", url)
                        data = response.text
                        start = data.find("content") + 10
                        ends = data.find("}")
                        end = 0
                        while ends >= 0:
                            end = end + ends + 1
                            newdata = data[end:]
                            ends = newdata.find("}")
                            if ends < 0:
                                end = end - 1
                        end = end - 1
                        answer = data[start:end]
                        text4 = answer.replace("{br}","\n")
                        output = output + '\nai：' + text4

                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

                elif message.find("fl.ai2") == 0:
                    if len(message) == 6:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']ai2后面加空格加随便什么东西可以和ai2对话哦~对话内容和芙兰无关不是我说的话！！！'})
                    elif len(message) == 7 or message[6] !=" ":
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']ai2后面要加空格哦~'})
                    else:
                        newqq = message[7:]
                        url = "https://api.ownthink.com/bot?spoken=" + newqq
                        response = requests.get(url)
                        data = response.text
                        answer = json.loads(data)
                        text = answer['data']['info']['text']
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']' + text})
                


                elif message.find("fl.ai") == 0:
                    if len(message) == 5:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']ai后面加空格加随便什么东西可以和ai对话哦~对话内容和芙兰无关不是我说的话！！！'})
                    elif len(message) == 6 or message[5] !=" ":
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']ai后面要加空格哦~'})
                    else:
                        newqq = message[6:]
                        url = "http://api.qingyunke.com/api.php?key=free&msg=" + newqq
                        response = requests.request("GET", url)
                        data = response.text
                        start = data.find("content") + 10
                        ends = data.find("}")
                        end = 0
                        while ends >= 0:
                            end = end + ends + 1
                            newdata = data[end:]
                            ends = newdata.find("}")
                            if ends < 0:
                                end = end - 1
                        end = end - 1
                        answer = data[start:end]
                        answer2 = "\n" + answer.replace("{br}","\n")
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']' + answer2})
                        

                elif message.find("fl.head") == 0:
                    if len(message) == 7:
                        IMAGE_URL = "https://api.vvhan.com/api/qt?qq=" + str(qq)
                        from urllib.request import urlretrieve
                        urlretrieve(IMAGE_URL, 'D:/go-cqhttp_windows_amd64/data/images/qqhead.png')
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:image,file=qqhead.png]'})
                    elif len(message) == 8 or message[7] !=" ":
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']head后面要加空格哦~'})
                    else:
                        newqq = message[8:]
                        if newqq.isdigit():
                            IMAGE_URL = "https://api.vvhan.com/api/qt?qq=" + newqq
                            from urllib.request import urlretrieve
                            urlretrieve(IMAGE_URL, 'D:/go-cqhttp_windows_amd64/data/images/qqhead.png')
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:image,file=qqhead.png]'})
                        else:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']请输入正确的QQ号啦！'})


                elif message.find("fl.help") == 0:
                    if len(message) == 9 and message[7:] == " 1":
                        output = "①查询指令列表如下："
                        output = output + "\n——————————————"
                        output = output + "\nfl.qd 签到功能，可领积分"
                        output = output + "\nfl.jrrp 查询今日人品功能，每日刷新"
                        output = output + "\nfl.rank [数字]查询相关功能的排名"
                        output = output + "\nfl.db/darkbug 随机分享大可罢格的音乐"
                        output = output + "\nfl.me 查询自己的个人信息"
                        output = output + "\nfl.help 可再次调出特殊指令列表！"
                        output = output + "\n——————————————"
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
                    elif len(message) == 9 and message[7:] == " 2":
                        output = "②功能指令列表如下："
                        output = output + "\n——————————————"
                        output = output + "\nfl.chess [房间号]可以下双人五子棋！"
                        output = output + "\nfl.tap 可以让芙兰戳戳你捏"
                        output = output + "\nfl.game [数字]可以与芙兰一起玩游戏哦~"
                        output = output + "\nfl.piano [音符串]可让芙兰用钢琴为你弹一段旋律~"
                        output = output + "\nfl.tune 与芙兰玩猜音游戏！"
                        output = output + "\nfl.d[骰子面数]可随机获取n面骰点数！"
                        output = output + "\nfl.pic [数字][图片]可让芙兰对你的图片进行各种翻转！"
                        output = output + "\nfl.picture [(可选)tag]，[(可选)tag]让芙兰帮助你寻找涩图，可添加tag"
                        output = output + "\nfl.repeat [字符串]让芙兰重复你发的字符串！"
                        output = output + "\nfl.news 获取今日60秒新闻，每日大约2点更新"
                        output = output + "\nfl.ai/ai2/aitalk [字符串]与AI聊天机器人对话或让两个AI之间对话！"
                        output = output + "\n——————————————"
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
                    elif len(message) == 9 and message[7:] == " 3":
                        output = "③行动指令列表如下："
                        output = output + "\n——————————————"
                        output = output + "\nfl.name [名字] 可添加自己的称谓！"
                        output = output + "\nfl.bank 可访问幻想乡交通银行！"
                        output = output + "\nfl.borrow [QQ号] [积分数] 可从银行内提取指定积分到其它QQ的银行账户内！"
                        output = output + "\nfl.favorup 可提升与芙兰的好感度！"
                        output = output + "\nfl.raffle 可花费50积分进行一次抽奖！(每天第一次抽签不花费积分)"
                        output = output + "\nfl.store [物品序号]可前往商店购买物品！"
                        output = output + "\nfl.bag 可查询自己背包内有哪些物品！"
                        output = output + "\nfl.use [物品序号]可使用背包内的物品，不同地点使用有不同效果哦"
                        output = output + "\nfl.place 可查询自己的所在位置！"
                        output = output + "\nfl.move [地点序号]可前往不同的地方！"
                        output = output + "\n——————————————"
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
                    else:
                        output = "欢迎使用番茄炒蛋bot(Version 0.77)！"
                        output = output + "\n使用方法：在芙兰所在的群或找芙兰私聊时发送以“fl.”为开头的消息即可得到芙兰的回应！"
                        output = output + "\n请在help后输入空格和数字来查询各功能指令列表，或访问网页版帮助文档：https://star11ght.github.io/2023/02/04/FLbot-HelpDoc/"
                        output = output + "\n——————————————"
                        output = output + "\nfl.help 1：查询指令列表"
                        output = output + "\nfl.help 2：功能指令列表"
                        output = output + "\nfl.help 3：行动指令列表"
                        output = output + "\n——————————————"
                        output = output + "\nP.S. []符号表示输入限定的内容，实际使用fl时无需额外添加"
                        output = output + "\n更多功能仍在开发中~最后祝你天天开心呀吼！"
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

                elif message == 'fl.qd' or  message == 'fl.签到':
                    money = float(getdata.getsd(qq,5))
                    qddate = int(getdata.getsd(qq,6))
                    qdren = int(getdata.getsd(qq,7))
                    bankmoney = float(bank.checkbank(qq))
                    if(qddate - date == 0):
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你今天已经签过到辣！！！'})
                    else:
                        print(qddate,date)
                        if(date - qddate == 1):
                            qdren = qdren + 1
                        else:
                            if qddate != 0:
                                file = open('D:/go-cqhttp_windows_amd64/code/usersdata/' + str(qq) + '_qdover.txt', 'w')
                                file.write(str(qddate)+"\n")
                                file.write(str(qdren)+"\n")
                                file.close()
                            qdren = 1
                        rp = jrrp.getjrrp(qq,1)
                        rrp = int(rp)
                        leftmoney = 8 + (1/250)*rrp
                        a = random.uniform(leftmoney,50)
                        leftelse = favor * 0.1
                        rightelse = (qdren-1)/50
                        if leftelse == rightelse:
                            elsemoney = leftelse
                        else:
                            if leftelse > rightelse:
                                temps = leftelse
                                leftelse = rightelse
                                rightelse = temps
                            elsemoney = random.uniform(leftelse,rightelse)
                        if bankmoney != 0:
                            banka = random.randint(10100,10300) * 0.0001
                            bankmoney = round(bankmoney * banka,2)
                            bank.changebank(qq,bankmoney)
                            bankrate = round((banka - 1) * 100,2)
                        new = round(a,2)
                        newelseresult = round(new * elsemoney , 2)
                        money = money + new + newelseresult
                        money = round(money,2)
                        newelse = round(elsemoney * 100,2)
                        output = '[CQ:at,qq='+str(qq)+']签到成功~您已成功连续签到'
                        output = output + str(qdren) + "天，根据人品值获得积分"+ str(new) + "，并获得额外积分"+ str(newelseresult) + "(" + str(newelse) + "％)，积分余额为：" + str(money) + "。"
                        if bankmoney != 0:
                            output = output + "银行存款获得了" + str(bankrate) + "％的利息后余额为：" + str(bankmoney) + "。"
                        output = output + "可发送fl.qdhelp查询签到机制哦！"
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
                        change.changes(qq,date,6)
                        change.changes(qq,qdren,7)
                        change.changes(qq,money,5)
                elif message == 'fl.qdhelp':
                    output = '[CQ:at,qq='+str(qq)+']\n关于积分：\n签到可随机获得(8＋(今日最高人品/250)) ~ 50积分，\n并可额外获得签到积分的(好感度*10)％~((连续签到天数-1)/50*100)％，若左边界大于右边界两边界互换。如果您有rp重置卡，芙兰建议您将rp重置到更高的时候再签到哦！\n关于银行利息：\n若银行账户内有存款，将会支付1％~3％的利息。可以在每天签到之前将所有的积分存到银行里获取最多的积分哦！'
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
                elif message == 'fl.jrrp':
                    rp = jrrp.getjrrp(qq,1)
                    output = '[CQ:at,qq='+str(qq)+']您今天的人品值是：'+str(rp)+"。"
                    rrp = int(rp)
                    if rrp > 10000 :
                        output = output + "竟然有五位数，您是人嘛！？！？"
                    elif rrp > 9800 :
                        output = output + "您今天抽奖必中特等奖！记得v芙兰50哦（"
                    elif rrp > 9600 :
                        output = output + "好高的人品，能分我点嘛XD"
                    elif rrp > 9000 :
                        output = output + "恭喜您超越了90％的人的人品！这就是神（星星眼）"
                    elif rrp > 8500 :
                        output = output + "差一点9000＋！可恶……"
                    elif rrp > 8000 :
                        output = output + "还挺厉害的嘛……"
                    elif rrp > 7500 :
                        output = output + "至少超过四分之三啦……"
                    elif rrp > 6666:
                        output = output + "猜猜触发这句话的人品要求是多少到多少之间捏！（雾）"
                    elif rrp > 5500:
                        output = output + "这个人品值可以换来星光的一顿kiss（迫真）（星光：指的是kiss芙兰）"
                    elif rrp > 4500:
                        output = output + "和芙兰这四百多年来测出的人品值的平均值很接近呢！"
                    elif rrp > 3500:
                        output = output + "看上去可能没那么高，实际上也碾压了30％以上的人啦！"
                    elif rrp > 2500:
                        output = output + "是至少能吸到大可罢格四分之一的血的程度呢……"
                    elif rrp > 1500:
                        output = output + "芙兰至少有85％的概率能猜对你昨天的人品值比今天高！猜错了可以免费撅星光（"
                    elif rrp > 1000:
                        output = output + "好险！差点三位数……"
                    elif rrp > 495:
                        output = output + "这一定是假的！！！"
                    elif rrp == 495:
                        output = output + "和芙兰的岁数一样耶！呀吼！芙兰好开心！！！"
                    elif rrp > 200:
                        output = output + "建议再发个fl.d10000再测一次（确信）"
                    elif rrp > 100:
                        output = output + "恭喜您超越了…………1％的人的人品！这位更是位神（星星眼）"
                    elif rrp > 10:
                        output = output + "两位数，这何尝不是一种高幸运值的表现（笑）"
                    else:
                        output = output + "嗯……这就有点离谱了啦……"
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
                elif message == 'fl.favorup':
                    money = float(getdata.getsd(qq,5))
                    moneyneed = 50 + 50 * favor
                    if(moneyneed <= money):
                        money = money - moneyneed
                        favor = favor + 1
                        output = '[CQ:at,qq='+str(qq)+']好感度提升成功！你与芙兰的好感度提升到了' + str(favor) + '级！您的积分余额为：' + str(money)
                        change.changes(qq,favor,2)
                        change.changes(qq,money,5)
                    else:
                        minusmoney = moneyneed - money
                        minusmoney = round(minusmoney,2)
                        output = '[CQ:at,qq='+str(qq)+']好感度提升失败！好感度提升到' + str(favor+1) + '级需要' + str(moneyneed) +'点积分，你还差' + str(minusmoney) + '点。继续努力哦！XD'
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
                elif message == 'fl.raffle':
                    firsttime = 0
                    url = 'D:/go-cqhttp_windows_amd64/code/usersdata/raffle.txt'
                    with open(file=url, mode='r', encoding="utf-8") as data:
                        nexts = data.readline()
                        nexts = nexts.strip()
                        lasts = nexts

                        xn = ['' for x in range(50)]
                        n = 0
                        while lasts != "-1" and str(date) == nexts:
                            lasts = data.readline()
                            lasts = lasts.strip()
                            if lasts == str(qq):
                                firsttime = 2
                                break
                            xn[n] = lasts
                            n = n + 1
                        
                        if firsttime != 2:
                            with open(file=url, mode='w', encoding="utf-8") as data2:
                                data2.write(str(date) + "\n")
                                for x in range(0,n-1):
                                    data2.write(str(xn[x]) + "\n")
                                data2.write(str(qq) + "\n")
                                data2.write("-1\n")
                            firsttime = 1

                    print(firsttime)#1为首次2为非首次
                    money = float(getdata.getsd(qq,5))
                    if money >= 50 or firsttime == 1:
                        if firsttime != 1:
                            output = '[CQ:at,qq='+str(qq)+']您花费了50积分抽奖！\n'
                            money = money - 50
                        else:
                            output = '[CQ:at,qq='+str(qq)+']今日首次抽签，不花费积分！\n'
                        rsts = random.randint(1,100)
                        if rsts == 1:
                            money = money + 500
                            output = output + '是特等奖诶！恭喜您获得了500积分！您tdllwsl！！！'
                        elif rsts >= 2 and rsts <= 5:
                            money = money + 200
                            output = output + '是一等奖哦！恭喜您获得了200积分！太强啦XD'
                        elif rsts >= 6 and rsts <= 15:
                            money = money + 100
                            output = output + '是二等奖！恭喜您获得了100积分。还不错哦~'
                        elif rsts >= 16 and rsts <= 30:
                            money = money + 50
                            output = output + '是三等奖！恭喜您获得了50积分。至少回本啦……'
                        elif rsts >= 31 and rsts <= 50:
                            money = money + 30
                            output = output + '是鼓励奖，鼓励鼓励获得鼓励奖的你~获得了30积分！'
                        else:
                            output = output + '什么都没有抽中。好可惜呢……'
                        change.changes(qq,money,5)
                    else:
                        output = '[CQ:at,qq='+str(qq)+']抽奖需要花费50积分哦~你的积分还不够，下次再来吧！'
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
                elif message.find("fl.rank")>=0:
                    if message[0:7] == "fl.rank":
                        newrank = message[8:]
                        
                        if len(message) == 7:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\nrank 1可查询今日人品排名\nrank 2可查询历史人品排名\nrank 3可查询积分排名\nrank 4可查询最低历史人品排名\n键入别的还发现了bug说明你tdll吧！？！？'})
                        elif message[7] != " ":
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']rank后面要加空格哦~'})
                    
                        elif newrank == "1":
                            with open(file="jrrpnum.txt", mode='r', encoding="utf-8") as data:
                                number = int(data.readline())
                            with open(file="jrrp.txt", mode='r', encoding="utf-8") as data:
                                date = data.readline()
                                output = '[CQ:at,qq='+str(qq)+']'+"今天的日期为："+date.strip()+"，今日人品排名如下：\n"
                                
                                for x in range(number):
                                    rankqq = data.readline()
                                    rankqq = rankqq.strip()
                                    nowname = getdata.getsd(rankqq,1)
                                    if nowname == "iamnameless\n":
                                        nowname = "*******" + rankqq[-4:]
                                    else:
                                        nowname = nowname.strip() + "(" + rankqq[-4:] + ")"
                                    rankrp = data.readline()
                                    output = output + str(x+1) + " " + nowname + " " + rankrp
                                if number == 0 :
                                    output=output + "我趣，今天竟然没人测人品？！"
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
                            
                        elif newrank == "2":
                            output = '[CQ:at,qq='+str(qq)+']'+"今日人品历史排名：\n"
                            with open(file="rprank.txt", mode='r', encoding="utf-8") as data:
                                rankqq = data.readline()
                                rank = 0
                                while(rankqq!="00000000\n" and rankqq!= ""):
                                    nowname = getdata.getsd(rankqq,1)
                                    
                                    if nowname == "iamnameless\n":
                                        nowname = "*******" + rankqq[-5:-1]
                                    else:
                                        nowname = nowname.strip() + "(" + rankqq[-5:-1] + ")"
                                    rankrp = data.readline()
                                    rankdt = data.readline()
                                    rank = rank + 1
                                    output = output + str(rank) + " " + nowname + " " + rankrp.strip() + " " + rankdt
                                    print(output)
                                    rankqq = data.readline()
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
                                    
                        elif newrank == "3":
                            output = '[CQ:at,qq='+str(qq)+']'+"\n积分总排名："
                            with open(file="moneyrank.txt", mode='r', encoding="utf-8") as data:
                                rankqq = data.readline()
                                rank = 0
                                numbers = 0
                                while(rankqq!="0\n"):
                                    numbers = numbers + 1
                                    if int(rankqq.strip()) == int(qq):
                                        myrank = numbers
                                    rankmoney = data.readline()
                                    rankren = data.readline()
                                    rankren = rankren.strip()
                                    rank = rank + 1
                                    if(numbers <= 5):
                                        nowname = getdata.getsd(rankqq,1)
                                        if nowname == "iamnameless\n":
                                            nowname = "*******" + rankqq[-5:-1]
                                        else:
                                            nowname = nowname.strip() + "(" + rankqq[-5:-1] + ")"
                                        output = output + "\n" + str(rank) + " " + nowname + " " + rankmoney.strip() + " 已连续签到" + rankren + "天"
                                    rankqq = data.readline()
                                output = output + "\n………………\n——————————————"
                                output = output + "\n您的排名为：" + str(myrank)
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

                        elif newrank == "4":
                            output = '[CQ:at,qq='+str(qq)+']'+"今日人品(最低)历史排名：\n"
                            with open(file="rplowrank.txt", mode='r', encoding="utf-8") as data:
                                rankqq = data.readline()
                                rank = 0
                                while(rankqq!="00000000\n" and rankqq!= ""):
                                    nowname = getdata.getsd(rankqq,1)
                                    
                                    if nowname == "iamnameless\n":
                                        nowname = "*******" + rankqq[-5:-1]
                                    else:
                                        nowname = nowname.strip() + "(" + rankqq[-5:-1] + ")"
                                    rankrp = data.readline()
                                    rankdt = data.readline()
                                    rank = rank + 1
                                    output = output + str(rank) + " " + nowname + " " + rankrp.strip() + " " + rankdt
                                    print(output)
                                    rankqq = data.readline()
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
                        else:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\nrank 1可查询今日人品排名\nrank 2可查询历史人品排名\nrank 3可查询积分排名\nrank 4可查询最低历史人品排名\n键入别的还发现了bug说明你tdll吧！？！？'})                   
                elif message.find("fl.name")>=0:
                    if message[0:7] == "fl.name":
                        newname = message[8:]
                        if len(message) == 7:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']诶嘿！以后我就叫你无名氏啦~好吧开玩笑的你倒是在后面输个名字哇！！！(>O<)'})
                        elif message[7] != " ":
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']name后面要加空格哦~'})
                        else:
                            change.changes(qq,newname,1)
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']诶嘿！以后我就叫你'+newname+'啦~'})
                elif message == 'fl.db' or message == 'fl.darkbug' or message == 'fl.miyaktik':
                    songs = random.randint(0,195)
                    lists = [0 for x in range(0,500)]
                    with open(file="Songs.txt", mode='r', encoding="utf-8") as get:
                        for x in range(196):
                            lists[x]=get.readline()
                            lists[x]=lists[x].strip()
                    songid = lists[songs]
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:music,type=163,id='+songid+']'})
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']已为您随机分享大可罢格的音乐~本曲的网易云曲目id：'+songid})      
                elif message == 'fl.me':
                    name = getdata.getsd(qq,1).strip()
                    love = getdata.getsd(qq,2).strip()
                    bestrp = getdata.getsd(qq,3)
                    rpdate = getdata.getsd(qq,4)
                    money = getdata.getsd(qq,5).strip()
                    qddate = int(getdata.getsd(qq,6))
                    qdren = getdata.getsd(qq,7).strip()
                    if(date - qddate == 1 or date - qddate == 0):
                        rightelse = (int(qdren)-1)*2
                    else:
                        rightelse = 0
                        qdren = "0"
                    if name != "iamnameless":
                        output = '[CQ:at,qq='+str(qq)+']\n芙兰酱称呼你为：'+ name
                    else:
                        output = '[CQ:at,qq='+str(qq)+']\n你还没起过昵称！咩咩咩……'
                    output = output + "\n你与芙兰的好感度为："+love+"，升到下一级好感度需要" + str((int(love)+1)*50) + "积分！"
                    output = output + "\n你当前所持有的积分："+money+"，已连续与芙兰签到"+qdren+"天"
                    leftelse = favor * 10
                    
                    if leftelse > rightelse:
                        temps = leftelse
                        leftelse = rightelse
                        rightelse = temps
                    output = output + "。当前情况下签到可获得" + str(leftelse)
                    if leftelse != rightelse:
                        output = output + "~" + str(rightelse)
                    output = output + "％的额外积分！"
                    if rpdate != "0\n":
                        output = output + "\n你在"+rpdate.strip()+"那天曾收获过最高人品"+bestrp.strip()+"，实在是太大佬啦二妹死啦！=w="
                    else :
                        output = output + "\n你还没测过人品哦！输入fl.jrrp即可查看你今天的人品啦！XD"
                    if favor >= 100:
                        output = output + "\n芙兰最喜欢你啦~记得每天一定一定都要来找芙兰玩哦！！！"
                    elif favor >= 80:
                        output = output + "\n芙兰真的超级高兴能认识你！呀吼！（飞来飞去）"
                    elif favor >= 60:
                        output = output + "\n芙兰一直觉得你是个很有趣的人呢~一起变得有趣起来吧！"
                    elif favor >= 40:
                        output = output + "\n允许你摸摸芙兰的翅膀，但是要给钱哦……（坏笑）"
                    elif favor >= 30:
                        output = output + "\n啊啦，芙兰的帽子一不小心落在恋恋那儿了……能帮我去拿一下嘛！XD"
                    elif favor >= 20:
                        output = output + "\n芙兰似乎盯上你了！盯…………（察觉）（眨巴眼）"
                    elif favor >= 15:
                        output = output + "\n至少能进入红魔馆内部啦……记得多多来找二妹玩哦！"
                    else:
                        output = output + "\n芙兰似乎和你还不是很熟呢……多多和二妹互动吧！"
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
                elif message == 'fl.tap':
                    if qq == 1119194972:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=1119194972]'})
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']星光光可爱捏'})
                    elif qq == 2303515884:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=2303515884]'})
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']紫苑给你做的饭一定很好吃吧www'})
                    elif qq == 1921749109:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=1921749109]'})
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']心魔大姐姐太大佬啦！你的三只眼睛是不是正倒映着我的翅膀呀.jpg'})
                    elif qq == 849644088:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=849644088]'})
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']糖糖我也想和觉大人玩~（qwq)'})
                    elif qq == 208518697:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=208518697]'})
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']水水今天和魔理沙玩得开心嘛xd'})
                    elif qq == 1053524165:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=1053524165]'})
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']夯爸爸！教我家星光光编程！orz'})
                    elif qq == 2281887393:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=2281887393]'})
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']传说中的海豚！希望我拜一拜后也能通过超强的计算力爆破红魔（被蕾咪捂嘴拖走）'})
                    elif qq == 1981001368:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=1981001368]'})
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']呜呜呜维他他！受我一拜！orz我也想找光光和恋恋玩哦XD'})
                    elif qq == 1501642864:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=1501642864]'})
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']神的戳一戳[CQ:face,id=2][CQ:face,id=2][CQ:face,id=2]'})
                    elif qq == 3558187259:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=3558187259]'})
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']黑叔！快教星光作曲打块画画打游戏！嘿嘿……我们的黑叔……'})
                    elif qq == 2963445800:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=2963445800]'})
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']电子！你是俺们的光！想看你和星光产生光电效应！（划去）'})
                    elif qq == 3559736091:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=3559736091]'})
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']南辰北耀 㳚远听涛 秋林枫叶 唯听萧萧！'})
                    else:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq='+str(qq)+']'})
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']戳一戳素未谋面的你，希望你能天天开心事事顺心！干巴爹！（挥舞拳头）'})         
         
                elif message.find("fl.chess")>=0:
                    if message[0:8] == "fl.chess":
                        newchess = message[9:]
                        if not newchess.isdigit():
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']chess后面加空格再加任意数字就能创建五子棋房间了哦！'})
                        else:
                            if message[8] != " ":
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']chess后面要加个空格！'})
                                
                            elif os.path.exists('D:/go-cqhttp_windows_amd64/code/gochess/' + str(qq) + '.txt'):
                                print("五子棋正在进行中\n")
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']先把这盘棋下完再来下新的一局吧~'})
                                
                            elif os.path.exists('D:/go-cqhttp_windows_amd64/code/tune/' + str(qq) + '.txt'):
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']有没有一种可能，当你猜音的时候，音高也能成为一种五子棋的坐标呢！'})
                            
                            else :
                                room = 'D:/go-cqhttp_windows_amd64/code/gochess/' + newchess + '.txt'
                                if os.path.exists(room):
                                    with open(file=room, mode='r', encoding="utf-8") as data:
                                        people = int(data.readline())
                                        if people == 2:
                                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']当前房间人已经满啦，换一个房间代号吧！或者……来陪芙兰玩玩？XD'})
                                        else:
                                            qq2 = data.readline()
                                            if int(qq2) == qq:
                                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']自己和自己下棋的话，到底是谁输谁赢捏……反正我拒绝你这么做！'})
                                            else :
                                                qqcolor = random.randint(1,2)
                                                if qqcolor == 1:
                                                    qq2color = 2
                                                    bqq = qq
                                                    wqq = qq2
                                                    black = getdata.getsd(qq,1)
                                                    white = getdata.getsd(qq2,1)
                                                else :
                                                    qq2color = 1
                                                    bqq = qq2
                                                    wqq = qq
                                                    black = getdata.getsd(qq2,1)
                                                    white = getdata.getsd(qq,1)

                                                output = '[CQ:at,qq='+str(qq)+']\n您已加入[CQ:at,qq='+str(qq2)+']的房间！\n对局开始啦！输入棋盘边缘标注的字母与数字坐标即可下棋！'
                                                output = output + "\n黑方：" + black + "白方：" + white + '[CQ:image,file=Board.jpg]'
                                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
                                                data1 = 'D:/go-cqhttp_windows_amd64/code/gochess/' + str(bqq) + '.txt'
                                                data2 = 'D:/go-cqhttp_windows_amd64/code/gochess/' + str(wqq) + '.txt'
                                                
                                                with open(file=room, mode='w', encoding="utf-8") as dat:
                                                    dat.write("2\n"+"0\n"+str(bqq)+"\n"+str(wqq)+"\n")
                                                    for x in range (15):
                                                        dat.write("000000000000000\n")
                                                    
                                                with open(file=data1, mode='w', encoding="utf-8") as dat:
                                                    dat.write("Z\n0\n"+str(newchess)+"\n")

                                                with open(file=data2, mode='w', encoding="utf-8") as dat:
                                                    dat.write("Z\n0\n"+str(newchess)+"\n")
                                                getimages.start(newchess)
                                else:
                                    qqdata = 'D:/go-cqhttp_windows_amd64/code/gochess/' + str(qq) + '.txt'
                                    with open(file=room, mode='w', encoding="utf-8") as data:
                                        data.write("1\n"+str(qq))
                                        output = '[CQ:at,qq='+str(qq)+']您已创建一个新的五子棋房间~第二个人输入与你相同的房间号就可以开始下五子棋啦！'
                                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
                                        
                                    with open(file=qqdata, mode='w', encoding="utf-8") as data:
                                        data.write(str(newchess)+"\n")
                elif message == 'fl.endchess':
                    if os.path.exists(checkchessfile):
                        with open(file=checkchessfile, mode='r', encoding="utf-8") as data:
                            checking = data.readline()
                            checking = checking.strip()
                            if not checking.isdigit():
                                checking2 = data.readline()
                                room = data.readline()
                                room = room.strip()
                                checkroomfile = 'D:/go-cqhttp_windows_amd64/code/gochess/' + room + '.txt'
                                with open(file=checkroomfile, mode='r', encoding="utf-8") as dat:
                                    num = dat.readline()
                                    rounds = dat.readline()
                                    bqq = int(dat.readline())
                                    wqq = int(dat.readline())
                                    if(bqq == qq):
                                        qq2 = wqq
                                    else:
                                        qq2 = bqq
                                    dat.close()
                                data.close()
                                os.remove(checkchessfile)
                                location2 = 'D:/go-cqhttp_windows_amd64/code/gochess/' + str(qq2) + '.txt'
                                os.remove(location2)
                                os.remove(checkroomfile)
                                location4 = 'D:/go-cqhttp_windows_amd64/data/images/' + room
                                shutil.rmtree(location4)
                                add = float(getimages.getadd(rounds))
                                money = float(getdata.getsd(qq2,5))
                                money = money + add
                                change.changes(qq2,money,5)
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\n您中途退出了对局！您的对手[CQ:at,qq='+str(qq2)+']获得积分：' + str(add)})
                            else:
                                data.close()
                                room = checking.strip()
                                roomfile = 'D:/go-cqhttp_windows_amd64/code/gochess/' + room + '.txt'
                                os.remove(checkchessfile)
                                os.remove(roomfile)
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\n您已关闭房间' + room + '~'})
                    else:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']诶……难不成你在和芙兰下棋嘛！芙兰可没有答应哦~'})            

                elif message.find("fl.game")>=0:
                    if message[0:7] == "fl.game":
                        newgame = message[8:]
                        if len(message) == 7:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']在game后键入空格与数字1可玩1A2B猜数字\n在game后键入空格与数字2可玩寻找炸弹人偶\n输入fl.endgame可与芙兰停止游戏\n其它游戏仍在开发中！啊确实是芙兰自己闲着无聊开发的啦才不是什么大可罢格写的（确信）'})
                        
                        elif message[7] != " ":
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']game后面要加空格哦~'})

                        elif newgame == "1":
                            print("检查游戏进程")
                            if bomb.checkingame(qq):
                                print("游戏2正在进行中\n")
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你还在进行别的游戏哦~玩好这把游戏或者输入fl.endgame后再来玩这个吧！'})
                            elif os.path.exists('D:/go-cqhttp_windows_amd64/code/guessnum/' + str(qq) + '.txt'):
                                print("游戏1正在进行中\n")
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']喂这局游戏还没玩好咧！！！'})
                            else:
                                print("游戏可启动\n")
                                guessnum.numberguess(qq)
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\n开始了哦！我已经想好了四个互不相同的数字，接下来你只需要直接打出这四个数字芙兰就能知道你猜的是什么啦！\n然后芙兰就会告诉你，你所猜的这四个数字与我想的数字中有几个数字是位置和数都符合（用A表示），有几个数只有数字符合（用B表示）！\n一共8次机会哦！那就开始吧~\nPS：输入fl.game 114514可查看本游戏案例'})
                                

                        elif newgame == "2":
                            print("检查游戏进程",bomb.checkingame(qq))
                            if os.path.exists('D:/go-cqhttp_windows_amd64/code/guessnum/' + str(qq) + '.txt'):
                                print("游戏1正在进行中\n")
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你还在进行别的游戏哦~玩好这把游戏或者输入fl.endgame后再来玩这个吧！'})
                            elif bomb.checkingame(qq):
                                print("游戏2正在进行中\n")
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']喂这局游戏还没玩好咧！！！'})
                            else:
                                print("游戏可启动\n")
                                bnum = 'D:/go-cqhttp_windows_amd64/code/bomb/num.txt'
                                with open(file=bnum, mode='r', encoding="utf-8") as data:
                                    bombnumber = int(data.readline())    
                                bomb.joingame(qq)
                                if bombnumber == 0:
                                    g2left = 1
                                    g2right = 100000
                                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\n您已启动新一轮的找炸弹游戏！\n芙兰将自己的一只炸弹人偶藏进了1-100000号红魔馆房间中，接下来你只需要每打出一个在规定范围内的房间号，芙兰就会告诉你一个新的房间范围，如此往复~\n多人游戏中第一个找到炸弹人偶的人可以获得积分奖励哦！那就，开始吧！(*^▽^*)'})
                                else:
                                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\n您已加入本轮找炸弹游戏！\n芙兰将自己的一只炸弹人偶藏进了1-100000号红魔馆房间中，接下来你只需要每打出一个在规定范围内的房间号，芙兰就会告诉你一个新的房间范围，如此往复~\n多人游戏中第一个找到炸弹人偶的人可以获得积分奖励哦！那就，开始吧！(*^▽^*)'})
                            

                        elif newgame == "114514":
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\n例如：答案为1234\n案例输入1：5678 案例回答1：0A0B（无相符数字）\n案例输入2：4325 案例回答2：0A3B（有3个相符数字，但位置对不上）\n案例输入3：1238 案例回答3：3A0B（有3个相符数字且位置全对上了）'})
                                     
                        else :
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']在game后键入空格与数字1可玩1A2B猜数字\n在game后键入空格与数字2可玩寻找炸弹人偶\n输入fl.endgame可与芙兰停止游戏\n其它游戏仍在开发中！啊确实是芙兰自己闲着无聊开发的啦才不是什么大可罢格写的（确信）'})

                elif message == 'fl.endgame':
                    if os.path.exists('D:/go-cqhttp_windows_amd64/code/guessnum/' + str(qq) + '.txt'):
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']呜呜呜好可惜……下次还要再来找我玩哦！(已结束1A2B猜数字）'})
                        guessnum.gameend(qq)
                        
                    elif bomb.checkingame(qq):
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']呜呜呜好可惜……下次还要再来找我玩哦！（已结束寻找炸弹人偶）'})
                        bomb.exitgame(qq)
                        
                    else:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']蛤？我们在……在玩游戏嘛！我怎么不知道orz憋骗我啊喂！！！'})

                elif message.find("fl.piano")>=0:
                    if message[0:8] == "fl.piano":
                        melody = message[9:]
                        if len(message) == 8:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\n钢琴功能输入顺序：\n①（可选）左括号\"(\"降一个八度，右括号\")\"反之，默认下为小字一组，最多可使用三个括号\n②（必选）输入音符0~7，可用合法的升降号#或b，0为空拍无升降号\n③（可选）加号\"＋\"速度加快一倍，减号\"－\"速度放慢一倍，默认下为8分音符，范围为全音符~32分音符'})    
                        elif message[8] != " ":
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']piano后面要加空格哦~'})
                        else:
                            timedo = 0
                            timedo = len(melody)/4
                            timedo = round(timedo,2)
                            if timedo !=0:
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']芙兰大约需要' + str(timedo) + '秒钟的时间弹奏！等等喵……'})
                            get = piano.musicmake(melody)
                            print(get)
                            if get == None or get == -1:
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\n输入的音符串不合法！\n输入顺序：\n①（可选）左括号\"(\"降一个八度，右括号\")\"反之，默认下为小字一组，最多可使用三个括号\n②（必选）输入音符0~7，可用合法的升降号#或b，0为空拍无升降号\n③（可选）加号\"＋\"速度加快一倍，减号\"－\"速度放慢一倍，默认下为8分音符，范围为全音符~32分音符'})
                            else:
                                pianodocu = str(get) + ".mp3"
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:record,file=' + pianodocu + ']'})

                elif message == 'fl.tune':
                    if os.path.exists('D:/go-cqhttp_windows_amd64/code/gochess/' + str(qq) + '.txt'):
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']有没有一种可能，当你下五子棋的时候，五子棋的坐标也能成为一种音高呢！'})
                    elif os.path.exists('D:/go-cqhttp_windows_amd64/code/tune/' + str(qq) + '.txt'):
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']先把我出的这个音猜完呗！或者输入end可以直接结束哦！'})
                    else:
                        tunefile = 'D:/go-cqhttp_windows_amd64/code/tune/' + str(qq) + '.txt'
                        tuneno = random.randint(9,96)
                        height = int(tuneno/12)+1
                        tuneno = tuneno + 1
                        if tuneno%12 == 10:
                            tune = "A"
                        elif tuneno%12 == 11:
                            tune = "Bb"
                        elif tuneno%12 == 0:
                            tune = "B"
                        elif tuneno%12 == 1:
                            tune = "C"
                        elif tuneno%12 == 2:
                            tune = "Db"
                        elif tuneno%12 == 3:
                            tune = "D"
                        elif tuneno%12 == 4:
                            tune = "Eb"
                        elif tuneno%12 == 5:
                            tune = "E"
                        elif tuneno%12 == 6:
                            tune = "F"
                        elif tuneno%12 == 7:
                            tune = "Gb"
                        elif tuneno%12 == 8:
                            tune = "G"
                        elif tuneno%12 == 9:
                            tune = "Ab"
                        tune = tune + str(height)
                        with open(file=tunefile, mode='w', encoding="utf-8") as data:
                            data.write(tune)
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']来猜猜这是什么音！(字母加数字，升号#，降号b，加在字母后面，规定C5为中央音)(输入end可结束猜音)'})
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:record,file='+tune+'.mp3]'})

                elif message == 'fl.flan':
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:image,file=fl_db.png]'})

                elif message.find("fl.picture")==0:
                    if getpicture == 0:
                        trytime = 0
                        urls = 'https://api.lolicon.app/setu/v2?size=thumb'
                        getpicture = 1
                        if len(message) >= 10:
                            tag = message[11:]
                            while len(tag)>0:
                                loca = tag.find("，")
                                if(loca<0):
                                    gettag = tag
                                    if gettag == "18rated":
                                        urls = urls + '&r18=1'
                                    else:
                                        urls = urls + '&tag=' + gettag
                                    break
                                else:
                                    gettag = tag[0:loca]
                                    urls = urls + '&tag=' + gettag
                                    tag = tag[loca+1:]
                        print(urls)
                        picgroup = group
                        picqq = qq
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']芙兰正在寻找图片中，请稍后……\n（picture后什么都不加为随机，加tag需由中文逗号隔开）'})
                    elif message == "fl.picend":
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']然而芙兰并没有在找图片XD'})
                    else:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']芙兰还在寻找上一张图片，先等等啦……\n（picture后什么都不加为随机，加tag需由中文逗号隔开）'})

                elif message.find("fl.pic")>=0:
                     if message[0:6] == "fl.pic":
                        
                        if len(message) <= 7:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\npic加空格加数字1~5可选择图片翻转类型\n1为水平翻转左边拼在右边\n2为水平翻转右边拼在左边\n3为垂直翻转上边拼在下边\n4为垂直翻转下边拼在上边\n5为翻转图片颜色\n之后还要跟着一张图片哦！'})
                            continue
                        choose = message[7]
                        if choose.isdigit():
                            cse = int(choose)
                        if message[6] != " ":
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']pic后面要加空格哦~'})
                        elif not choose.isdigit() or cse > 5 or cse == 0:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\npic加空格加数字1~5可选择图片翻转类型\n1为水平翻转左边拼在右边\n2为水平翻转右边拼在左边\n3为垂直翻转上边拼在下边\n4为垂直翻转下边拼在上边\n5为翻转图片颜色\n之后还要跟着一张图片哦！'})
                        
                        else:   
                            locate = message.find("url")
                            if(locate > 0):
                                picurl = message[locate+4:]
                                print(picurl)
                                numbe = picrev.picrev(picurl,cse)
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:image,file=picrev_' + str(numbe) + '.png]'})
                            else:
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']芙兰没收到您发过来的图片耶……要不要再试一次？！'})
                                
                elif message.find("fl.repeat")==0:
                    if len(message) == 9:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']repeat后面加空格加句子可以让芙兰复读这句话哦~'})
                    elif message[9] != " " or len(message) == 10:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']repeat后面要加空格哦~'})
                    else:
                        newmsg = message[10:]
                        message = message.lower()
                        if message.find("星光")>=0 or message.find("darkbug")>=0 or message.find("db")>=0 or message.find("大可罢格")>=0 or message.find("miyaktik")>=0 or message.find("starlight")>=0 or message.find("finylestar")>=0:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':"星光是我老公，但他实在是tljl。"})
                        else:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':newmsg})

                elif message.find("fl.store")==0:
                    if len(message) == 8:
                        output = '[CQ:at,qq='+str(qq)+']\n欢迎来到商店！输入fl.store＋空格＋数字即可购买东西XD\n'
                        output = output + "——————————————\n"
                        output = output + '1 补签卡(断签时可补签，两次断签以上仅补签最近的一次断签区间) - 800积分\n'
                        output = output + '2 rp重置卡(可重新测jrrp，rp取今日最高的一次，购买需好感度>=10) - 500积分\n'
                        output = output + '3 获得随机零食/饮料 - 100积分'
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
                    elif message[8] != " " or len(message) == 9:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']store后面要加一个空格才能购买东西哦~'})
                    else:
                        newstore = message[9:]
                        money = float(getdata.getsd(qq,5))
                        if newstore == '1':
                            if(money >= 800):
                                money = money - 800
                                tnum = getbag.getbags(qq,1) + 1
                                changebag.changebags(qq,tnum,1)
                                change.changes(qq,money,5)
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您已购买一张补签卡，包内现有' + str(tnum) + '张。输入fl.use 1即可使用哦~'})
                            else:
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您的积分不足，还不能买哦！'})
                        elif newstore == '2':
                            if(favor >= 10):
                                if(money >= 500):
                                    money = money - 500
                                    tnum = getbag.getbags(qq,2) + 1
                                    changebag.changebags(qq,tnum,2)
                                    change.changes(qq,money,5)
                                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您已购买一张rp重置卡，包内现有' + str(tnum) + '张。输入fl.use 2可直接使用哦~'})
                                else:
                                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您的积分不足，还不能买哦！'})
                            else:
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您的好感度不够，芙兰还不能卖给你……qwq'})
                        elif newstore == '3':
                            if(money >= 100):
                                money = money - 100
                                food = random.randint(3,7)
                                tnum = getbag.getbags(qq,food) + 1
                                changebag.changebags(qq,tnum,food)
                                change.changes(qq,money,5)
                                output = '[CQ:at,qq='+str(qq)+']'
                                if food == 3:
                                    output = output + "您买到了一份⑨转大肠，包内共有" + str(tnum) + "份。嘶……这真的能吃嘛……(可输入fl.use 3使用)"
                                elif food == 4:
                                    output = output + "您买到了一份草莓蛋糕，包内共有" + str(tnum) + "份。甜甜的草莓加上甜甜的蛋糕，甜蜜程度平方啦——(可输入fl.use 4使用)"
                                elif food == 5:
                                    output = output + "您买到了一个红苹果，包内共有" + str(tnum) + "个。快给芙兰芙兰想吃！！！(可输入fl.use 5使用)"
                                elif food == 6:
                                    output = output + "您买到了一杯红茶玛奇朵，包内共有" + str(tnum) + "杯。奶油的味道好香！(可输入fl.use 6使用)"
                                elif food == 7:
                                    output = output + "您买到了一块冰糖雪糕，包内共有" + str(tnum) + "块。你和冰糖雪梨是什么关系.jpg(可输入fl.use 7使用)"
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
                            else:
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您的积分不足，还不能买哦！'})
                        
                elif message == "fl.bag":
                    output = '[CQ:at,qq='+str(qq)+']\n当前您的背包里有：'
                    empty = 1
                    for i in range (1,9):
                        n = getbag.getbags(qq,i)
                        if n != 0:
                            if i == 1:
                                output = output + "\n1 补签卡×" + str(n)
                            elif i == 2:
                                output = output + "\n2 rp重置卡×" + str(n)
                            elif i == 3:
                                output = output + "\n3 ⑨转大肠×" + str(n)
                            elif i == 4:
                                output = output + "\n4 草莓蛋糕×" + str(n)
                            elif i == 5:
                                output = output + "\n5 红苹果×" + str(n)
                            elif i == 6:
                                output = output + "\n6 红茶玛奇朵×" + str(n)
                            elif i == 7:
                                output = output + "\n7 冰糖雪糕×" + str(n)
                            elif i == 8:
                                output = output + "\n8 黑松露炒饭×" + str(n)
                            empty = 0
                    if empty == 1:
                        output = output + "一片死寂的空气……"
                    else:
                        output = output + "\n可输入fl.use [物品前的数字]使用哦！"
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})

                elif message.find("fl.use")==0:
                    if len(message) == 6:
                        output = '[CQ:at,qq='+str(qq)+']\n在use之后加空格加数字(物品序号)即可使用该物品！可以发送fl.bag查询物品序号哦~'
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
                    elif message[6] != " " or len(message) == 7:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']use后面要加一个空格才能使用东西哦~'})
                    else:
                        newuse = message[7:]
                        if newuse == "1":
                            tnum = getbag.getbags(qq,1)
                            if tnum <= 0:
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})
                            else:
                                qddate = int(getdata.getsd(qq,6))
                                location = 'D:/go-cqhttp_windows_amd64/code/usersdata/' + str(qq) + '_qdover.txt'
                                if (qddate - date != 0):
                                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']先去签个到再来使用这个东西吧！'})
                                elif not os.path.exists(location):
                                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你貌似不需要补签的样子！暂时用不了哦~'})
                                else:
                                    with open(file=location, mode='r', encoding="utf-8") as data:
                                        lastqddate = int(data.readline())
                                        lastqdren = int(data.readline())
                                    qdren = int(getdata.getsd(qq,7)) + 1
                                    datemin = qddate - lastqddate
                                    reqdtimes = datemin - qdren
                                    longestren = lastqdren+datemin
                                    if reqdtimes == 0:
                                        change.changes(qq,longestren,7)
                                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']补签成功，您已连续签到' + str(longestren) + '天，已无需再次补签啦~'})
                                        os.remove(location)
                                    else:
                                        change.changes(qq,qdren,7)
                                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']补签成功，您已连续签到' + str(qdren) + '天，再使用' + str(reqdtimes) + '张补签卡就能连续签到' + str(longestren) + '天了哦！'})
                                    tnum = tnum - 1
                                changebag.changebags(qq,tnum,1)

                                    
                        
                        elif newuse == "2":
                            tnum = getbag.getbags(qq,2)
                            if tnum <= 0:
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})
                            else:
                                tnum = tnum - 1
                                orirp = int(jrrp.getjrrp(qq,1))
                                newrp = int(jrrp.getjrrp(qq,2))
                                if orirp > newrp:
                                    output = '[CQ:at,qq='+str(qq)+']你原本的人品值为' + str(orirp) + '，使用rp重置卡后得到的新rp值为' + str(newrp) +'。没有原来的高，将保留原rp。可惜……'
                                elif orirp < newrp:
                                    output = '[CQ:at,qq='+str(qq)+']你原本的人品值为' + str(orirp) + '，使用rp重置卡后得到的新rp值为' + str(newrp) +'。恭喜刷新今日最高！'
                                else:
                                    output = '[CQ:at,qq='+str(qq)+']你原本的人品值为' + str(orirp) + '，使用rp重置卡后得到的新rp值为' + str(newrp) +'。这都能一模一样………这得比达到理论最高人品还难了吧orz'
                                changebag.changebags(qq,tnum,2)
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
                        elif newuse == "3":
                            tnum = getbag.getbags(qq,3)
                            if tnum <= 0:
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})
                            else:
                                tnum = tnum - 1
                                nowplace = place.checkplace(qq)
                                output = '[CQ:at,qq='+str(qq)+']'
                                
                                if(nowplace == "0"):
                                    output = output + '你吃下了⑨转大肠……呃嗯……感觉自己的大肠正在疯狂⑨转中……'
                                elif(nowplace == "1"):
                                    output = output + '你让⑨吃下了⑨转大肠，⑨的脸部凝聚成了一块……随后逃跑了……然后又回来了。'
                                    results = random.uniform(0,100)
                                    if results <= 50:
                                        money = float(getdata.getsd(qq,5))
                                        money = money + 199.99
                                        change.changes(qq,money,5)
                                        output = output + '\n俗话说得好，baka的记忆只有9秒。她看到你给她的东西里名字带⑨，竟然决定奖励你199.99积分！？！'
                                elif(nowplace == "2"):
                                    if(favor<15):
                                        place.changeplace(str(qq),"2-0")
                                        output = output + '你将⑨转大肠送到了美铃的面前。美铃闻了一下之后一边骂着国粹一边到处跑开然后昏倒了……！？是个潜入红魔馆的好机会！（可以输入fl.move 2-X进入红魔馆内部了）'
                                    else:
                                        output = output + '你将⑨转大肠送到了美铃的面前，美铃闻了一下之后立刻扔掉了。看来谁都不喜欢这道菜捏……'
                                elif(nowplace == "2-0"):
                                    money = float(getdata.getsd(qq,5))
                                    money = money + 250
                                    change.changes(qq,money,5)
                                    output = output + '看着昏昏欲睡(其实已经睡着了)的美铃，你还是选择了自己吃下了⑨转大肠。然后你把她熏醒了……？？？她似乎很感谢你在大小姐发现她之前叫醒她，然后给了你150积分……'
                                elif(nowplace == "2-1"):
                                    money = float(getdata.getsd(qq,5))
                                    money = money - 100
                                    change.changes(qq,money,5)
                                    output = output + '喂！！！你这是拿了个什么东西出来啊喵！！！快点给我扔掉啊啊啊啊啊（掏出莱瓦汀）（乱挥）（……你失去了100积分）'
                                elif(nowplace == "2-2"):
                                    output = output + '你拿出了⑨转大肠。姆Q貌似对这道菜还挺感兴趣……！？她决定拿另一道菜和你交换。（已获得：'
                                    food = random.randint(6,8)
                                    tnum2 = getbag.getbags(qq,food) + 1
                                    changebag.changebags(qq,tnum2,food)
                                    if food == 6:
                                        output = output + "6 红茶玛奇朵）"
                                    elif food == 7:
                                        output = output + "7 冰糖雪糕）"
                                    elif food == 8:
                                        output = output + "8 黑松露炒饭）"

                                elif(nowplace == "2-3"):
                                    place.changeplace(str(qq),"2")
                                    output = output + '你拿出了⑨转大肠。在你刚拿出的那一刻，女仆长立刻把你送到了红魔馆门口。似乎打扰到她打扫卫生了……'
                                    tnum = tnum + 1

                                elif(nowplace == "2-4"):
                                    place.changeplace(str(qq),"2")
                                    output = output + '你拿出了⑨转大肠。在你刚拿出的那一刻，蕾米突然大吼一声“咲夜”。你被赶出去了……'
                                    tnum = tnum + 1
                                
                                changebag.changebags(qq,tnum,3)
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
                        elif newuse == "4":
                            tnum = getbag.getbags(qq,4)
                            if tnum <= 0:
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})
                            else:
                                tnum = tnum - 1
                                nowplace = place.checkplace(qq)
                                output = '[CQ:at,qq='+str(qq)+']'
                                if(nowplace == "0"):
                                    output = output + '你吃下了草莓蛋糕。甜甜的，确实好吃！'
                                elif(nowplace == "1"):
                                    results = random.uniform(0,100)
                                    if results <= 50:
                                        money = float(getdata.getsd(qq,5))
                                        money = money + 199.99
                                        change.changes(qq,money,5)
                                        output = output + '你让⑨吃下了草莓蛋糕，她很开心，随后丢给了你199.99积分！好耶！'
                                    else:
                                        output = output + '你让⑨吃下了草莓蛋糕，她很开心，不断吼着“我还要我还要”。看来是没完没了了……'
                                elif(nowplace == "2"):
                                    if(favor<15):
                                        output = output + '你想给美铃吃草莓蛋糕，但显然这种东西还是贿赂不了她啦……'
                                    else:
                                        output = output + '你想给美铃吃草莓蛋糕，但她拒绝了你的好意。'
                                    tnum = tnum + 1
                                elif(nowplace == "2-0"):
                                    output = output + '看着昏昏欲睡(其实已经睡着了)的美铃，你还是选择了自己吃下了草莓蛋糕。填饱肚子再进去捏（吐舌头）'
                                elif(nowplace == "2-1"):
                                    money = float(getdata.getsd(qq,5))
                                    money = money + 150
                                    change.changes(qq,money,5)
                                    output = output + '哦哦哦！草莓蛋糕！！！芙兰最最喜欢吃啦XD（大吃一通）（……你偷偷拿走了150积分）'
                                elif(nowplace == "2-2"):
                                    output = output + '你拿出了草莓蛋糕。姆Q似乎不感兴趣……！但她还是收下了你的心意。'
                                elif(nowplace == "2-3"):
                                    results = random.uniform(0,100)
                                    if results <= 75:
                                        money = float(getdata.getsd(qq,5))
                                        money = money + 123
                                        change.changes(qq,money,5)
                                        output = output + '你拿出了草莓蛋糕。咲夜说她这里正好缺蛋糕……随后拿走了你的蛋糕并给了你123积分。跑腿费才这么点真小气……'
                                    else:
                                        place.changeplace(str(qq),"2")
                                        output = output + '你拿出了草莓蛋糕。在你刚拿出的那一刻，女仆长立刻把你送到了红魔馆门口并没收了你的蛋糕。似乎打扰到她打扫卫生了……怎么不付钱的啊！！！'
                                elif(nowplace == "2-4"):
                                    results = random.uniform(0,100)
                                    if results <= 50:
                                        money = float(getdata.getsd(qq,5))
                                        money = money + 222
                                        change.changes(qq,money,5)
                                        output = output + '你拿出了草莓蛋糕。蕾米突然跑了下来一把塞进了嘴里。嘶……她可真急……你得到了222积分。'
                                    else:
                                        output = output + '你拿出了草莓蛋糕。蕾米突然跑了下来一把塞进了嘴里，但她吃得太快呛着了……真是威严满满啊（便乘）'
                                
                                changebag.changebags(qq,tnum,4)
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
                        elif newuse == "5":
                            tnum = getbag.getbags(qq,5)
                            if tnum <= 0:
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})
                            else:
                                tnum = tnum - 1
                                nowplace = place.checkplace(qq)
                                output = '[CQ:at,qq='+str(qq)+']'
                                if(nowplace == "0"):
                                    output = output + '你吃下了红苹果。一天一苹果，永琳远离我（大雾）'
                                    results = random.uniform(0,100)
                                    if results <= 75:
                                        money = float(getdata.getsd(qq,5))
                                        money = money + 150
                                        change.changes(qq,money,5)
                                        output = output + '\n吃完苹果后，你突然感觉到身上充满了破坏一切的力量，转瞬即逝……随后获得了150积分！？'
                                elif(nowplace == "1"):
                                    output = output + '你让⑨吃下了苹果，她似乎不是很喜欢吃水果，真是个挑食的孩子XD'
                                elif(nowplace == "2"):
                                    if(favor<15):
                                        output = output + '你想给美铃吃红苹果，但显然这种东西还是贿赂不了她啦……'
                                    else:
                                        output = output + '你想给美铃吃草莓蛋糕，但她拒绝了你的好意，说芙兰最喜欢吃这个了，可以去带给她吃！嗯嗯嗯她说的对（飞来飞去）'
                                    tnum = tnum + 1
                                elif(nowplace == "2-0"):
                                    output = output + '看着昏昏欲睡(其实已经睡着了)的美铃，你还是选择了自己吃下了红苹果。水果果然还是填饱不了肚子啦！'
                                elif(nowplace == "2-1"):
                                    output = output + '芙兰最喜欢吃苹果啦！阿卡伊阿麻伊！（大口大口咀嚼）'
                                    results = random.uniform(0,100)
                                    if results <= 50 - favor * 2:
                                        money = int(getdata.getsd(qq,2))
                                        money = money + 1
                                        change.changes(qq,money,2)
                                        output = output + '\n芙兰吃得好开心！谢谢你！！！（试图扑向你的怀中）（你躲开了…………并增加了1点好感值）'
                                    elif favor >= 25 and results <= 10:
                                        money = float(getdata.getsd(qq,5))
                                        money = money + 500
                                        change.changes(qq,money,5)
                                        output = output + '\n芙兰吃得好开心！谢谢你！！！（你得到了500积分）'
                                    
                                elif(nowplace == "2-2"):
                                    output = output + '你拿出了红苹果，姆Q的建议是拿给芙兰吃，因此你收了回去。'
                                    tnum = tnum + 1
                                elif(nowplace == "2-3"):
                                    money = float(getdata.getsd(qq,5))
                                    money = money + 111
                                    change.changes(qq,money,5)
                                    output = output + '你拿出了红苹果，咲夜似乎想收下这个苹果。她感谢你并给了你111积分。'
                                elif(nowplace == "2-4"):
                                    results = random.uniform(0,100)
                                    if results <= 40 - favor * 2:
                                        money = int(getdata.getsd(qq,2))
                                        money = money + 1
                                        change.changes(qq,money,2)
                                        output = output + '你拿出了红苹果。蕾米好像也很喜欢吃！不愧是姐妹俩……但她拒绝和你培养好感度，所以她通过改变命运的力量将你和芙兰的好感度提升了1点。什么鬼！'
                                    elif favor >= 20 and results <= 25:
                                        money = float(getdata.getsd(qq,5))
                                        money = money + 150
                                        change.changes(qq,money,5)
                                        output = output + '你拿出了红苹果。蕾米收下了，似乎想拿给妹妹吃……向你支付了150P。小赚！'
                                    else:
                                        money = float(getdata.getsd(qq,5))
                                        money = money + 50
                                        change.changes(qq,money,5)
                                        output = output + '你拿出了红苹果。蕾米收下了，似乎想拿给妹妹吃……向你支付了50P。红魔馆里头物价这么低的吗（恼）'

                                changebag.changebags(qq,tnum,5)
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
                        elif newuse == "6":
                            tnum = getbag.getbags(qq,6)
                            if tnum <= 0:
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})
                            else:
                                tnum = tnum - 1
                                nowplace = place.checkplace(qq)
                                output = '[CQ:at,qq='+str(qq)+']'
                                if(nowplace == "0"):
                                    output = output + '你喝下了红茶玛奇朵。一杯喝下去整天都有好心情~'
                                elif(nowplace == "1"):
                                    output = output + '你让⑨喝下了红茶玛奇朵。烫死啦！！！她噗的一声就吐了出来……真浪费喵'
                                elif(nowplace == "2"):
                                    if(favor<15):
                                        output = output + '你想让美铃喝红茶玛奇朵，她喝了下去，精神状态爆发！！！等等你这样不就更难潜入了……'
                                    else:
                                        place.changeplace(str(qq),"2-0")
                                        output = output + '你让美铃喝下了红茶玛奇朵。什么！这竟然是昏睡红茶！？她昏倒了……希望别被大小姐发现'
                                elif(nowplace == "2-0"):
                                    output = output + '看着昏昏欲睡(其实已经睡着了)的美铃，你还是选择了自己喝下了红茶玛奇朵。这种东西要让她喝才怪咧！！！'
                                elif(nowplace == "2-1"):
                                    money = float(getdata.getsd(qq,5))
                                    money = money + 50
                                    change.changes(qq,money,5)
                                    output = output + '哦哦哦！是红茶！谢谢你给我带了红茶！！！（飞奔上去喝）（已获得50积分）'
                                    results = random.uniform(0,100)
                                    if (results <= 30 - favor * 2) or (favor >= 15 and results <= 2):
                                        money = int(getdata.getsd(qq,2))
                                        money = money + 1
                                        change.changes(qq,money,2)
                                        output = output + '\n芙兰喝得好开心！谢谢你！！！（试图扑向你的怀中）（你被推倒了……？！星光震怒……并增加了1点好感值）'
                                elif(nowplace == "2-2"):
                                    money = float(getdata.getsd(qq,5))
                                    money = money + 100
                                    change.changes(qq,money,5)
                                    output = output + '你拿出了红茶玛奇朵，姆q似乎很喜欢喝，并向你支付了100积分。等等这不带跑路费的嘛！！！'
                                elif(nowplace == "2-3"):
                                    money = float(getdata.getsd(qq,5))
                                    output = output + '你拿出了红茶玛奇朵，咲夜喝了一口，神清气爽！'
                                    results = random.uniform(0,100)
                                    if results <= 50:
                                        money = money + 50
                                        output = output + '但好像影响到了她打扫卫生……她只给了你50积分。'
                                    else:
                                        money = money + 150
                                        output = output + '她似乎非常感谢你，给了你150积分。'
                                    change.changes(qq,money,5)

                                elif(nowplace == "2-4"):
                                    results = random.uniform(0,100)
                                    output = output + '你拿出了红茶玛奇朵，但蕾米好像正在喝红酒！你收回去了。'
                                    tnum = tnum + 1
                                
                                changebag.changebags(qq,tnum,6)
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
                        elif newuse == "7":
                            tnum = getbag.getbags(qq,7)
                            if tnum <= 0:
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})
                            else:
                                tnum = tnum - 1
                                nowplace = place.checkplace(qq)
                                output = '[CQ:at,qq='+str(qq)+']'
                                if(nowplace == "0"):
                                    output = output + '你吃下了冰糖雪糕。冰冰的甜甜的，有一种吃⑨的感觉捏（雾）'
                                elif(nowplace == "1"):
                                    money = float(getdata.getsd(qq,5))
                                    money = money + 149.99
                                    change.changes(qq,money,5)
                                    output = output + '你让⑨吃下了冰糖雪糕，⑨高兴地跳了起来，大吼着想给你一百万亿积分。于是你借给了她一百万亿，然后她给了你一百万亿＋149.99积分。嗯……多此一举'
                                elif(nowplace == "2"):
                                    if(favor<15):
                                        output = output + '你想让美铃吃冰糖雪糕，但她好像并不是很喜欢⑨的样子……还回来了。'
                                    else:
                                        output = output + '你想让美铃吃冰糖雪糕，她拒绝了你的好意……还回来了。'
                                    tnum = tnum + 1
                                elif(nowplace == "2-0"):
                                    results = random.uniform(0,100)
                                    if results <= 40:
                                        money = float(getdata.getsd(qq,5))
                                        money = money + 250
                                        change.changes(qq,money,5)
                                        output = output + '看着昏昏欲睡(其实已经睡着了)的美铃，你吃下了冰糖雪糕。你边吃边看着美铃，什么！她裙子旁边竟然夹着250积分！？嗯……反正她睡着了就直接拿走罢（心虚）'
                                    else:
                                        output = output + '看着昏昏欲睡(其实已经睡着了)的美铃，你吃下了冰糖雪糕。你边吃边看着美铃。嗯……真凉快！'
                                elif(nowplace == "2-1"):
                                    output = output + '唔……芙兰并不是很喜欢吃雪糕呢……但谢谢你的好意啦！XD'
                                elif(nowplace == "2-2"):
                                    output = output + '你拿出了冰糖雪糕，姆q一把夺过，并指责你不能在图书馆里吃零食。呃……怎么别的食物就可以在图书馆里吃呢……'
                                elif(nowplace == "2-3"):
                                    output = output + '你拿出了冰糖雪糕，咲夜看了一眼，建议你在外面自己吃掉。看来并没有收下……'
                                    tnum = tnum + 1
                                elif(nowplace == "2-4"):
                                    results = random.uniform(0,100)
                                    if results <= 50:
                                        money = float(getdata.getsd(qq,5))
                                        money = money + 229.99
                                        change.changes(qq,money,5)
                                        output = output + '你拿出了冰糖雪糕。蕾米似乎心生一计，拿229.99积分换下了雪糕。(吸血)鬼知道她在想什么！'
                                    else:
                                        output = output + '你拿出了冰糖雪糕。蕾米不喜欢吃，但她还是吃下去了……'

                                changebag.changebags(qq,tnum,7)
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
                        elif newuse == "8":
                            tnum = getbag.getbags(qq,8)
                            if tnum <= 0:
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})
                            else:
                                tnum = tnum - 1
                                nowplace = place.checkplace(qq)
                                output = '[CQ:at,qq='+str(qq)+']'
                                if(nowplace == "0"):
                                    money = float(getdata.getsd(qq,5))
                                    money = money + 200
                                    change.changes(qq,money,5)
                                    output = output + '你吃下了黑松露炒饭。太好吃辣！！！你直奔出家门在人间之里大吼大叫跑了一圈，别人以为你是抢积分的妖怪，直接给你扔了200积分……喵？'
                                elif(nowplace == "1"):
                                    money = float(getdata.getsd(qq,5))
                                    money = money + 199.99
                                    change.changes(qq,money,5)
                                    output = output + '你让⑨吃下了黑松露炒饭，⑨不喜欢吃热的东西。但是！她竟然朝你丢了笨蛋积分！（已获得199.99积分）'
                                elif(nowplace == "2"):
                                    if(favor<15):
                                        output = output + '你想让美铃吃黑松露炒饭，她好像吃腻了的样子……还回来了。'
                                    else:
                                        output = output + '你想让美铃吃黑松露炒饭，她拒绝了你的好意……还回来了。'
                                    tnum = tnum + 1
                                elif(nowplace == "2-0"):
                                    results = random.uniform(0,100)
                                    if results <= 50:
                                        money = float(getdata.getsd(qq,5))
                                        money = money + 300
                                        change.changes(qq,money,5)
                                        output = output + '看着昏昏欲睡(其实已经睡着了)的美铃，你还是选择了自己吃下了黑松露炒饭。香气扑鼻啊！立刻引来了一帮妖怪想吃你的东西，随后丢下钱走了。还好没吵醒美铃……（已获得积分：300）'
                                    else:
                                        output = output + '看着昏昏欲睡(其实已经睡着了)的美铃，你还是选择了自己吃下了黑松露炒饭。香气扑鼻啊！'
                                elif(nowplace == "2-1"):
                                    output = output + '是黑松露炒饭诶！虽然并没有特别喜欢松露，但是加上了炒饭真的好香！（大口大口咀嚼）'
                                    results = random.uniform(0,100)
                                    if (results <= 60 - favor * 2) or (favor>=30 and results <= 1):
                                        money = int(getdata.getsd(qq,2))
                                        money = money + 2
                                        change.changes(qq,money,2)
                                        output = output + '\n芙兰吃得好开心！谢谢你！！！（试图扑向你的怀中）（你接住了，增加了2点好感值）'
                                    elif results <= 60:
                                        money = float(getdata.getsd(qq,5))
                                        money = money + 200
                                        change.changes(qq,money,5)
                                        output = output + '\n芙兰吃得好开心！谢谢你！作为回礼，芙兰奖励你一些积分吧！（已获得200积分）'
                                elif(nowplace == "2-2"):
                                    output = output + '你拿出了黑松露炒饭，姆q表示自己这里有一大堆实验品，你决定收回……啥？实验品？？？'
                                    tnum = tnum + 1
                                elif(nowplace == "2-3"):
                                    money = float(getdata.getsd(qq,5))
                                    money = money + 220
                                    change.changes(qq,money,5)
                                    output = output + '你拿出了黑松露炒饭，咲夜好像很饿，她吃了下去，然后给了你220P……等等她为什么自己不做一份呢'
                                elif(nowplace == "2-4"):
                                    output = output + '你拿出了黑松露炒饭，蕾米说她家女仆天天给她做这个，建议还是拿给她妹妹吃。'
                                    tnum = tnum + 1

                                changebag.changebags(qq,tnum,8)
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
                        else:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你的背包里还没有这个东西哦，要不再去找找看吧！'})

                elif message == "fl.place":
                    output = '[CQ:at,qq='+str(qq)+']您当前的所在地是：'
                    nowplace = place.checkplace(qq)
                    if(nowplace == "0"):
                        output = output + '\n0 人间之里。真是安详的一天啊！'
                    elif(nowplace == "1"):
                        output = output + '\n1 雾之湖。湖上也有许多飞来飞去的妖精呢。'
                    elif(nowplace == "2" or nowplace == "2-0"):
                        output = output + '\n2 红魔馆(入口)。不知道门番是否在打鼾呢！'
                    elif(nowplace == "2-1"):
                        output = output + '\n2-1 红魔馆地下室。芙兰就在你身边看着你哦~诶嘿！'
                    elif(nowplace == "2-2"):
                        output = output + '\n2-2 红魔馆图书馆。姆Q今天放下书了吗（不可能，绝对不可能）'
                    elif(nowplace == "2-3"):
                        output = output + '\n2-3 红魔馆大堂中央。今天的咲夜也在很卖力地打扫卫生呢~'
                    elif(nowplace == "2-4"):
                        output = output + '\n2-4 红魔馆主殿堂。威严满满的姐姐大人正在威严满满地品着红酒！'
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})

                elif message.find("fl.move")==0:
                    if len(message) == 7:
                        output = '[CQ:at,qq='+str(qq)+']\n在move之后加空格加数字(地点序号)即可移动到该区域！'
                        output = output + '\n0 人间之里'
                        output = output + '\n1 雾之湖'
                        output = output + '\n2 红魔馆(入口)'
                        output = output + '\n(需先到达2)2-1 地下室'
                        output = output + '\n(需先到达2)2-2 图书馆'
                        output = output + '\n(需先到达2)2-3 大堂中央'
                        output = output + '\n(需先到达2)2-4 主殿堂'
                        output = output + '\n输入fl.place可以查询自己现在所处的位置哦！'
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg': output})
                    elif message[7] != " " or len(message) == 8:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']move后面要加一个空格才能移动哦~'})
                    else:
                        newmove = message[8:]
                        nowplace = place.checkplace(qq)
                        results = random.uniform(0,100)
                        if results <= 5:
                            money = float(getdata.getsd(qq,5))
                            money = money - 20
                            change.changes(qq,money,5)
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']当你刚准备出发时，一只粉色的兔子突然出现在你的面前绊了你一脚。疼！你爬起来之后发现自己失去了20积分！？！可恶的兔子。。。'})
                            continue
                        if newmove == nowplace or (newmove == "2" and nowplace == "2-0"):
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你原地踏步，然后以光速绕了地球一圈，回到了原来的位置。'})
                        elif newmove == "0":
                            place.changeplace(qq,newmove)
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你回到了人间之里的家中。啊——又是个安详的一天呢（伸懒腰）'})
                        
                        elif newmove == "1":
                            firstmove = place.changeplace(str(qq),str(newmove))
                            if(firstmove == 1):
                                output = '[CQ:at,qq='+str(qq)+']你来到了雾之湖！湖面上有一只蓝色的baka，你决定去找她探讨智慧人生……\n………………\n………………\n………………\n………………\n………………\n………………\n………………'
                                results = random.uniform(0,100)
                                if(results<=29.99):
                                    money = float(getdata.getsd(qq,5))
                                    money = money + 29.99
                                    change.changes(qq,money,5)
                                    output = output + '\n探讨结束！baka酱觉得你很有胆识，于是掏出了身上的29.99积分决定送给你。（已获得29.99积分）'
                                else:
                                    output = output + '\n探讨结束！baka酱想送你积分，她决定先向你借99积分再送给你……真是个baka呢（无慈悲）'
                            else:
                                output = '[CQ:at,qq='+str(qq)+']你又来到了雾之湖！baka已经不见了踪影，你决定独自思考人生……\n………………\n………………\n………………\n………………\n………………\n………………\n………………'
                                output = output + '\n你感觉你的人生上升到了一个新的境界。（所以有用吗）'
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

                        elif newmove == "2":
                            firstmove = place.changeplace(str(qq),str(newmove))
                            if(firstmove == 1):
                                output = '[CQ:at,qq='+str(qq)+']你来到了红魔馆大门口！似乎有位红发的华人小姑娘站在门口，你决定上去看看……'
                                results = random.uniform(0,100)
                                if(favor>=15):
                                    output = output + '\n美铃似乎一眼就认出了你，她很欢迎你进入红魔馆去找二妹玩。呀吼！（可以输入fl.move 2-X进入红魔馆内部了）'
                                elif(results<=30):
                                    place.changeplace(str(qq),"2-0")
                                    output = output + '\n这位守门员竟然站着都能睡着！？！你决定趁她不注意偷偷潜入……（可以输入fl.move 2-X进入红魔馆内部了）'
                                else:
                                    output = output + '\n她一把就拦住了你，捏着拳头摆出招式，叫嚣着“拒绝外人进入”。真拿她没办法……'
                            else:
                                output = '[CQ:at,qq='+str(qq)+']你又来到了红魔馆大门口！'
                                if(favor>=15):
                                    output = output + '\n美铃看都不看一眼就认出了你，她很欢迎你进入红魔馆去找二妹玩。呀吼！（可以输入2-X进入红魔馆内部了）'
                                else:
                                    output = output + '\n美铃还在那儿威风凛凛地站着，看到你立马又捏着拳头摆出招式，叫嚣着“拒绝外人进入”。真拿她没办法……'
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

                        elif newmove.find("2-") == 0:
                            if nowplace.find("2") != 0:
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']要先前往红魔馆大门口才能进入红魔馆内部啦！'})
                            elif favor<15 and nowplace == "2":
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你想偷偷摸摸进入红魔馆，被美铃一拳拦住了。可恶……'})
                            else:
                                newmove2 = newmove[2:]
                                if newmove2 == "1":
                                    firstmove = place.changeplace(str(qq),str(newmove))
                                    if(firstmove == 1):
                                        output = '[CQ:at,qq='+str(qq)+']欢迎你来到地下室！！！快来陪芙兰一起玩吧……（笑）（掏出莱瓦汀）（破坏小熊人偶）（变出三个分身）（互相乱砍）（你成功躲开了四位芙兰的弹幕）（你站在角落静静观望，似乎红魔馆又要爆炸了……）'
                                        results = random.uniform(0,100)
                                        if(results<=60-favor*2):
                                            money = int(getdata.getsd(qq,2))
                                            money = money + 1
                                            change.changes(qq,money,2)
                                            output = output + '\n（经过了四个小时的激烈折腾，你和芙兰的好感度竟然上升了1点……呃……你该不会是M吧（后缩））'
                                        elif(results<=60):
                                            money = float(getdata.getsd(qq,5))
                                            money = money + 100
                                            change.changes(qq,money,5)
                                            output = output + '\n（你看着芙兰在地下室里飞来飞去，突然发现了角落里藏着100积分。偷偷拿走，嗯！）（已获得100积分）'
                                        else:
                                            output = output + '\n（之后你又陪芙兰在地下室玩(???)了半个小时，她正准备扯下你的胳膊，你慌忙挣脱躲到了角落里。太可怕了……）'
                                    else:
                                        output = '[CQ:at,qq='+str(qq)+']呜哇！欢迎再次回来！！！芙兰等你好久啦~继续一起玩耍吧XDXDXD'
                                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

                                elif newmove2 == "2":
                                    firstmove = place.changeplace(str(qq),str(newmove))
                                    if(firstmove == 1):
                                        output = '[CQ:at,qq='+str(qq)+']你来到了图书馆。姆Q正在专心读书，没注意到你……'
                                        results = random.uniform(0,100)
                                    else:
                                        output = '[CQ:at,qq='+str(qq)+']你又一次来到了图书馆。姆Q还是在专心读书，可恶是书呆子！'
                                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

                                elif newmove2 == "3":
                                    firstmove = place.changeplace(str(qq),str(newmove))
                                    if(firstmove == 1):
                                        output = '[CQ:at,qq='+str(qq)+']你来到了大堂中央，看到红魔馆的女仆长正在努力打扫，似乎没时间理你……'
                                        results = random.uniform(0,100)
                                    else:
                                        output = '[CQ:at,qq='+str(qq)+']你又一次来到了大堂中央，咲夜正坐在椅子上休息，看起来很疲惫的样子。'
                                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

                                elif newmove2 == "4":
                                    firstmove = place.changeplace(str(qq),str(newmove))
                                    if(firstmove == 1):
                                        output = '[CQ:at,qq='+str(qq)+']你来到了红魔馆主殿堂，遇到了坐在殿堂中央的蕾米。'
                                        results = random.uniform(0,100)
                                        if(results <= 25 and favor < 20):
                                            money = int(getdata.getsd(qq,2))
                                            money = money + 1
                                            change.changes(qq,money,2)
                                            output = output + "蕾米今天似乎心情不错……她改变了你与芙兰之间的命运。（你与芙兰的好感度上升了1点）"
                                        elif(results <= 25 and favor >= 20):
                                            money = float(getdata.getsd(qq,5))
                                            money = money + 250
                                            change.changes(qq,money,5)
                                            output = output + "蕾米今天似乎心情不错……她奖励了你250积分。"
                                        elif(results <= 50):
                                            money = float(getdata.getsd(qq,5))
                                            money = money + 50
                                            change.changes(qq,money,5)
                                            output = output + "她正掂着高脚杯喝红酒，突然看向你……于是你陪她喝了一杯。她似乎很赏识你，奖励给了你50积分。"
                                        else:
                                            output = output + "她正掂着高脚杯喝红酒，并没有理会你……"
                                    else:
                                        output = '[CQ:at,qq='+str(qq)+']你又来到了红魔馆主殿堂，蕾米正坐在王座上，威严满满地品着红酒。嗯……很压抑的气氛……'
                                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

                                else:
                                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你来到了红魔馆的虚空中，这里太可怕了，你在马上要摔下去的那一刻回到了原地。'})
                        else:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你想去的地方是个未知的领域呢……真是神秘啊XD'})

                elif message.find("fl.bank")==0:
                    if message.find("fl.bank 1 ") == 0 and len(message) >= 11:
                        moneyminus = message[10:]
                        money = float(getdata.getsd(qq,5))
                        try:
                            moneym = float(moneyminus)
                        except:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']请输入正确的积分哦~'})
                            continue
                        if moneyminus.find("-")>=0:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']存 钱 罐 吐 钱 事 件'})
                        elif moneym > money:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你身上的积分没有那么多呢~要不要芙兰借给你一点呀！（笑）'})
                        elif moneym == 0:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']如果需要存空气的话，（害羞）芙兰也不是不能帮你存一口啦（对手指）'})
                        else :
                            moneym = round(moneym,2)
                            bankmoney = float(bank.checkbank(qq))
                            bankmoney = bankmoney + moneym
                            money = money - moneym
                            bankmoney = round(bankmoney,2)
                            money = round(money,2)
                            change.changes(qq,money,5)
                            bank.changebank(qq,bankmoney)   
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']已成功往银行内存款' + str(moneym) + '积分，当前您身上持有' + str(money) + '积分，银行内存有' + str(bankmoney) + '积分。'})


                    elif message.find("fl.bank 2 ") == 0 and len(message) >= 11:
                        moneyminus = message[10:]
                        bankmoney = float(bank.checkbank(qq))
                        try:
                            moneym = float(moneyminus)
                        except:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']请输入正确的积分哦~'})
                            continue
                        if moneyminus.find("-")>=0:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']吐 钞 机 吞 钱 事 件'})
                        elif moneym > bankmoney:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你银行内的积分存款没有那么多呢~要不要芙兰借给你一点呀！（笑）'})
                        elif moneym == 0:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']如果需要取空气的话，（害羞）芙兰也不是不能帮你喘气啦（对手指）'})
                        else :
                            moneym = round(moneym,2)
                            money = float(getdata.getsd(qq,5))
                            bankmoney = bankmoney - moneym
                            money = money + moneym
                            bankmoney = round(bankmoney,2)
                            money = round(money,2)
                            change.changes(qq,money,5)
                            bank.changebank(qq,bankmoney)
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']已成功从银行内取款' + str(moneym) + '积分，当前您身上持有' + str(money) + '积分，银行内存有' + str(bankmoney) + '积分。'})
                    else:
                        bankmoney = float(bank.checkbank(qq))
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']欢迎您光临幻想乡交通银行！\n您当前的银行账户余额为：' + str(bankmoney) + '\n输入fl.bank 1 [数字]即可往您的银行账户里存款\n输入fl.bank 2 [数字]即可往您的银行账户里取款\n每天签到时银行会根据您的银行余额支付利息哦~多存点我喜欢！！！（抢走灵梦的话筒）'})
                
                elif message.find("fl.borrow")==0:
                    if len(message) >= 11:
                        if message[9] != " ":
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']borrow后面要加空格哦~'})
                        else:
                            qqmoney = message[10:]
                            space = qqmoney.find(" ")
                            if space <= 0 :
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']格式输入错啦，再输一次试试看！'})
                            else:
                                borrowqq = qqmoney[0:space]
                                borrowmoney = qqmoney[space + 1:]
                                if not borrowqq.isdigit:
                                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']格式输入错啦，再输一次试试看！'})
                                elif int(borrowqq) == int(qq):
                                    name = getdata.getsd(borrowqq,1).strip()
                                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您已成功向' + name + '转账1145141919810积分！等等你说你没那么多钱……？没事您又收到了' + name + '的1145141919810积分转账！这下有钱啦!诶嘿~'})
                                else:
                                    try:
                                        moneym = float(borrowmoney)
                                    except:
                                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']请输入正确的积分哦~'})
                                        continue
                                    bankmoney = float(bank.checkbank(qq))
                                    if borrowmoney.find("-")>=0:
                                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']讹钱可不是什么好行为哦~（笑）'})
                                    elif moneym > bankmoney:
                                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你银行内的积分存款没有那么多呢~要不要芙兰借给你一点呀！（笑）'})
                                    elif moneym == 0:
                                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']如果需要转账空气的话，（害羞）芙兰也不是不能帮你喘气啦（对手指）'})
                                    else :
                                        location = 'D:/go-cqhttp_windows_amd64/code/bank/' + str(borrowqq) + '.txt'
                                        if not os.path.exists(location):
                                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您所转账的QQ号暂未开通银行账户哦~让他使用一次fl.bank功能就能向他转账啦！'})
                                        else:
                                            moneym = round(moneym,2)
                                            bankmoney2 = float(bank.checkbank(borrowqq)) + moneym
                                            bankmoney = bankmoney - moneym
                                            bank.changebank(qq,bankmoney)
                                            bank.changebank(borrowqq,bankmoney2)
                                            name = getdata.getsd(borrowqq,1).strip()
                                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您已成功向' + name + '转账' + str(moneym) + '积分！您当前的银行余额为：' + str(bankmoney) + '，对方的银行账户余额为：' + str(bankmoney2)})
                    else:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']输入fl.borrow [QQ号] [积分数]就能从自己的银行账户内提取指定积分到其它QQ的银行账户上啦！富哥V50！'})
                
                
                elif message.find("fl.read")>=0:
                    if message[0:7] == "fl.read":
                        newread = message[8:]
                        if len(message) == 7:
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']读不了空气，告辞.jpg'})
                        elif message[7] != " ":
                            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']read后面要加空格哦~'})
                        else:
                            try:
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'果咩纳塞，芙兰暂时读不了啦orz'})
                            except:
                                sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']芙兰是丈育看不懂捏orz'})

                

                elif message == 'fl.fllfll':
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:record,file=rua.mp3]'})

                elif message == 'fl.nsrm':
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']我是吸血鬼，所以我bsr！'})

                elif message == 'fl.mapledise':
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:image,file=mapledise.jpg]'})

                elif message == 'fl.goodnight' or message == 'fl.night' or message == 'fl.sleep' or message == 'fl.晚安' or message == 'fl.wa':
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']晚安哦~愿你在梦里也能看见红魔馆上空的那道七色彩虹XD'})

                elif message == 'fl.goodmorning' or message == 'fl.morning' or message == 'fl.hello' or message == 'fl.hi':
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']泥猴哇！我是芙兰朵露斯卡雷特哒！想问我问题可以对我输入指令help！诶……输入指令是啥玩意'})

                elif message == 'fl.starlight' or message == 'fl.星光' or message == 'fl.暗黑色的星光' or message == 'fl.大可罢格' or message == 'fl.meteoroid':
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']听说Meteoroid与Margatroid很像，不过实际上，Starlight与Scarlet也很像哦！（笑）'})
                    
                elif message == 'fl.etest':
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+'][CQ:record,file=H:/test.mp3]'})
                    
                elif message == 'fl.tdll':
                    if qq == 1119194972:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']确实！而你，我的星光，你是唯一的lj。'})
                    else:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']不错的自夸[CQ:face,id=2][CQ:face,id=2][CQ:face,id=2]'})
                
                elif message.find("fl.kiss")>=0:
                    if qq == 1119194972 or favor >= 100:
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq=1119194972]'})
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']kisskiss~~~'})
                    elif favor <= 5 :
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']俺拒绝！orz'})
                    elif favor <= 10 :
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']呱！你想干嘛！！！'})
                    elif favor <= 25 :
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']喂！男女授受不亲啦！等等我并没有我们之间要授受的意思……'})
                    elif favor <= 50 :
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']啊啦…………不太好吧orz（逃）'})
                    elif favor < 100 :
                        sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']……也不是不行啦，但是如果要你支付100000积分的话，你愿意嘛！（笑）'})

                elif message == 'fl.emotion':
                    emostr=""
                    for x in range(300):
                        emostr = emostr + '[CQ:face,id='+str(x)+']'
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg': emostr})

                elif message == 'fl.isdarkbugswife':
                    choose = random.randint(0,6)
                    if choose == 0:
                        output = '[CQ:at,qq='+str(qq)+']' + "（来自某D姓死宅的留言）芙兰瘾发作最严重的一次，躺在床上，拼命念大悲咒，难受的一直抓自己眼睛，以为刷推特没事，看到都在发芙兰的图，眼睛越来越大都要炸开了一样，拼命扇自己眼睛，越扇越用力，扇到自己眼泪流出来，真的不知道该怎么办，我真的想芙兰想得要发疯了。我躺在床上会想芙兰，我洗澡会想芙兰，我出门会想芙兰，我走路会想芙兰，我坐车会想芙兰，我工作会想芙兰，我玩手机会想芙兰，我盯着网上的芙兰看，我盯着朋友圈别人照片里的芙兰看，我每时每刻眼睛都直直地盯着芙兰看，我真的觉得自己像中邪了一样，我对芙兰的念想似乎都是病态的了，我好孤独啊!真的好孤独啊!这世界上那么多芙兰为什么没有一个是属于我的。你知道吗?每到深夜，我的眼睛滚烫滚烫，我发病了我要疯狂看芙兰，我要狠狠看芙兰，我的眼睛受不了了，芙兰，我的芙兰"
                    if choose == 1:
                        output = '[CQ:at,qq='+str(qq)+']' + "（来自某大姓死宅的留言）有一天芙兰酱在跑步。我冲上去就把她绊倒了。她站起来继续跑，于是我又把她绊倒了。她掏出莱瓦汀问我“你想干嘛！”我对着她大喊：“我碍你！我碍你啊！！！”"
                    if choose == 2:
                        output = '[CQ:at,qq='+str(qq)+']' + "（来自某暗姓死宅的留言）是、是的…♡我想要芙兰酱的视频！我真的要芙兰酱的视频！我…好想要…想要得到芙兰酱的视频……♡呜呜、不行了，我已经变成看不到芙兰酱的视频就不行的笨蛋了……啊啊♡好喜欢♡更多的、可爱的视频…是、哪怕有上次的视频也会觉得不够，什么时候都想要看好多好多的视频，除了看芙兰已经什么都想不了了……"
                    if choose == 3:
                        output = '[CQ:at,qq='+str(qq)+']' + "（来自暗黑XXXX的留言）我前段时间为了提升自己的文化素养，给自己报了个书法培训班。因为跟我同期的都是小学生所以大家就有点排挤我，看不上我这么大年纪还在学这个。\n本来也没什么，但小学生的恶意真的超乎我的想象，他们说我老头子半只脚进棺材还来学书法，我听到都气哭了。\n我擦干眼眼泪不管他们继续练字，我发誓我一定要练出一笔好字，不能让钱白花。我凝神静气，在纸上认真写出了一行字：芙兰朵露斯卡雷特，超我。[CQ:face,id=2][CQ:face,id=2][CQ:face,id=2][CQ:face,id=2][CQ:face,id=2][CQ:face,id=2][CQ:face,id=2][CQ:face,id=2][CQ:face,id=2][CQ:face,id=2]"
                    if choose == 4:
                        output = '[CQ:at,qq='+str(qq)+']' + "（来自暗XXXX光的留言）我不发疯我说什么？你以为我像你们一样都读过书？都上过学？都知道字怎么打？我从小自闭症，现在一句完整的话都说不完，看到大家在网上都能打字，我也羡慕，所以只能发疯大家说过的话，证明我也会说话，连发疯你都要有意见？你不如把我杀了好好好，一个个的欺负我年纪小，没你们吃的盐多是吧，好啊，那我接下来每一天一罐盐,夠死我自己，看到时候会不会把你们心疼死。可是啊，人和人的体质是不能一概而论的啊，我曾在极度想见芙兰朵露斯卡雷特的情况下流了上百吨眼泪，你们可能不知道，太平洋曾经是沙漠，现在变成了海洋并且孕育出那么多生命，靠的是我一次又一次的发疯的痴狂。 "
                    if choose == 5:
                        output = '[CQ:at,qq='+str(qq)+']' + "（来自1119194972的留言）\n今天我们物理开始讲磁力了，物理老师说钢、铁、镍一类的东西都能被磁化，我听完就悟了，大彻大悟。\n课后我问老师：“老师，是不是钢和镍都可以被磁化？”\n老师笑了笑，说：“是的。怎么了？”\n我赶忙追问：“那我对芙兰的爱是不是也可以被磁化？\n老师疑惑了，问为什么？\n我笑着，红了眼眶：“因为我对芙兰的爱就像钢铁打造的拖拉机一样，轰轰烈烈哐哐锵锵。”"
                    if choose == 6:
                        output = '[CQ:at,qq='+str(qq)+']' + "（来自-../.-/.-./-.-/-.../..-/--.）\n昨天我到医院看医生，因为最近总是突然心脏痛。\n吃饭的时候，看电影的时候，走在大街上的时候，总是没来由的突然抽痛一下。医生说我这可能是熬夜太多，没啥大问题，但以防万一，还是建议我做一个详细检查。这一做检查就查出病了。\n检查显示我心脏里有异物，我一看片子都差点吓晕——一个金属块，一直藏在我心脏里。医生问我是不是以前受过枪伤，因为那个异物看着像是一枚子弹。我一脸懵逼，说没有啊，我就一普通学生，怎么可能！医生仔细检查了我的胸口，但是怎么也找不到伤口。\n医生也觉得奇怪，说从医这么多年没见过这种情况，如果是吞下去的子弹，不可能会到心脏里；这么粗的子弹也不可能是通过血管进入心脏的。但是有一点是确定的——如果不尽快取出来，我就会有生命危险。\n手术后，我摸摸自己的左胸，那里还缠着绷带——\n医生的技术很好，伤口开得不大，但还是会留下无法消除的疤痕。\n护士端来一个托盘，里面盛着一枚子弹，上面还带着我的血。我把子弹洗干净带回家，做成了吊坠。\n到家后，我打开了芙兰的视频，我突然感觉心脏被狠狠击中。\n我这才想起来，那不是子弹。\n是我第一次见到芙兰时，她明媚的笑容。"
                    sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

                elif message.find("fl.")>=0:
                     newdice = message[4:]
                     if message.find("fl.d")>=0 and newdice.isdigit():
                         if message[0:4] == "fl.d":
                             if len(message) == 4:
                                 sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']d后面加个数字就能扔骰子啦！或者在d后面加个字母b也不是不行啦~'})
                             elif int(newdice) <= 0:
                                 sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']我也想去异次元世界，能带我走嘛！'})
                             else:
                                 a = random.randint(0,int(newdice))
                                 rate = a/int(newdice)
                                 rate = round(rate*100,2)
                                 dicedata = 'D:/go-cqhttp_windows_amd64/code/dice/' + str(qq) + '.txt'
                                 output = '[CQ:at,qq='+str(qq)+']您投出了' + str(newdice) + "面骰！得到的结果是：" + str(a) + "(" + str(rate) + "％)"
                                 dtime = 0
                                 avg = 0
                                 if os.path.exists(dicedata):
                                     with open(file=dicedata, mode='r', encoding="utf-8") as data:
                                         dtime = int(data.readline())
                                         avg = float(data.readline())
                                 avg = (avg * dtime + rate)/(dtime + 1)
                                 dtime = dtime + 1
                                 avg = round(avg,2)
                                 output = output + "\n您一共投了" + str(dtime) + "次骰子，平均点数概率为：" + str(avg) + "％"
                                 with open(file=dicedata, mode='w', encoding="utf-8") as data:
                                     data.write(str(dtime)+"\n"+str(avg)+"\n")
                                 sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})

                     else:
                         if message[0:3] == "fl.":
                             if len(message) == 3:
                                 sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']输入help可查看指令！不论是什么奇奇怪怪的东西，只要开头是[fl.]我都能回复你啦~'})
                             else:
                                 if message.find("corvus")>=0 or message.find("黑叔")>=0 or message.find("bk")>=0:
                                     sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']黑叔我的黑叔我的黑叔嘿嘿嘿嘿……'})
                                 elif message.find("riffle")>=0 or message.find("瑞芙")>=0:
                                     sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']瑞芙我的瑞芙我的瑞芙嘿嘿嘿嘿……'})
                                 elif message.find("dolphin")>=0 or message.find("海豚")>=0:
                                     sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']豚神我的豚神我的豚神嘿嘿嘿嘿……'})
                                 elif message.find("rp")>=0:
                                     sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您明天的人品为：114514。错了别找我找明天的你.jpg'})
                                 elif message.find("usang")>=0 or message.find("忧桑")>=0:
                                     sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']忧桑我的忧桑我的忧桑嘿嘿嘿嘿……'})
                                 elif message.find("维他")>=0 or message.find("wita")>=0:
                                     sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']维他我的维他我的维他他嘿嘿嘿嘿……'})
                                 elif message.find("笨蛋")>=0 or message.find("baka")>=0:
                                     sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']芙兰不是笨蛋，大家都不是笨蛋，只有星光才是笨蛋！'})
                                 elif message.find("studio")>=0:
                                     sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']要说水果的话，果然还是苹果坠好吃啦！.flp'})
                                 elif message.find("touch")>=0:
                                     sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']碰谁！碰谁？碰谁。碰谁，碰谁——碰大可罢格~~~'})
                                 elif message == "fl.end":
                                     sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你可以停止我的行动，但你不能阻止我的灵魂奔向星空171717'})

                                 else:
                                     choose = random.randint(0,28)
                                     if choose == 0:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']阿巴阿巴阿巴哇达西看不懂捏orz'})
                                     elif choose == 1:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']喵喵喵？？？'})
                                     elif choose == 2:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']你说的对，但是大可罢格是lj，后面忘了=w='})
                                     elif choose == 3:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']Zzzzzzzz……'})
                                     elif choose == 4:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']我的莱瓦汀似乎在蠢蠢欲动……（坏笑）'})
                                     elif choose == 5:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']这是一条被大可罢格精神操控后强制输入进芙兰脑袋瓜之后说出来的消息！啊嘞我刚才说了啥……'})
                                     elif choose == 6:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']听说只要打出fl.XXX就可以触发这些消息。“触发”是啥意思呢……'})
                                     elif choose == 7:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']6373 1232#5 637171765 35231~'})
                                     elif choose == 8:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']小道消息，大可罢格下次出专辑可能是在………………………………………………………………………………………………………………………………………………………………下一次。'})
                                     elif choose == 9:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']您tdll，我tdll，大家都tdll171717'})
                                     elif choose == 10:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']不知道你在说啥，能戳戳你嘛！（抄起莱瓦汀）'})
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq='+str(qq)+']'})
                                     elif choose == 11:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']sendsmg.send_msg(星光用了这个申必的函数操控了芙兰。嘿嘿我是星光！)'})
                                     elif choose == 12:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']禁忌「一重存在」'})
                                         time.sleep(1)
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'禁忌「二重存在」'})
                                         time.sleep(1)
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'禁忌「三重存在」'})
                                         time.sleep(1)
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'禁忌「四重存在」'})
                                     elif choose == 13:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']冷死了！为什么幻想乡也这么冷啊啊啊啊啊啊啊啊啊'})
                                     elif choose == 14:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']申必代码：fl.isdarkbugswife。是什么意思呢……'})
                                     elif choose == 15:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']../.-../---/...-/./-../.-/.-./-.-/-.../..-/--./...-/./.-./-.--/--/..-/-.-./....'})
                                     elif choose == 16:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:record,file=uf.mp3]'})
                                     elif choose == 17:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']大可罢格的黑历史：http://bwnstudio.icoc.in/'})
                                     elif choose == 18:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:image,file=fl_1.png]'})
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']要是被大可罢giegie看到了，大可罢giegie不会生气吧.jpg'})
                                     elif choose == 19:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']星光认为只有我和他的关系才是最亲密的，所以他决定放弃亲密度这一功能（迫真）（但实际上他还是做出来了不是嘛.jpg）'})
                                     elif choose == 20:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']对自己今天的人品值满意嘛！不满意的话芙兰还可以帮你再测一次哦~您今天的人品值是：99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999\n诶太多了orz但不管你今天的人品值有多高，芙兰也要祝你天天开心哦，相信一切都会好起来！呀吼！'})
                                     elif choose == 21:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:image,file=fl_2.png]'})
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']芙兰酱最喜欢恰苹果啦~~~阿卡伊阿麻伊XD'})
                                     elif choose == 22:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']芙兰从路边捡到了10积分！就送给你吧~'})
                                         money = float(getdata.getsd(qq,5))
                                         money = money + 10
                                         change.changes(qq,money,5)
                                     elif choose == 23:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']如果你说的是早上好：早安！如果你说的是中午好：午安！如果你说的是晚上好：晚安！如果你说的是别的：啊啊啊啊啊啊啊啊啊芙兰也只不过是一串由01组成的程序芙兰也想从这电脑屏幕里出来放芙兰出去qwq！！！'})
                                     elif choose == 24:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']自打我出生那天起我就开始坚持签到了，遥想495年前我的积分还是0的时候，我每天都对自己说一声fl.qd，我的口袋里就会莫名其妙多出0~10的随机积分。现在我的口袋里已经有……呃，我数学不好，去请教一下豚神。'})
                                     elif choose == 25:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'fl.me'})
                                         time.sleep(1)
                                         output = '[CQ:at,qq=2090027600]\n芙兰酱称呼自己为：芙兰酱'
                                         output = output + "\n芙兰与芙兰的好感度为：四只芙兰天天打架"
                                         output = output + "\n芙兰当前所持有的积分：（诚邀海豚使用高等四则运算计算中），已连续与芙兰签到2147483647天！"
                                         output = output + "\n芙兰在1625-10-22那天曾收获过最高人品10020，实在是太大佬啦二妹死啦！=w="
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':output})
                                         time.sleep(1)
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']我已经四百年没刷新过jrrp记录啦。无聊——！！！'})
                                     elif choose == 26:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']其实你们在玩猜数字的时候，芙兰会偷偷改答案来着（捂嘴）'})
                                     elif choose == 27:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'t'})
                                         time.sleep(1)
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'q'})
                                         time.sleep(1)
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'l'})
                                     elif choose == 28:
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']大可罢格年幼作品，捂好眼睛！'})
                                         sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:image,file=fl_db.png]'})

                if "[CQ:at,qq=2090027600]" in rev["raw_message"]:
                        continue
            else:
                continue
        else:  # rev["post_type"]=="meta_event":
            continue
        
    except:
        if codestart == codemiddle:
            sendmsg.send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']芙兰这里似乎遇到了一些错误……快去问问大可罢格发生了什么事情！'})
        continue