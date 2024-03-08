## split_list_into_n_cores.py
## divide a list into groups and send each group to a processes
## groups is set as the limit of available logical cores in the host
## the list will the abecedary
## output will depend on the available logical cores of your host

import multiprocessing
import concurrent.futures
import os
import string
import sys

def initiate_thread(element):
    print('Letter {} processed by PID: {}'.format(element, os.getpid()))

def initiate_process(group):
    global n_threads
    print('Process {} with group - {}'.format(os.getpid(), group))
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_processes) as texecutor:
        result_threads = []
        futures = [ texecutor.submit(initiate_thread, g) for g in group ]
        for future in concurrent.futures.as_completed(futures):
            result_threads.append(future)

abc = list(string.ascii_lowercase)
n_processes = multiprocessing.cpu_count()
n_threads = sys.argv[1]
chunck_size = n_processes
groups = [abc[i:i+chunck_size] for i in range(0, len(abc), chunck_size)]

print('The list abc - {}'.format(abc))
print('Available logical N cores - {}'.format(n_processes))
print('The list will be divided in chuncks of {} elements'.format(n_processes))
print()

for i in range(0,len(groups)):
    print('Group {} - {}'.format(i+1,groups[i]))
print()

with concurrent.futures.ProcessPoolExecutor(max_workers=n_processes) as pexecutor:
    result_processes = []
    futures = [ pexecutor.submit(initiate_process, g) for g in groups ]
    for future in concurrent.futures.as_completed(futures):
        result_processes.append(future)
