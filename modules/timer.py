import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.elapsed = 0

    def start(self):
        self.start_time = time.time()

    def stop(self):
        if self.start_time is None:
            return 0
        self.elapsed = time.time() - self.start_time
        return self.elapsed