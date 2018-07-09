# Problem 2
# 2. Write a class called "Organism". Have the class initialize with the
# organism's complete taxonomic lineage (KPCOFGS) and common name.
# Write methods which allow a user to see these values in informative ways.

class Organism:
    def __init__(self,
                 K = '??',
                 P = '??',
                 C = '??',
                 O = '??',
                 F = '??',
                 G = '??',
                 S = '??',
                 N = '??'):
        self.K = K
        self.P = P
        self.C = C
        self.O = O
        self.F = F
        self.G = G
        self.S = S
        self.N = N
        for i in self.__dict__.keys():
            if self.__dict__[i] == '??':
                 print('No value provided for: ', i)

    def description(self):
        print('Access the lineage values of the organism using the first \
letters in\nKingdom, Phylum, Class, Order, Family, Genus, Species, and Name \
(KPCOFGSN)\nLonger descriptions can also be accessed.\n\
Examples: object.K, object.full(), and object.short()')

    def full(self):
        print(self.N, '\'s full name description:\n',
              'Kingdom = ', self.K, "\n",
              'Phylum = ', self.P, "\n",
              'Class = ', self.C, "\n",
              'Order = ', self.O, "\n",
              'Family = ', self.F, "\n",
              'Genus = ', self.G, "\n",
              'Species = ', self.S, sep = "")

    def short(self):
        print(self.N, '\'s short name description:\n',
              self.G, ' ', self.S.lower(), sep = "")
