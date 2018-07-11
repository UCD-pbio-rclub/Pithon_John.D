# Problem 5
# Import your class and function from problems 3 and 4.
# Demonstrate using them together

from Problem_3 import LongOrganism
from Problem_4 import OrganismCompare

plant1 = ('Plantae', 'Tracheophyta', 'Magnoliopsida', 'Brassicales',
         'Brassicaceae', 'Brassica', 'Napus', 'DaAe', 'Asia', 1120, 4)

plant2 = ('Plantae', 'Tracheophyta', 'Magnoliopsida', 'Brassicales',
         'Brassicaceae', 'Brassica', 'Napus', 'DaOl', 'Asia', 1120, 4)

plant3 = ('Plantae', 'Tracheophyta', 'Magnoliopsida', 'Brassicales',
         'Brassicaceae', 'Brassica', 'Rapa', 'Rapa', 'Asia', 485, 2)

A = LongOrganism(*plant1)
B = LongOrganism(*plant2)
C = LongOrganism(*plant3)

print()

print('Looking at organism A')
A.full()

print()

print('Looking at organism C')
C.full()

print()

print('Compare all between A and C')
OrganismCompare(A, C)

print()

print('Compare lineages of A and B')
OrganismCompare(A, B, 'lineage')

print()

print('Compare genetics of B and C')
OrganismCompare(B, C, 'genetic')
