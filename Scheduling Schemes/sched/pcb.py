class pcb:
    """initialize PCB for different processes"""

    def __init__(self, pid, burst_time, priority, arrival_time=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
