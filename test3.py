data = [[1,2,3],
        [4,5,6],
        [7,8,9]]

rsum_list = list()
csum_list = list()
for i in range(3):
        rsum = 0
        csum = 0
        for j in range(3):
                rsum += data[i][j]
        rsum_list.append(rsum)

print(rsum_list)
for i in range(3):
        rsum = 0
        csum = 0
        for z in range(3):
                csum += data[z][i]
        csum_list.append(csum)
print(csum_list)