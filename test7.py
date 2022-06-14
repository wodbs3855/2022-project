from random import sample

lst = sorted(sample(range(1,31),6))
print(lst)

result=filter(lambda x : x%3==0, lst)

print(list(result))