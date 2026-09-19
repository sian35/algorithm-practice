def solution(s):
    answer = ''
    word = s.split(" ")
    new_list = []
    for one in word:
        new = ''
        for i in range(len(one)):
            if(i%2 ==0):
                new += one[i].upper()
            else:
                new += one[i].lower()

        new_list.append(new)

    answer = ' '.join(new_list)

    return answer