def solution(a, b):
    answer = 0
    min_ = min(a,b)
    max_ = max(a,b)
    for i in range(min_, max_+1):
        answer += i
    
    return answer