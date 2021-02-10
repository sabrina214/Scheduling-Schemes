import sched.auxiliary as aux


class schedule:
    def __init__(self, ready_queue):
        self.rq = ready_queue.processes
        self.n = ready_queue.n
        self.avg_wt = 0
        self.avg_ta = 0

    def ps_time(self):
        # sort according to burst times first then,
        # again wrt to arrival times
        # then use fcfs scheduling.
        self.rq = sorted(self.rq, key=lambda x: x[2])
        self.rq = sorted(self.rq, key=lambda x: x[1])
        aux.ps_time(self.rq, self.n)

    def show(self):
        self.ps_time()
        (self.avg_wt, self.avg_ta) = aux.avg(self.rq, self.n)
        print('\nSJF SCHEDULING')
        aux.show(self.rq, self.avg_wt, self.avg_ta)
