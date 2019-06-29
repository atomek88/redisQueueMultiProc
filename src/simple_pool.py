# simple example using multiprocessing library
import time
import multiprocessing

from tasks import get_word_counts

PROCESSES = multiprocessing.cpu_count() -1
# different methods of asynchronous processing: choose between multi-arg, concurrency, blocking, ordered results
# examples map, map_async apply, apply_async
def run():
    """ run for counting word multiprocessing """
    print(f'Running with {PROCESSES} processes')
    start = time.time()
    with multiprocessing.Pool(PROCESSES) as p:
        p.map_async(get_word_counts, [
            'pride-and-prejudice.txt',
            'heart-of-darkness.txt',
            'frankenstein.txt',
            'dracula.txt'
        ])
        p.close() # tell pool sto stop accepting tasks
        p.join() # tells pool to exit after all tasks done
    print(f'Time taken = {time.time() - start:.10f}')

# if file invoked start run
if __name__ == '__main__':
    run()
