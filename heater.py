import multiprocessing
import os
import sys
import time
def count(start, end):
    for i in range(start, end+1):
    	print(i)

def main():
    num_processes = multiprocessing.cpu_count()*50
    process_size = 9999999
    
    processes = []
    for i in range(num_processes):
        start = i * process_size + 1
        end = start + process_size - 1
        p = multiprocessing.Process(target=count, args=(start, end))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
        
if __name__ == '__main__':
    main()
