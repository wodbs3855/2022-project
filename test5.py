fr=['apple','banana','grapes','pear']
prices =(100,500,1200,1500)

for a,(b,n) in enumerate(zip(fr,prices),start=1):
    print("{} {}가격 {}".format(a,b,n))

    #zip은 튜플형태로 변환봔환되니까 (a,n)으로 묶어줌
    