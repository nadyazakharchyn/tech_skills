arr = [[156, 784, 15, 367], [98, 67, 111], [344, 658,14, 3]]
sum = 0 
for i in arr:
    for j in i:
        if j % 2 == 0:
            sum = sum + j
            print("We add", j, "and current sum is", sum)
            
print("Total Sum is", sum)