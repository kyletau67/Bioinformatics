dna_str1 = "TTCGATCCATTG"
dna_str2 = "ATCAATCGATCG"

def h_d_loop(str1, str2):
    hd = 0
    for position in range(len(str1)):
        if str1[position] != str2[position]:
            hd += 1
    return hd

def h_d_set(str1, str2):
    nucleotide_set1 = set([(x, y) for x, y in enumerate(str1)])
    nucleotide_set2 = set([(x, y) for x, y in enumerate(str2)])
    return len(nucleotide_set1.difference(nucleotide_set2))

def h_d_zip(str1, str2):
    zipped_dna = zip(str1, str2)
    return len([(n1, n2) for n1, n2 in zipped_dna if n1 != n2])

print(h_d_loop(dna_str1, dna_str2))
print(h_d_set(dna_str1, dna_str2))
print(h_d_zip(dna_str1, dna_str2))
