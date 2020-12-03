def find_waiting_time(bt):
    waiting_time = list()
    for i in range(len(bt)):
        if i==0:
            waiting_time.append(0)
        else:
            waiting_time.append(waiting_time[i-1] +bt[i-1])
    return waiting_time

def turn_around_time(wt, bt):
    turnaround_time = [sum(x) for x in zip(wt, bt)]
    return turnaround_time

def first_come_first_serve(processes,burst_time):
    waiting_time = find_waiting_time(burst_time)
    turnaround_time = turn_around_time(waiting_time, burst_time)
    print('Process Id\tBurst Time\tWaiting Time\tTurnaournd Time')
    for i in range(len(processes)):
        print(f'{processes[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}')
    print(f'Average waiting time is {sum(waiting_time)/len(waiting_time)}')
    print(f'Average turnaround time is {sum(turnaround_time)/len(turnaround_time)}')
def shortest_job_first(p, bt):
    sorted_tuple = sorted(zip(bt, p))
    burst_time_list = []
    process_id_list = []
    for i in range(len(sorted_tuple)):
        burst_time_list.append(sorted_tuple[i][0])
        process_id_list.append(sorted_tuple[i][1])
    wt = find_waiting_time(burst_time_list)
    tt = turn_around_time(wt,burst_time_list)
    print('Process Id\tBurst Time\tWaiting Time\tTurnaournd Time')
    for i in range(len(p)):
        print(f'{process_id_list[i]}\t\t{burst_time_list[i]}\t\t{wt[i]}\t\t{tt[i]}')
    print(f'Average waiting time is {sum(wt)/len(wt)}')
    print(f'Average turnaround time is {sum(tt)/len(tt)}')
def priority_first(process_id, priority_order, burst_time_list):
    process_list = []
    burst_new = []
    for i in priority_order:
        process_list.append(process_id[i-1])
        burst_new.append(burst_time_list[i-1])
    waiting_time_pf = find_waiting_time(burst_new)
    turnaround_time_pf = turn_around_time(waiting_time_pf,burst_new)
    print('Process Id\tBurst Time\tWaiting Time\tTurnaournd Time')
    for i in range(len(process_list)):
        print(f'{process_list[i]}\t\t{burst_new[i]}\t\t{waiting_time_pf[i]}\t\t{turnaround_time_pf[i]}')
    print(f'Average waiting time is {sum(waiting_time_pf)/len(waiting_time_pf)}')
    print(f'Average turnaround time is {sum(turnaround_time_pf)/len(turnaround_time_pf)}')


def roundrobin(p, burst, quantum):
    n = len(p)
    wt = [0] * len(p)
    rem_bt = [0] * n
    for i in range(n):
        rem_bt[i] = burst[i]
    t = 0
    while (True):
        done = True
        for i in range(n):
            if (rem_bt[i] > 0):
                done = False

                if (rem_bt[i] > quantum):
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t = t + rem_bt[i]
                    wt[i] = t - burst[i]
                    rem_bt[i] = 0
        if (done == True):
            break
    turnaround = turn_around_time(wt=wt, bt=burst)
    print('Process Id\tBurst Time\tWaiting Time\tTurnaournd Time')
    for i in range(len(p)):
        print(f'{p[i]}\t\t{burst[i]}\t\t{wt[i]}\t\t{turnaround[i]}')
    print(f'Average waiting time is {sum(wt) / len(wt)}')
    print(f'Average turnaround time is {sum(turnaround) / len(turnaround)}')
