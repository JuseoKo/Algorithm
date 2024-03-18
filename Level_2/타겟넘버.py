def solution(numbers, target):
    result = [0]  #계산 결과

    for num in numbers:
        calc = []

        for leaf in result:
            calc.append(leaf + num)  # 더하는 경우
            calc.append(leaf - num)  # 빼는 경우

        result = calc

    return result.count(target)
