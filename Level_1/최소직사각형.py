def solution(sizes):
    x1 = []
    y1 = []
    for i in range(0, len(sizes)):
        x = sizes[i][0]
        y = sizes[i][1]
        if x > y :
            x1.append(x)
            y1.append(y)
        else:
            x1.append(y)
            y1.append(x)
    x1.sort()
    y1.sort()
    answer = x1[len(sizes)-1]*y1[len(sizes)-1]
    return answer

print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))