# Даны периоды онлайн статуса для 20 пользователей. Вывести промежутки времени, в которые пользователи были онлайн

import re
from datetime import datetime

fileIn = open('files/ex5_user_1_4.txt', 'r')
user1, user2 = input().split()

print(user1, user2)
x = fileIn.read()
y = re.findall("^"+user1+"\s.*", x, re.MULTILINE)
y1 = re.findall("^"+user2+"\s.*", x, re.MULTILINE)
y.sort()
y1.sort()
user1_online = []
user2_online = []
us1_us2_online = []
for t in y:
    g = t.split(" ")
    user1_online.append([int(g[1]), int(g[2])])
for t1 in y1:
    g1 = t1.split(' ')
    user2_online.append([int(g1[1]), int(g1[2])])

c = []
k = len(user1_online)
i = len(user2_online)
for j in range(i):
    for h in range(k):
        c = []
        if user1_online[h][0] < user2_online[j][0] < user1_online[h][1]:
            c.append(user2_online[j][0])
            if user2_online[j][1] < user1_online[h][1]:
                c.append(user2_online[j][1])
                us1_us2_online.append(c)
            else:
                c.append(user1_online[h][1])
                us1_us2_online.append(c)

for h in range(k):
    for j in range(i):
        c = []
        if user2_online[j][0] < user1_online[h][0] < user2_online[j][1]:
            c.append(user1_online[h][0])
            if user1_online[h][1] < user2_online[j][1]:
                c.append(user1_online[h][1])
                us1_us2_online.append(c)
            else:
                c.append(user2_online[j][1])
                us1_us2_online.append(c)

us1_us2_online.sort()

print("Пользователи " + user1 + " и " + user2 + " были одновременно в онлайне в следующие промежутки времени:")
for prom in us1_us2_online:
    print(datetime.fromtimestamp(prom[0]).strftime("%Y-%m-%d %H:%M:%S") + " - " +
          datetime.fromtimestamp(prom[1]).strftime("%Y-%m-%d %H:%M:%S"))