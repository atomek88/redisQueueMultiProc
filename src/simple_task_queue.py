# simple task queue with timing

import time
import multiprocessing

from tasks import get_word_counts

PROCESSES = multiprocessing.cpu_count() -1
NUMBER_OF_TASKS = 10

def process_tasks(task_queue_todo, tasks_queue_complete):
    """ process a task from queue, word counts, return True """
    while not task_queue_todo.empty():
        book = task_queue_todo.get()
        get_word_counts(book)
        tasks_queue_complete.put(book)
    return True

def add_tasks(task_queue, number_of_tasks):
    """ add all tasks to a multiprocessing queue"""
    for num in range(number_of_tasks):
        task_queue.put('pride-and-prejudice.txt')
        task_queue.put('heart-of-darkness.txt')
        task_queue.put('frankenstein.txt')
        task_queue.put('dracula.txt')
    return task_queue

def run():
    empty_task_queue = multiprocessing.Queue()
    full_task_queue = add_tasks(empty_task_queue, NUMBER_OF_TASKS)
    completed_tasks_queue = multiprocessing.Queue()
    processes = []
    print(f'Running with {PROCESSES} processes')
    start = time.time()
    for n in range(PROCESSES):
        p = multiprocessing.Process(
            target = process_tasks, args=(full_task_queue,completed_tasks_queue))
        processes.append(p)
        p.start()


    for p in processes:
        p.join()
        #where to add to completed tasks queue
    print(f'Books completed : {completed_tasks_queue.empty()}')
    print(f'Time taken = { time.time() - start:.10f}')

if __name__ == "__main__":
    run()
