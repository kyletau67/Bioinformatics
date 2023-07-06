#==== Functions for GC Content reading from FASTA file
def readFile(filePath):
    """reading file and returning list of lines"""
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]
    

def gc_content(seq):
    """GC Content in a DNA/RNA sequence"""
    return round( ((seq.count('C') + seq.count('G')) / len(seq) * 100), 6)


#Calculate GC Content from FASTA formatted test file:

#==== Read data from FASTA file
FASTAFile = readFile('../test_data/rosalind_gc.txt')
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

RESULTDict = {key: gc_content(value) for (key,value) in FASTADict.items()}

print(RESULTDict)

#====Find max value
maxGCKey = max(RESULTDict, key=RESULTDict.get)

#====Collect results (max value of GC Content in file)
print(f'{maxGCKey[1:]}\n{RESULTDict[maxGCKey]}')