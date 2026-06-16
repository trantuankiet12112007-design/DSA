def find_min_passes_between_states(start_state, end_state):
    n = len(start_state)
    passes = 0
    current_state = list(start_state)
    
    if current_state == end_state:
        return passes
        
    for i in range(n):
        passes += 1
        for j in range(0, n - i - 1):
            if current_state[j] > current_state[j + 1]:
                current_state[j], current_state[j + 1] = current_state[j + 1], current_state[j]
        if current_state == end_state:
            return passes
    return passes

start = [4, 3, 2, 1]
end = [3, 2, 1, 4]
print(find_min_passes_between_states(start, end))