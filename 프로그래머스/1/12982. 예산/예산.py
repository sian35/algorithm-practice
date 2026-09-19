def solution(d, budget):
    new_d = sorted(d)
    total=0
    answer = 0
    for money in new_d:
        total +=money
        if total > budget:
            break
        answer +=1

    return answer