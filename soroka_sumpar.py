m=[[156, 784, 15, 367], [98, 67, 111], [344, 658,14, 3]]
sumpar = 0
for i in m:
    for j in i:
        if j % 2 == 0:
            sumpar = sumpar + j
print(sumpar)
