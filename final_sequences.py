#!/usr/bin/env python3

import re

id_handle = open("terminal_final_list.txt", 'r')
seq_handle = open("pdbtm_alpha_redundant_nospace_nonewline.txt", 'r')
# seq_handle = open("pdbtm_alpha_redundant_nospace_nonewline.txt", 'r').readlines()     #saved as list -> no need to close
# use above line instead of seek
cid=0
for id in id_handle:
    #id = re.sub("\W", "", id)
    id_n = id.strip("\n")
    #print(id_n)
    id_n_s = id_n.strip()
    #
    # print('id',repr(id_n_s))
    seq_handle.seek(0)
    for line in seq_handle:
        # line = re.sub("\W", "", line)
        line_n = line.strip("\n")
        line_n_s = line_n.strip()
        #print('seq',repr(line_n_s))
        #print(repr(line_n_s[0]))
        if id_n_s == line_n_s:
            cid+=1
            # print(id_n_s)
            with open("final_sequences.fasta", 'a') as final_handle:
                final_handle.write(id_n_s+"\n")
                seq = seq_handle.readline().strip()
                final_handle.write(seq+"\n")
print(cid)
id_handle.close()
seq_handle.close()

