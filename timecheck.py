import datetime

def times():
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    with open(file="time.txt", mode='r', encoding="utf-8") as time:
        today = time.readline()
        num = int(time.readline())
    today = today.strip()
    if date != today:
        num = num + 1
        with open(file="time.txt", mode='w', encoding="utf-8") as time:
            time.write(date+"\n")
            time.write(str(num)+"\n")
            time.close()
    return num

print("todaytime = " + str(times()))
