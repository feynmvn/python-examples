## split_list_into_n_cores.py
## divide a list into groups and send each group to a processes
## groups is set as the limit of available logical cores in the host
## the list will the abecedary
## output will depend on the available logical cores of your host

import multiprocessing
import concurrent.futures
import os
import string

def initiate_process(group):
    print('Process {} with group - {}'.format(os.getpid(), group))


abc = list(string.ascii_lowercase)
n_processes = multiprocessing.cpu_count()
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
    result = []
    futures = [ pexecutor.submit(initiate_process, g) for g in groups ]
    for future in concurrent.futures.as_completed(futures):
        result.append(future)
