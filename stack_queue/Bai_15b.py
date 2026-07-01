from collections import deque

def round_robin_scheduling(processes, burst_times, quantum):
    queue = deque([[processes[i], burst_times[i]] for i in range(len(processes))])
    current_time = 0
    completion_times = {}

    while queue:
        p_name, remaining_time = queue.popleft()
        if remaining_time <= quantum:
            current_time += remaining_time
            completion_times[p_name] = current_time
        else:
            current_time += quantum
            queue.append([p_name, remaining_time - quantum])
    return completion_times


proc = ["P1", "P2", "P3"]
bt = [5, 2, 4]
print("Bài 15:", round_robin_scheduling(proc, bt, quantum=2))
