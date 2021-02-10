import random
import plotly.graph_objects as go
from tabulate import tabulate


class job:
    """create a job queue(list of PCBs)"""

    def __init__(self, n, max_increment=0):
        self.processes = []
        self.n = n
        # self.total_bt = 0
        self.avg_wt = []
        self.avg_ta = []

        self.__create_process_queue(max_increment)

    def __create_process_queue(self, k):
        # create a set of PIDs
        pids = set()
        while len(pids) != self.n:
            pids.add(random.randint(1000, 9999))
        at = 0
        for pid in pids:
            bt = random.randint(1, 20)
            # self.total_bt += bt
            # priority = random.randint(1, self.n)
            # pcb = [pid, at, bt, priority, None, None]
            pcb = [pid, at, bt, None, None]
            self.processes.append(pcb)
            x = random.randint(0, k)
            at += x

    def show(self):
        # headers = ['SNo.', 'PID', 'Arrival-time', 'CPU-time', 'Priority', 'Waiting_time', 'Turnaround_time']
        headers = ['SNo.', 'PID', 'Arrival-time', 'CPU-time', 'Waiting_time', 'Turnaround_time']
        print(tabulate(self.processes, headers, showindex='always'))

    def bar_chart(self):
        # schedulers = ['FCFS', 'SJF', 'PRIORITY', 'ROUND-ROBIN', 'SRTF']
        schedulers = ['FCFS', 'SJF']
        fig = go.Figure(data=[go.Bar(name='Average Waiting Time', x=schedulers, y=self.avg_wt),
                              go.Bar(name='Average TurnAround Time', x=schedulers, y=self.avg_ta)
                              ])
        fig.update_layout(title='Comparison chart of different schedulers',
                          yaxis=dict(title='Time in seconds'),
                          barmode='group')
        fig.show()
