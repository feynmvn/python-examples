import multiprocessing
import os

print('(multiprocessing) Total of logical cores (CPUs) available in your host - {}'.format(multiprocessing.cpu_count()))
print('(os) Total of logical cores (CPUs) available in your host - {}'.format(multiprocessing.cpu_count()))
