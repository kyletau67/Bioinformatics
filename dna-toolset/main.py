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
print(f'Nucleotide Frequency: {countNucFrequency(DNAStr)}')
print(f'RNA Transcription: {transcription(DNAStr)}\n')

print(f"DNA String + Complement + Reverse Complement:\n5' {DNAStr} 3'")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {reverse_complement(DNAStr)[::-1]} 5' [Complement]")
print(f"5' {reverse_complement(DNAStr)} 3' [Reverse Complement]\n")

print(f'GC Content: {gc_content(DNAStr)}%\n')
print(
    f'GC Content in Subsection k=5: {gc_content_subsec(DNAStr, k=5)}\n')