import sched.auxiliary as aux
import plotly.graph_objects as go


class schedule:
    def __init__(self, ready_queue, time_slices):
        self.rq = ready_queue.processes
        self.n = ready_queue.n
        self.time_slices = time_slices
        self.m = len(self.time_slices)
        self.avg_wt = [0] * self.m
        self.avg_ta = [0] * self.m

    def ps_time(self, ts):
        cpu_time = 0
        remaining = self.n
        flag = False
        i = 0

        r_times = [0] * self.n
        for i in range(self.n):
            r_times[i] = self.rq[i][2]

        while remaining:

            if ts >= r_times[i] > 0:
                cpu_time += r_times[i]
                r_times[i] = 0
                flag = True

            elif r_times[i] > 0:
                r_times[i] -= ts
                cpu_time += ts

            if r_times[i] == 0 and flag is True:
                remaining -= 1
                self.rq[i][4] = cpu_time - self.rq[i][1] - self.rq[i][2]
                self.rq[i][5] = cpu_time - self.rq[i][1]
                flag = False

            if i == self.n - 1:
                i = 0

            elif self.rq[(i + 1) % self.n][1] <= cpu_time:
                i += 1

            else:
                if r_times[i] == 0:
                    i += 1
                    cpu_time += self.rq[i % self.n][1] - cpu_time

                else:
                    i = 0

    def show(self):
        for i in range(self.m):
            self.ps_time(self.time_slices[i])
            self.avg_wt[i], self.avg_ta[i] = aux.avg(self.rq, self.n)
            print('\nROUND-ROBIN SCHEDULING : TIME-SLICE :- ' + str(self.time_slices[i]))
            aux.show(self.rq, self.avg_wt[i], self.avg_ta[i])

    def bar_chart(self):
        fig = go.Figure(data=[go.Bar(name="Average Waiting Time", x=self.time_slices, y=self.avg_wt),
                              go.Bar(name="Average Turnaround Time", x=self.time_slices, y=self.avg_ta)
                              ])

        fig.update_layout(title="Comparison of ROUND-ROBIN Schedulers with different time slices",
                          xaxis=dict(title="Time slices in seconds"),
                          yaxis=dict(title="Time in seconds"),
                          barmode="group")

        fig.show()
