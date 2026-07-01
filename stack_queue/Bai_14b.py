from collections import deque

class HitCounter:
    def __init__(self, time_window=300):
        self.queue = deque()
        self.time_window = time_window

    def log_hit(self, timestamp):
        self.queue.append(timestamp)
        self._clean_old_hits(timestamp)

    def get_hits(self, current_timestamp):
        self._clean_old_hits(current_timestamp)
        return len(self.queue)

    def _clean_old_hits(self, current_time):
        while self.queue and self.queue[0] <= current_time - self.time_window:
            self.queue.popleft()


hc = HitCounter(time_window=300)
hc.log_hit(100); hc.log_hit(200); hc.log_hit(500)
print("Bài 14 - Số hits tại mốc 500s:", hc.get_hits(500))