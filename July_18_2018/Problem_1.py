# Problem 1
# Write a function that reports the number of sequences in a fasta file

import string
import re
import glob

def fastaCount():
    files = glob.glob('*')
    filename = input('Enter the name of the fasta file if unsure, enter ls for \
current directory listings: ')
    if filename == 'ls':
        for i in files:
            print(i)
        filename = input('Enter the name of the fasta file: ')
    if filename in files:
        with open(filename, 'r') as f:
            count = 0
            line = f.readline()
            while line != '':
                if line.startswith('>'):
                    count += 1
                line = f.readline()
            print('There are', count, 'fasta records in', filename)
    else:
        print('File could not be found')

            

