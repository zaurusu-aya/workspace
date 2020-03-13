import random
import time
points = [0, 1]
total = 0
w = 2
while True:
    i = random.randint(0, 1)
    points.append(i)
    for i in points:
        w += 1
        total = total + i
        print('合計:' + str(total) + '\n--------------------------------------')
        h = total / w
        print('平均:' + str(h) + '\n--------------------------------------')
        print('計算回数:' + str(w) + '\n--------------------------------------')


