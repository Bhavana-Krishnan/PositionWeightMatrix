import math
import numpy as np
import random
from Bio import motifs
from Bio.Seq import Seq

# input file with list of sequences
file1 = open(
    'C:\\Users\\Bhavana\\Downloads\\Python_Code-main\\Python_Code-main\\PositionWeightMatrix\\exampleseqs.txt', 'r')
x = file1.readlines()
p = [i.replace('\n', '') for i in x]
new = []
for i in range(len(p)):
    new.append(Seq(p[i].upper()))  # appending sequences to a list

m = motifs.create(new[:])
# print(m.counts)
pwm = m.counts.normalize(
    # Pseudocounts for the probability of occurrence of all the nucleotides is considered equal, therefore, each of them is equal to 0.25
    # Amount added to the number of observed cases in order to change the expected probability of the PPM
    pseudocounts={'A': 0, 'C': 0, 'G': 0, 'T': 0})
# print(pwm)
# log odds matrix or the position weight matrix
pssm = pwm.log_odds()
print(pssm)

# Below, we calculate the score for each sequence based on the length of the sequence
val = []
# print(new)
for i in new[:]:
    a, b, c, d, e, f, g, h, i = str(i)
    result = pssm[a, 0] + pssm[b, 1] + pssm[c, 2]+pssm[d, 3] + \
        pssm[e, 4] + pssm[f, 5] + pssm[g, 6] + pssm[h, 7] + pssm[i, 8]
    val.append([result])
# print(val)


def score_cal(seq):
    a, b, c, d, e, f, g, h, i = seq
    result = pssm[a, 0] + pssm[b, 1] + pssm[c, 2]+pssm[d, 3] + \
        pssm[e, 4] + pssm[f, 5] + pssm[g, 6] + pssm[h, 7] + pssm[i, 8]
    return result


file1 = open('C:\\Users\\Bhavana\\Downloads\\Python_Code-main\\Python_Code-main\\PositionWeightMatrix\\exampleseqsscore.txt', "w")
for i in new[:]:
    file1.writelines("\n{}\t{}".format(i, str(score_cal(str(i)))))
file1.close()
