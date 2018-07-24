# Problem 1
# Write a function that reports the number of sequences in a fasta file

import string
import re
import glob

def fastaCount(filename):
    with open(filename, 'r') as f:
        count = 0
        line = f.readline()
        while line != '':
            if line.startswith('>'):
                count += 1
            line = f.readline()
    return count

