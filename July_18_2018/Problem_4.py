# Problem 4
# Write a function that converts a fastq file to a fasta file

import glob
import string
import re
from os.path import splitext

def fastqConvert():
    files = glob.glob('*')
    fq = input('Enter the name of the fastq file if unsure, enter \'ls\' \
for current directory listings: ')
    if fq == 'ls':
        for i in files:
            print(i)
        fq = input('Enter the name of the fastq file: ')
    if fq in files:
        fa = splitext(fq)[0] + '.fa'
        with open(fq, 'r') as o:
            with open(fa, 'w') as n:
                line = o.readline()
                while line != '':
                    if line.startswith('@'):
                        line = re.sub('^@', '>', line)
                        n.write(line)
                        line = o.readline()
                        n.write(line)
                        line = o.readline()
                        line = o.readline()
                    line = o.readline()
        print(fa, 'has been created')
    else:
        print('File could not be found')
