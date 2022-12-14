def stars(n):
    L=[]
    #3일경우 즉 베이스값은 *로 채움
    if n == 1:
        return ['*']
    stars_mini=stars(n//3)
    for star in stars_mini:
        L.append(star*3)
        #양쪽에 이전 차수 별값이 존재하고 중앙에 n//3만큼의 공백 삽입
    for star in stars_mini:
        L.append(star+' '*(n//3)+star)
    for star in stars_mini:
        L.append(star*3)
    return L

n=int(input())
print('\n'.join(stars(n)))