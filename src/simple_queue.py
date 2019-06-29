# customize simple queue

import multiprocessing

def run():
    data = [
    'pride-and-prejudice.txt',
    'heart-of-darkness.txt',
    'frankenstein.txt',
    'dracula.txt'
    ]
    queue = multiprocessing.Queue()

    print('Enqueuing..')
    for book in data:
        print(book)
        queue.put(book)

    print('\nDequeuing..')
    while not queue.empty():
        print(queue.get())

if __name__ == '__main__':
    run()        
