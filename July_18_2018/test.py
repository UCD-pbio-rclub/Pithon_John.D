import string
import re
with open('sample.fa', 'r') as f:
    count = 0
    line = f.readline()
    while line != '':
        if line.startswith('>'):
            print(line, end = '')
            count += 1
        line = f.readline()
    print('There are', count, 'fasta records in the file')

with open('SP1.fq', 'r') as o:
    with open('SP1.fa', 'w') as n:
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
    print('Fasta Created')


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return (i + 1) // 4

