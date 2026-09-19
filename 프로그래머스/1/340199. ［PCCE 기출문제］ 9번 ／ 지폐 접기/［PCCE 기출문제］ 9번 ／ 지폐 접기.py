def solution(wallet, bill):
    answer = 0
    wallet_min = min(wallet)
    wallet_max = max(wallet)
    b1, b2= bill
    
    while wallet_min < min(b1,b2) or wallet_max < max(b1,b2):
        if b1 > b2:
            b1 = b1 // 2
        else:
            b2 = b2 // 2
        answer += 1
    
    return answer