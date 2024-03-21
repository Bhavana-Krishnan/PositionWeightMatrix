# Calculation of Position frequency matrix for a set of aligned sequences of uniform length using Object Oriented Programming
import itertools
import numpy as np
import pandas as pd


class PosWeightMatrix():
    row_names = ['A', 'T', 'G', 'C']

    def __init__(self, arrayofseqs):
        self.arrayofseqs = arrayofseqs

    def getPFM(self):
        '''Calculates the frequency of occurrence of a 
        particular nucleotide in the same position 
        given a set ofsequences'''
        PFM = []
        A, T, G, C = [], [], [], []
        for j in range(len(self.arrayofseqs[0])):
            A.append([i[j] for i in self.arrayofseqs].count('A'))
            T.append([i[j] for i in self.arrayofseqs].count('T'))
            G.append([i[j] for i in self.arrayofseqs].count('G'))
            C.append([i[j] for i in self.arrayofseqs].count('C'))
        PFM = np.array([A, T, G, C])
        return PFM

    def getPPM(self):
        '''Get Position Probability Matrix, Obtained by
        dividing the PFM with the total number of 
        sequences in the array'''
        PFM = self.getPFM()
        PPM = PFM / len(self.arrayofseqs)
        PPM_df = pd.DataFrame(data=PPM, index=PosFreqMatrix.row_names, columns=[
                              i for i in range(1, len(self.arrayofseqs[0])+1)])
        return PPM_df

    def getPWM(self, b=None):#b is backgrounf probability,considered uniform for all nucs when b is None
        '''Get Position Weight Matrix using the below method
        By taking the logarithm base 2 values of the PPM on 
        division with the base probability of nuc=0.25 and 
        for amino acid as 0.05, the PWM can be achieved'''
        PPM = self.getPPM()
        if b == None:
            PWM_b = PPM / 0.25
        else:

        PWM = np.log2(PWM_b)
        PWM_df = pd.DataFrame(data=PWM, index=PosFreqMatrix.row_names, columns=[
                              i for i in range(1, len(self.arrayofseqs[0])+1)])
        return PWM_df

#Creating Inputs
# Sample 1
# You can comment out the below region if you want to give your own set of sequences and assign it in this line to seqs
seqs = ['GAGGTAAAC', 'TCCGTAAGT', 'CAGGTTGGA', 'ACAGTCAGT', 'TAGGTCATT',
        'TAGGTACTG', 'ATGGTAACT', 'CAGGTATAC', 'TGTGTGAGT', 'AAGGTAAGT']

# Sample 2 - Generating a library of strings with 9 nucleotides

'''
seqs = []
for v in itertools.product(['A', 'T', 'G', 'C'], repeat=8):
    seqs.append("".join(list(map(str, v))))'''

# Creating Object Instance
seqsPFM = PosWeightMatrix(seqs)
print(seqsPFM.getPFM())
print(seqsPFM.getPPM())
print(seqsPFM.getPWM())