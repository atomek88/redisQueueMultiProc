# redis worker for queue
import redis
from redis_queue import SimpleQueue

def worker():
    """ worker for completing task"""
    red = redis.Redis(host='localhost', port=6379)
    queue = SimpleQueue(red, 'sample')
    if queue.get_length() > 0:
        # dequeue serializes task and runs func
        queue.dequeue()
    else:
        print('No tasks in the queue')

if __name__ == '__main__':
    worker()
