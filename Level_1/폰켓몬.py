def solution(nums):
    poketmon_num = len(set(nums))
    max_poketmon = len(nums) / 2
    if poketmon_num > max_poketmon:
        answer = max_poketmon
    else:
        answer = poketmon_num
    return answer