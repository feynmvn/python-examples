## split_list_in_chunck_size.py - script to split a list into N chuncks

import sys
import string

abc = list(string.ascii_lowercase)
print('List - {}'.format(abc))

chunck_size = int(sys.argv[1])

print('List divide into chuck size of - {}'.format(str(chunck_size)))


chunks = [abc[i:i+chunck_size] for i in range(0, len(abc), chunck_size)]

print(chunks)


print('How chuck size calculated')

for i in range(0, len(abc), chunck_size):
    print('[{} - {}]'.format(i, i+chunck_size))
