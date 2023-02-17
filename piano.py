from pydub import AudioSegment
import os

def musicmake(melody):
    x = len(melody)
    tune = ["" for i in range (500)]
    tunen = -1
    flag = 0
    for i in range(0,x):
        if (melody[i] == "(" or melody[i] == ")" or melody[i].isdigit()) and flag == 0:
            tunen = tunen + 1
            if melody[i] == "(" or melody[i] == ")":
                flag = 1
        elif melody[i].isdigit() and flag == 1:
            flag = 0
        tune[tunen] = tune[tunen] + melody[i]

    with open(file='D:/go-cqhttp_windows_amd64/code/piano/number.txt', mode='r', encoding="utf-8") as data:
        numbe = int(data.readline())
    numbe = numbe + 1
    with open(file='D:/go-cqhttp_windows_amd64/code/piano/number.txt', mode='w', encoding="utf-8") as data:
        data.write(str(numbe)) 
        
    for i in range(0,tunen+1):
        height = 5
        length = 3
        number = -1
        numn = 0
        halftune = 0
        long = len(tune[i])
        tori = tune[i]
        tfinal = ""
        for j in range (long):
            if tori[j]==")":
                height = height + 1
            elif tori[j]=="(":
                height = height - 1
            elif tori[j].isdigit():
                if int(tori[j])>=8:
                    numn = 2
                else:
                    number = int(tori[j])
                    numn = numn + 1
            elif tori[j]=="#":
                if number == 3 or number == 7 or number == 0:
                    halftune = 2
                else:
                    if number == 0 and height != 5:
                        return -1
                    number = number + 1
                    halftune = halftune + 1
            elif tori[j]=="b":
                if number == 1 or number == 4 or number == 0:
                    halftune = 2
                else:
                    halftune = halftune + 1
            elif tori[j]=="+":
                length = length + 1
            elif tori[j]=="-":
                length = length - 1
            else:
                print("Input Error!")
                return -1
        if height > 8 or height < 2 or length > 5 or length < 1 or numn != 1 or halftune > 1:
            print("Input Error!")
            return -1
        if number == 1:
            tfinal = "C"
        elif number == 2:
            tfinal = "D"
        elif number == 3:
            tfinal = "E"
        elif number == 4:
            tfinal = "F"
        elif number == 5:
            tfinal = "G"
        elif number == 6:
            tfinal = "A"
        elif number == 7:
            tfinal = "B"
        elif number == 0:
            tfinal = "0"
        if halftune == 1:
            tfinal = tfinal + "b"
        if number!=0 :
            tfinal = tfinal + str(height)
        if length == 2:
            tfinal = tfinal + "_4"
        elif length == 3:
            tfinal = tfinal + "_8"
        elif length == 4:
            tfinal = tfinal + "_16"
        elif length == 5:
            tfinal = tfinal + "_32"
        print(tfinal)

        location = 'D:/go-cqhttp_windows_amd64/data/voices/'
        new2 = location + tfinal + ".mp3"
        sound2=AudioSegment.from_mp3(new2)
        if i == 0:
            if tunen == 0:
                sound2.export('D:/go-cqhttp_windows_amd64/data/voices/' + str(numbe) + ".mp3", format="mp3")
                print("合成完成")
                return numbe
            else:
                sound2.export('D:/go-cqhttp_windows_amd64/code/piano/' + str(numbe) + "_0.mp3", format="mp3")
        else:
            new1='D:/go-cqhttp_windows_amd64/code/piano/' + str(numbe) + "_" + str(i-1) + ".mp3"
            sound1=AudioSegment.from_mp3(new1)
            sound = sound1 + sound2
            if i==tunen:
                sound.export('D:/go-cqhttp_windows_amd64/data/voices/' + str(numbe) + ".mp3", format="mp3")
                os.remove(new1)
                print("合成完成")
                return numbe
            else:
                sound.export('D:/go-cqhttp_windows_amd64/code/piano/' + str(numbe) + "_" + str(i) + ".mp3", format="mp3")
                os.remove(new1)
