# Problem 5
# Create an instance of your 'Organism' class from last week.
# Demonstrate pickling it to a file, and loading it from the file.
# Note: when opening the file you may need to add the 'b' option

import sys, pickle
sys.path.append('/home/pi/Documents/Pithon_Directories/Pithon_JohnD')
from July_11_2018.Problem_2 import Organism

a = Organism(G = 'Homo', S = 'sapien', N = 'John')

a.short()

with open('organism.pickle', 'wb') as f:
    pickle.dump(a, f)

with open('organism.pickle', 'rb') as n:
    b = pickle.load(n)

b.short()
