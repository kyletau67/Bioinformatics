from Bio import Entrez, SeqIO
from Bio.SeqUtils import molecular_weight, gc_fraction
from collections import Counter

#working with covid dna to practice using Biopython

Entrez.email = "" 
handle = Entrez.efetch(db="nucleotide", id="MN908947", rettype="gb", retmode="text")
recs = list(SeqIO.parse(handle, 'gb'))
handle.close()

covid_dna = recs[0].seq
# molecular weight
print(molecular_weight(covid_dna))
print(gc_fraction(covid_dna))

count_nucleotides = {
    'A': covid_dna.count('A'),
    'T': covid_dna.count('T'),
    'C': covid_dna.count('C'),
    'G': covid_dna.count('G')
}
print(count_nucleotides)

#transcription
covid_mrna = covid_dna.transcribe()
print(covid_mrna)

#translation
covid_aa = covid_mrna.translate()
print(covid_aa)

#most common amino acids
common_amino = Counter(covid_aa)
common_amino.most_common(10)
del common_amino['*']
print(f"Covid-19's genome has {sum(common_amino.values())} amino acids")

proteins = covid_aa.split('*')
print(f'We have {len(proteins)} amino acid chains in the covid-19 genome')
#eliminate aa chains shorter than 20
for protein in proteins:
    if len(protein) < 20:
        proteins.remove(protein)
