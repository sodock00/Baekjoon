from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    total_weight = 0
    time = 0

    while trucks or total_weight != 0:
        time += 1
        total_weight -= bridge.popleft()

        if trucks:
            if total_weight + trucks[0] <= weight:
                truck = trucks.popleft()
                bridge.append(truck)
                total_weight += truck
            else:
                bridge.append(0)
        else:
            bridge.append(0)

    return time
