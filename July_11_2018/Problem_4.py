# Problem 4
# Write a function which allows a user to compare and/or contrast two
# instances of your class "LongOrganism"

def OrganismCompare(organism1, organism2, comparison = 'full'):
    name1 = type(organism1).__name__
    name2 = type(organism2).__name__
    if name1 != 'LongOrganism' or name2 != 'LongOrganism':
        print('One of the two input organisms was not of class LongOrganism')
        return

    if comparison == 'lineage' or comparison == 'full':
        lines = ['K','P','C','O','F','G','S','N']
        lines_dict = {'K' : 'kingdom', 'P' : 'phylum',
                     'C' : 'class', 'O' : 'order',
                     'F' : 'family', 'G' : 'genus',
                     'S' : 'species', 'N' : 'name'}
        same = ''
        i = 0
        while i < len(lines):
            if getattr(organism1, lines[i]) != getattr(organism2, lines[i]):
                break
            i += 1
        if i == 0:
            print(organism1.N, 'and', organism2.N, 'belong to different kingdoms')
        elif i == len(lines):
            print(organism1.N, 'and', organism2.N, 'are the same')
        elif i == len(lines) - 1:
            print(organism1.N, 'and', organism2.N, 'are the same species with different names')
        else:
            print(organism1.N, 'and', organism2.N, 'share the same', end = ' ')
            for x in range(i):
                if x != i - 1:
                    print(lines_dict.get(lines[x]), end = ', ')
                else:
                    print('and ', lines_dict.get(lines[x]), '.', sep = '')

    if comparison == 'genetic' or comparison == 'full':
        if organism1.Ploidy == organism2.Ploidy:
            print(organism1.N, ' and ',
                  organism2.N, ' have the same ploidy: ',
                  organism1.Ploidy, 'n', sep = '')
        else:
            print(organism1.N, 'and', organism2.N, 'have different ploidy')
            print(organism1.N, ' has a ploidy of ',
                  organism1.Ploidy, 'n', sep = '')
            print(organism2.N, ' has a ploidy of ',
                  organism2.Ploidy, 'n', sep = '')
        if organism1.Size == organism2.Size:
            print(organism1.N, ' and ', organism2.N,
                  ' have the same genome size: ',
                  organism1.Size, 'Mb', sep = '')
        else:
            if organism1.Size > organism2.Size:
                print(organism1.N, ' has a genome size of ',
                      organism1.Size, 'Mb which is greater than ',
                      organism2.N, '\'s genome size of ', organism2.Size,
                      'Mb.', sep = '')
            else:
                print(organism2.N, ' has a genome size of ',
                      organism2.Size, 'Mb which is greater than ',
                      organism1.N, '\'s genome size of ', organism1.Size,
                      'Mb.', sep = '')
    if comparison == 'region' or comparison == 'full':
        if organism1.Region == organism2.Region:
            print(organism1.N, 'and', organism2.N, 'have the same region:',
                  organism1.Region)
        else:
            print(organism1.N, 'and', organism2.N,
                  ' have the different regions,', organism1.N,
                  'is from', organism1.Region, 'while', organism2.N,
                  'is from', organism2.Region)
    return

