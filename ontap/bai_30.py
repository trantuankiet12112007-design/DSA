from collections import deque

def round_robin(arrival_time, burst_time, quantum):
    n = len(burst_time)
    rem_time = burst_time.copy()
    completion_time = [0] * n
    
    processes = sorted(range(n), key=lambda x: arrival_time[x])
    
    q = deque()
    t = 0
    idx = 0 
    if n > 0:
        t = arrival_time[processes[0]]
        while idx < n and arrival_time[processes[idx]] <= t:
            q.append(processes[idx])
            idx += 1

    while q:
        p = q.popleft()
        
        exec_time = min(rem_time[p], quantum)
        t += exec_time
        rem_time[p] -= exec_time
        
        while idx < n and arrival_time[processes[idx]] <= t:
            q.append(processes[idx])
            idx += 1
            
        if rem_time[p] > 0:
            q.append(p)
        else:
            completion_time[p] = t
            
        if not q and idx < n:
            t = arrival_time[processes[idx]]
            while idx < n and arrival_time[processes[idx]] <= t:
                q.append(processes[idx])
                idx += 1
                
    return completion_time

arrival = [0, 1, 2]
burst = [5, 3, 8]
q = 2

res = round_robin(arrival, burst, q)
print("Thời điểm hoàn thành của các tiến trình:", res)