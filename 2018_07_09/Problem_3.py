# Problem 3
# Demonstrate inheritance by importing your class "Organism" from problem 2.
# Use it to create a new class called "LongOrganism" which inherits "Organism"
# and modifies it by adding any other attributes that may be significant
# about an organism (ie ploidy, genome size, region).
# Write new methods which allow a user to see these values in informative ways.

from Problem_2 import Organism

print('This module allows you to create an organism class. It expects Kingdom\
 Phylum, Class, Order, Family, Genus, Species, Common Name, Region, Size, and \
Ploidy in that order')
      
class LongOrganism(Organism):
    def __init__(self,
                 K = '??',
                 P = '??',
                 C = '??',
                 O = '??',
                 F = '??',
                 G = '??',
                 S = '??',
                 N = '??',
                 Region = '??',
                 Size = '??',
                 Ploidy = '??'):
        self.Region = Region
        try:
            self.Ploidy = int(Ploidy)
        except ValueError:
            self.Ploidy = Ploidy
            print('Ploidy must be numeric')
        try:
            self.Size = int(Size)
        except ValueError:
            self.Size = Size
            print('Size must be numeric and is in Mb')
        Organism.__init__(self,K,P,C,O,F,G,S,N)

    def genome(self):
        print(self.N, '\'s genome description:\n',
              'Ploidy = ', self.Ploidy, 'n\n',
              'Genome Size = ', self.Size, ' Mb', sep = '')

    def region(self):
        print(self.N, '\'s region description:\n',
              'Region = ', self.Region, sep = '')

        
    def full(self):
        Organism.full(self)
        self.genome()
        self.region()

    def description(self):
        Organism.description(self)
        print('Genome information can be acccessed using\n',
              'object.genome(), object.Ploidy and object.Size\n',
              'Region information can be acccessed using\n',
              'object.region() and object.Region', sep = '')

