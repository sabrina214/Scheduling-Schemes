import sched.auxiliary as aux


class schedule:

    def __init__(self, ready_queue):
        self.rq = ready_queue.processes
        self.n = ready_queue.n
        self.avg_wt = 0
        self.avg_ta = 0

    def ps_time(self):
        # sort according to priority first then
        # according to arrival times
        self.rq = sorted(self.rq, key=lambda x: x[3])
        self.rq = sorted(self.rq, key=lambda x: x[1])
        aux.ps_time(self.rq, self.n)

    def show(self):
        self.ps_time()
        (self.avg_wt, self.avg_ta) = aux.avg(self.rq, self.n)
        print('\nPRIORITY SCHEDULING - NON-PREEMPTIVE')
        aux.show(self.rq, self.avg_wt, self.avg_ta)

