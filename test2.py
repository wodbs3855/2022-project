m = [[1,2],[3,4],[5,6],[7,8]]

for i in m:
    for j in i:
        print(j, end=' ')
    print()
#zip은 동일한 개수로 이루어진 자료형을 묶어주는 역할
for i in list(zip(*m)):#*를 붙여 col끼리 서로 엮어줌 *args 파라미타 몇개 받을지 모를떄 튜플로 전달
    for j in i:
        print(j,end='')
    print()