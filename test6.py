planets = [('수성', 1235, 0.3),('금성',5512,0.7),('태양',1244,0)]


a = sorted(planets, key=lambda x : x[1])
planets.sort(key=lambda x : x[0], reverse=True)
#key파라미터로 lambda함수를 넘겨주어 element의 정렬조건 설정
print(planets)
