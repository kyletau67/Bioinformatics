#==== Functions for reading from FASTA file
def readFile(filePath):
    """reading file and returning list of lines"""
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]
    
#==== Read data from FASTA file
FASTAFile = readFile('../test_data/rosalind_cons.txt')
#Dictionary for Labels + Data
FASTADict = {}
#String for holding current label
FASTALabel = ""

#==== Clean and Prep Data 
#Converting FASTA/List file data into a dictionary
for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

#print(FASTADict)


sequences = []
for value in FASTADict:
    sequences.append(FASTADict[value])
    n = len(FASTADict[value])


profile_dict = {
    "A": [0]*n, 
    "G": [0]*n,
    "C": [0]*n,
    "T": [0]*n
}

#print(profile_dict)
for seq in sequences:
    for position, nuc in enumerate(seq):
        profile_dict[nuc][position] += 1

#print(profile_dict)

maxes = []
for position in range(n):
    max_count = 0
    max_nuc = ""
    for nuc in ['A','G','C','T']:
        count = profile_dict[nuc][position]
        if count > max_count:
            max_count = count
            max_nuc = nuc
    maxes.append(max_nuc)

#print(maxes)
consensus = ''.join(maxes)
print(consensus)