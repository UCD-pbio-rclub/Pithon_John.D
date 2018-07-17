# Problem 2
# Write a function that reports the number of sequences in a fastq file
import glob

def fastqCount():
    files = glob.glob('*')
    filename = input('Enter the name of the fastq file if unsure, enter \'ls\' \
for current directory listings: ')
    if filename == 'ls':
        for i in files:
            print(i)
        filename = input('Enter the name of the fastq file: ')
    if filename in files:
        with open(filename) as f:
            for i, l in enumerate(f):
                pass
            print('There are', (i+1)//4, 'fastq records in', filename)
    else:
        print('File could not be found')
