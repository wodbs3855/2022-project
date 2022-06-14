books = {'파이썬':['강환수'],
         'c언어':['강환수','이동규'],
         '개론':['강환수','이동규','신용현']}

for key, value in books.items():
    print(key, end=' ')
    for z in value:
        print(z,end=' ')
    print()



