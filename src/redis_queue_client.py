# redis client queue

import redis

from redis_queue import SimpleQueue
from tasks import get_word_counts

NUMBER_OF_TASKS = 10

if __name__ == '__main__':
    red = redis.Redis(host='localhost', port=6379)
    queue = SimpleQueue(red, 'sample')
    count = 0
    for n in range(NUMBER_OF_TASKS):
        queue.enqueue('pride-and-prejudice.txt')
        queue.enqueue('heart-of-darkness.txt')
        queue.enqueue('frankenstein.txt')
        queue.enqueue('dracula.txt')
        count+= 4
    print(f'Enqueued {count} tasks')
