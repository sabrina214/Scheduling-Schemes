from tabulate import tabulate


def avg(rq, n):
    avg_ta, avg_wt = 0, 0
    for i in range(n):
        avg_wt += rq[i][3]
        avg_ta += rq[i][4]
    avg_wt /= n
    avg_ta /= n
    return [avg_wt, avg_ta]


def ps_time(rq, n):
    wt = 0
    service_time = 0
    for i in range(1, n):
        rq[i - 1][3] = wt
        service_time += rq[i - 1][2]
        rq[i - 1][4] = service_time
        wt = service_time - rq[i][1]
        if wt < 0:
            wt = service_time = 0
    rq[n - 1][3] = wt
    rq[n - 1][4] = service_time + rq[n - 1][2]


def gc_start(total_bt):
    print(' --', end='')
    for i in range(1, total_bt):
        print('---',end='')
    print('\n|', end='')


def gc_end(total_bt):
    print()
    for i in range(0, total_bt):
        print('|--', end='')
    print('|')
    for i in range(0, total_bt+1):
        print(str(i))


def show(rq, avg_wt, avg_ta):
    # headers = ['SNo.', 'PID', 'Arrival-time', 'CPU-time', 'Priority', 'Waiting_time', 'Turnaround_time']
    headers = ['SNo.', 'PID', 'Arrival-time', 'CPU-time', 'Waiting_time', 'Turnaround_time']
    print(tabulate(rq, headers, showindex='always'))
    print("Average waiting time : " + str(avg_wt) +
          "\nAverage turnaround time : " + str(avg_ta)
          )
