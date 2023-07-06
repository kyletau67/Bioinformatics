#DNA Toolkit file
import collections
from structures import *


#Check sequence to make sure it is a DNA String
def validateSeq(seq):
    tempseq = seq.upper() #uppercase version of string input
    for nuc in tempseq:
        if nuc not in Nucleotides:
            return False
    return tempseq    
    
    
#Count nucleotide frequency
def countNucFrequency(seq):
    tempFreqDict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nuc in seq:
        tempFreqDict[nuc] += 1
    return tempFreqDict


def transcription(seq):
    """transcribing RNA from DNA, replacing thymine with uracil"""
    return seq.replace('T','U')

def reverse_complement(seq):
    """swapping complement pairs in DNA, then reversing the string"""
    #return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]
    mapping = str.maketrans('ATCG', 'TAGC')
    return seq.translate(mapping)[::-1]

def gc_content(seq):
    """GC Content in a DNA/RNA sequence"""
    return round(
        ((seq.count('C') + seq.count('G')) / len(seq) * 100),6)

def gc_content_subsec(seq, k=20):
    """GC Content in a DNA/RNA sub-sequence length k. k=20 by default"""
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i+k]
        res.append(gc_content(subseq))
    return res
