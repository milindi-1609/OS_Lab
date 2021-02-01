from scheduler import first_come_first_serve,shortest_job_first,priority_first,roundrobin
processes = [1,2,3]
burst_time = [10,5,8]
priority_list_new = [2,1,3]
print('First come first serve')
first_come_first_serve(processes=processes, burst_time= burst_time)
print('Shortest Job First')
shortest_job_first(p = processes, bt = burst_time)
priority_first(process_id = processes, priority_order=priority_list_new,burst_time_list = burst_time)
roundrobin(p=processes, burst=burst_time, quantum=2
