from sched import auxiliary as aux


class schedule:
    def __init__(self, ready_queue):
        self.rq = ready_queue.processes
        self.n = ready_queue.n
        self.avg_wt = 0
        self.avg_ta = 0

    def ps_time(self):
        aux.ps_time(self.rq, self.n)

    def show(self):
        self.ps_time()
        (self.avg_wt, self.avg_ta) = aux.avg(self.rq, self.n)
        print('\nFCFS SCHEDULING')
        aux.show(self.rq, self.avg_wt, self.avg_ta)
