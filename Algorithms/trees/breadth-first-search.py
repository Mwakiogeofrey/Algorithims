"""
The logic will be as follows:
1. Visit every node in the tree
2. If the node is a file, print out its name
3. If the node is a folder, add it to a queue of folders to search for files

"""

from os import listdir
from os.path import isfile, join
from collections import deque

def printnames(start_dir):
    search_queue = deque()
    search_queue.append(start_dir)
    while search_queue:
        dir = search_queue.popleft()
        for file in sorted(listdir(dir)):
            fullpath = join(dir, file)
            if isfile(fullpath):
                print(file)
            else:
                search_queue.append(fullpath)
                printnames("pics")