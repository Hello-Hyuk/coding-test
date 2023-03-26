def solution(storey):
    answer = 0
    while storey:
        remainer = storey % 10
        if remainer > 5:
            answer += 10-remainer
            storey += 10
        elif remainer < 5:
            answer += remainer
        else :
            if ((storey // 10) % 10) >= 5:
                storey += 10
            answer += remainer
        storey //= 10
    print(answer)
    return answer
            
solution(16) #6 
solution(2554) #16
