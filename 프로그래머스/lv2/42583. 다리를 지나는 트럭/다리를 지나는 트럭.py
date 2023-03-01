from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_dq = deque([0] * bridge_length)
    bridge_weight = 0 
    while bridge_dq:
        answer += 1
        arrived_car = bridge_dq.popleft()
        if arrived_car != 0:
            bridge_weight -= arrived_car
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:      
                t = truck_weights.pop(0)
                bridge_dq.append(t)
                bridge_weight += t
            else:
                bridge_dq.append(0)
                        
    return answer