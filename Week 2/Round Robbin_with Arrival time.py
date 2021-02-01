def CalcWaitingTime(process, wt_time, n, burst_time,quantum, completion_time,arrival_time):
    rem_time = []
    for val in burst_time:
        rem_time.append(val)
    t = 0
    arrival = 0
    while True:
        done = True
        for i in range(n):
            if rem_time[i] > 0:
                done = False
                if rem_time[i] > quantum and arrival_time[i] <= arrival:
                    t += quantum
                    rem_time[i] -= quantum
                    arrival +=1
                else:
                    if arrival_time[i] <= arrival:
                        arrival +=1
                        t += rem_time[i]
                        rem_time[i] = 0
                        completion_time[i] = t
        if done == True:
            break


def CalcTurnAroundTime(process, wt_time, n,burst_time,tat_time,completion_time,arrival_time):
    for i in range(n):
        tat_time[i] = completion_time[i] - arrival_time[i]
        wt_time[i] = tat_time[i] - burst_time[i]


def CalcAvgTime(process,n, burst_time, quantum, arrival_time):
    wt_time = []
    tat_time=[]
    completion_time=[]
    total_wt = 0
    total_tat = 0
    CalcWaitingTime(process, wt_time, n, burst_time, quantum, completion_time, arrival_time)
    CalcTurnAroundTime(process, wt_time, n, burst_time, tat_time, completion_time, arrival_time)
    print("PROCESS\tARRIVAL TIME\tBURST TIME\tCOMPLETION TIME\tTURN AROUND TIME\tWAITING TIME")
    for i in range(n):
        total_wt = total_wt + wt_time[i]
        total_tat = total_tat + tat_time[i];
        print(f"{i+1}\t{arrival_time[i]}\t{burst_time[i]}\t{completion_time[i]}\t{tat_time[i]}\t{wt_time[i]}")
    print(f"AVERAGE WAITING TIME {total_wt/n}")
    print(f"AVERAGE TURN AROUND TIME {total_tat/n}")


if __name__ == '__main__':
    quantum = 2
    arrival_time = [0,1,2,3]
    process = [1,2,3,4]
    burst_time = [5,4,2,1]
    n = len(process)
    CalcAvgTime(process,n, burst_time, quantum, arrival_time)
