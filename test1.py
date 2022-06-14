import random



while True:
    b = {random.randint(1,100)for i in range(10)}
    if len(b) == 10:
        break
print(b)

for j in b:
    print(j, end= ' ')
