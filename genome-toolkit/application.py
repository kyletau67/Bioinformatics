from genome_toolkit import genomeToolkit

gt = genomeToolkit()

seq = "AAAGAAAATTGA"
kmer = "AAA"

print(gt.count_kmer(seq,kmer))