from bio_structs import *
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

    #Check sequence to make sure it is a DNA String
    def __validate(self):
        return set(Nucleotides).issuperset(self.seq)    
    
    def get_seq_biotype(self):
        """Returns sequence type"""
        return self.seq_type

    def get_seq_info(self):
        """Returns 4 strings. Full sequence info"""
        return f"[LABEL]: {self.label}\n[SEQUENCE]: {self.seq}\n[BIOTYPE]: {self.seq_type}\n[LENGTH]: {len(self.seq)}"
    
    def generate_rnd_seq(self, length=10, seq_type="DNA"):
        """Generate random DNA seq, provided the length"""
        seq = ''.join([random.choice(Nucleotides)
                     for x in range(length)])
        self.__init__(seq, seq_type, "Randomly generated sequence")