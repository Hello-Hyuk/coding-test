import numpy as np
def solution(places):
    places_np = np.array(places)

    answer = []
    round = 0
    for place in places_np:
        ans = []
        round += 1
        idx = []
        for i in range(len(place[0])):
            for j in range(len(place)):
                if place[i][j] == "P":
                    idx.append((i,j))
        idx_np = np.array(idx)

        count = 0
        print(idx)
        for i in range(len(idx)):
            for j in range(i+1,len(idx)):
                count += 1
                calc = abs(idx_np[i]-idx_np[j])
                dist = np.sum(calc)

                if dist <= 2 :
                    list = ""
                    max_r = max(idx_np[i][0],idx_np[j][0])
                    max_c = max(idx_np[i][1],idx_np[j][1])
                    min_r = min(idx_np[i][0],idx_np[j][0])
                    min_c = min(idx_np[i][1],idx_np[j][1])
                    for k in range(max_r-min_r+1):
                        list += place[min_r:max_r+1][k][min_c:max_c+1]

                    if "O" in list or dist==1:
                        ans.append(0)

        print(ans)

        if not ans:
            answer.append(1)
        else :
            answer.append(0)

    return answer