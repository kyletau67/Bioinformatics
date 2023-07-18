from bio_structs import NUCLEOTIDE_BASE, DNA_Codons, RNA_Codons 
from collections import Counter
import random

class bio_seq:
    """DNA sequence class. Default value: ATCG, DNA, No label"""

    def __init__(self, seq="ATCG", seq_type="DNA", label='No Label'):
        """Seq initialization, validation"""
        self.seq = seq.upper()
        self.label = label
        self.seq_type = seq_type
        self.is_valid = self.__validate()
        assert self.is_valid, f"Provided data does not seem to be a correct {self.seq_type} sequence"

    def __validate(self):
        """Check sequence to make sure it is a DNA String"""
        return set(NUCLEOTIDE_BASE[self.seq_type]).issuperset(self.seq)    
    
    def get_seq_biotype(self):
        """Returns sequence type"""
        return self.seq_type

    def get_seq_info(self):
        """Returns 4 strings. Full sequence info"""
        return f"[LABEL]: {self.label}\n[SEQUENCE]: {self.seq}\n[BIOTYPE]: {self.seq_type}\n[LENGTH]: {len(self.seq)}"
    
    def generate_rnd_seq(self, length=10, seq_type="DNA"):
        """Generate random DNA seq, provided the length"""
        seq = ''.join([random.choice(NUCLEOTIDE_BASE[seq_type])
                     for x in range(length)])
        self.__init__(seq, seq_type, "Randomly generated sequence")

    def nucleotide_frequency(self):
        """Count nucleotides in a given sequence. Return dictionary"""
        return dict(Counter(self.seq))
    
    def transcription(self):
        """transcribing RNA from DNA, replacing thymine with uracil"""
        if self.seq_type == "DNA":
            return self.seq.replace('T','U')
        return "Not a DNA Sequence"
    
    def reverse_complement(self):
        """swapping complement pairs in DNA, then reversing the string"""
        if self.seq_type == "DNA":
            mapping = str.maketrans('ATCG', 'TAGC')
        else:
            mapping = str.maketrans('AUCG', 'UAGC')
        return self.seq.translate(mapping)[::-1]
    
    def gc_content(self):
        """GC Content in a DNA/RNA sequence"""
        return round(
            ((self.seq.count('C') + self.seq.count('G')) / len(self.seq) * 100),6)

    def gc_content_subsec(self, k=20):
        """GC Content in a DNA/RNA sub-sequence length k. k=20 by default"""
        res = []
        for i in range(0, len(self.seq) - k + 1, k):
            subseq = self.seq[i:i+k]
            res.append(round(
                ((subseq.count('C') + subseq.count('G')) / len(subseq) * 100),6))
        return res
    
    def translate_seq(self, init_pos=0):
        """Translates DNA seq into amino acid seq"""
        if self.seq_type == "DNA":
            return [DNA_Codons[self.seq[pos:pos+3]] for pos in range(init_pos, len(self.seq) - 2, 3)]
        elif self.seq_type == "RNA":
            return [RNA_Codons[self.seq[pos:pos+3]] for pos in range(init_pos, len(self.seq) - 2, 3)]

    def codon_usage(self, aminoacid):
        """Provides frequency of each codon encoding a given amino acid in DNA seq"""
        tmpList = []
        if self.seq_type == "DNA":
            for i in range(0, len(self.seq) - 2, 3):
                if DNA_Codons[self.seq[i:i+3]] == aminoacid:
                    tmpList.append(self.seq[i:i+3])

        if self.seq_type == "RNA":
            for i in range(0, len(self.seq) - 2, 3):
                if RNA_Codons[self.seq[i:i+3]] == aminoacid:
                    tmpList.append(self.seq[i:i+3])
                    
        freqDict = dict(Counter(tmpList))
        totalWeight = sum(freqDict.values())
        for seq in freqDict:
            freqDict[seq] = round(freqDict[seq] / totalWeight, 2)
        return freqDict
   
    def gen_reading_frames(self):
        """Generate six reading frames of DNA seq, including reverse complement"""
        frames = []
        frames.append(self.translate_seq(0))
        frames.append(self.translate_seq(1))
        frames.append(self.translate_seq(2))
        tmp_seq = bio_seq(self.reverse_complement(), self.seq_type)
        frames.append(tmp_seq.translate_seq(0))
        frames.append(tmp_seq.translate_seq(1))
        frames.append(tmp_seq.translate_seq(2))  
        del tmp_seq      
        return frames
    
    def proteins_from_rf(self,aa_seq):
        """Compute all possible proteins in an aminoacid seq and return a list of possible proteins"""
        current_prot = []
        proteins = []
        for aa in aa_seq:
            if aa == "_":
                #stop codon detected - end of amino acid seq
                if current_prot:
                    for p in current_prot:
                        proteins.append(p)
                    current_prot = []
            else:
                #start accumulating amino acids if M is detected (start codon)
                if aa == "M":
                    current_prot.append("")
                for i in range(len(current_prot)):
                    current_prot[i] += aa
        return proteins
    
    def all_proteins_from_orfs(self, startReadPos=0, endReadPos=0, ordered=False):
        """Compute all possible proteins for all open reading frames"""
        """Protein Search DB: https://wwww.ncbi.nlm.nih.gov/nuccore/NM_001185097.2"""
        """API can be used to pull protein info"""
        if endReadPos > startReadPos:
            tmp_seq = bio_seq(self.seq[startRead: endRead], self.seq_type)
            rfs = tmp_seq.gen_reading_frames()
        else:
            rfs = self.gen_reading_frames()

        res = []
        for rf in rfs:
            proteins = self.proteins_from_rf(rf)
            for p in proteins:
                res.append(p)

        if ordered:
            return sorted(res, key = len, reverse = True)
        return res