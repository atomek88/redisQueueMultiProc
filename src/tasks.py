# part of python asynchronous task queue - Tomasz Michalik

import os
import sys
import json
import time
import uuid
import collections

from nltk.corpus import stopwords

COMMON_WORDS = set(stopwords.words('english'))
DATA_DIRECTORY = os.path.join(os.path.dirname(__file__), 'data')
OUTPUT_DIRECTORY = os.path.join(os.path.dirname(__file__), 'output')


def save_file(filename, data):
    """ save file to output, provide random gen hex string as uuid"""
    random_str = uuid.uuid4().hex
    outfile = f'{filename}_{random_str}.txt'
    with open(os.path.join(OUTPUT_DIRECTORY, outfile), 'w') as outfile:
        outfile.write(data)

# get word counts
def get_word_counts(filename):
    """get word counts of provided filename"""
    wordcount = collections.Counter()
    with open(os.path.join(DATA_DIRECTORY, filename), 'r') as f:
        for line in f:
            wordcount.update(line.split()) #counter will update words based on N seen
    for word in set(COMMON_WORDS):
        del wordcount[word] # this deletes common words
    save_file(filename, json.dumps(dict(wordcount.most_common(20))))
    # simulate long running task
    time.sleep(2)
    proc = os.getpid()
    print(f'Processed {filename} with process id: {proc}')

#main driver
if __name__ == '__main__':
    get_word_counts(sys.argv[1])
