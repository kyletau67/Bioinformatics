class genomeToolkit:
    def __init__(self):
        print("Genome Toolkit initiated")

    def count_kmer(self, sequence, kmer):
        """Counts repeating k-mers in a sequence. Includes overlapping k-mers"""
        kmer_count = 0
        for position in range(len(sequence) - (len(kmer) -1)):
            if sequence[position:position + len(kmer)] == kmer:
                kmer_count += 1
        return kmer_count
    
    def find_most_frequent_kmers(self, sequence, k_len):
        """Finds most frequent k-mers of given length in DNA string"""
        kmer_frequencies = {}

        for i in range(len(sequence) - k_len + 1):
            kmer = sequence[i:i+k_len]
            if kmer in kmer_frequencies:
                kmer_frequencies[kmer] += 1
            else:
                kmer_frequencies[kmer] = 1
        
        return [kmer for kmer, frequency in kmer_frequencies.items() 
                if frequency == max(kmer_frequencies.values()) ]