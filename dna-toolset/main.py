#DNAToolset Testing 
from DNAToolkit import *
from utilities import colored
import random

#Create random DNA sequence and sort

randDNAstr = ''.join([random.choice(Nucleotides)
                        for nuc in range(50)])

DNAStr = validateSeq(randDNAstr)

print(f'\nSequence: {colored(DNAStr)}\n')
print(f'Sequence Length: {len(DNAStr)}\n')
print(f'Nucleotide Frequency: {countNucFrequency(DNAStr)}\n')
print(f'RNA Transcription: {transcription(DNAStr)}\n')

print(f"DNA String + Reverse Complement:\n5' {DNAStr} 3'")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {reverse_complement(DNAStr)} 5'\n")