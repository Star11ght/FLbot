import random
import os

def numberguess(qq):
    a = random.randint(0,9)
    b = random.randint(0,9)
    while a == b:
        b = random.randint(0,9)
    c = random.randint(0,9)
    while a == c or b == c:
        c = random.randint(0,9)
    d = random.randint(0,9)
    while a == d or b == d or c == d:
        d = random.randint(0,9)
    location = 'D:/go-cqhttp_windows_amd64/code/guessnum/' + str(qq) + '.txt'
    with open(file=location, mode='w', encoding="utf-8") as data:
            data.write(str(a)+"\n")
            data.write(str(b)+"\n")
            data.write(str(c)+"\n")
            data.write(str(d)+"\n")
            data.write("8\n")
            data.close()

def gameend(qq):
    location = 'D:/go-cqhttp_windows_amd64/code/guessnum/' + str(qq) + '.txt'
    os.remove(location)
