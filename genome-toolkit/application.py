from genome_toolkit import genomeToolkit

gt = genomeToolkit()

seq = "AAAGAAAATTGA"
kmer = "AA"
k_len = 3

print(gt.count_kmer(seq,kmer))
print(f'Most frequent k-mer: {gt.find_most_frequent_kmers(seq, k_len)}')