from sched import process, fcfs, sjf, priority, round_robin_b, srtf


def main():

    n = int(input('Enter no. of processes : '))

    # enter time-slice values as single-space separated  values in a single line
    # time_slices = list(map(int, input('Enter time-slices for round-robin scheduler : ').split()))

    # create queue of n different processes
    # 1st parameter is for no. of processes and 2nd parameter
    # is for max-increment that is to be added to current arrival
    # time to generate next processes's arrival-time, in that way
    # we generate arrival-times in increasing order and
    # don't need to sort later.

    rq = process.job(n, 2)
    rq.show()

    # pass the ready queue for FCFS scheduling
    obj_1 = fcfs.schedule(rq)
    obj_1.show()

    # pass the ready queue for SJF scheduling
    obj_2 = sjf.schedule(rq)
    obj_2.show()

    # pass the ready queue for PRIORITY - NON-PREEMPTIVE scheduling
    # obj_3 = priority.schedule(rq)
    # obj_3.show()

    # pass the ready queue for ROUND-ROBIN scheduling alongwith timeslices
    # obj_4 = round_robin_b.schedule(rq, time_slices)
    # this shows the output of that ROUND-ROBIN scheduler whose
    # time-slice gave minimum avg. times
    # obj_4.show()

    # pass the ready queue for SRTF scheduling
    # obj_5 = srtf.schedule(rq)
    # obj_5.show()

    rq.avg_wt = [obj_1.avg_wt,
                 obj_2.avg_wt,
                 # obj_3.avg_wt,
                 # min(obj_4.avg_wt),
                 # obj_5.avg_wt
                 ]

    rq.avg_ta = [obj_1.avg_ta,
                 obj_2.avg_ta,
                 # obj_3.avg_ta,
                 # min(obj_4.avg_ta),
                 # obj_5.avg_ta
                 ]

    # rq.avg_wt = [obj_1.avg_wt,
    #              obj_2.avg_wt,
    #              obj_3.avg_wt,
    #              obj_4.avg_wt,
    #              obj_5.avg_wt
    #              ]
    #
    # rq.avg_ta = [obj_1.avg_ta,
    #              obj_2.avg_ta,
    #              obj_3.avg_ta,
    #              obj_4.avg_ta,
    #              obj_5.avg_ta
    #              ]

    rq.bar_chart()

    # obj_4.bar_chart()


if __name__ == '__main__':
    main()
