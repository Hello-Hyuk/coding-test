import numpy as np

def solution(alp, cop, problems):
    max_alp, max_cop = 0,0
    
    for problem in problems:
        max_alp = max(max_alp,problem[0])
        max_cop = max(max_cop,problem[1])
    #dp
    dp = np.ones((max_alp+1,max_cop+1),np.float64) * np.inf
    alp = min(alp, max_alp)  # 둘중 하나라도 목표값을 넘어가면 안된다.
    cop = min(cop, max_cop) 
    dp[alp][cop] = 0
    for a in range(alp,max_alp+1):
        for c in range(cop,max_cop+1):
            # upgrade rwd by study
            if a < max_alp:
                dp[a+1][c] = min(dp[a+1][c],dp[a][c]+1)
            if c < max_cop:
                dp[a][c+1] = min(dp[a][c+1],dp[a][c]+1) 
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a >= alp_req and c >= cop_req:
                    next_alp = min(a+alp_rwd,max_alp)
                    next_cop = min(c+cop_rwd,max_cop)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop],dp[a][c]+cost)
    
    return dp[max_alp][max_cop]
