#!/usr/bin/env python3

"""
import re

regex = re.compile("[\.\- ]+")
infilename = "pdbtm_alpha_nr.fasta"
outfilename = "pdbtm_alpha_nr_nospace.fasta"
with open(infilename, 'r') as in_handle, open(outfilename, 'w') as out_handle:
    for l in in_handle:
        print(l)
        # l = l.strip()
        #out_handle.write(regex.sub("", l))

"""

from Bio import SeqIO

w_handle = open("pdbtm_alpha_redundant_nospace_nonewline.fasta", 'w')

with open("pdbtm_alpha_redundant.seq", 'rU') as r_handle:
    for record in SeqIO.parse(r_handle, "fasta"):
        seq = str(record.seq)
        w_handle.write('>'+record.id+"\n"+seq+"\n")

w_handle.close()