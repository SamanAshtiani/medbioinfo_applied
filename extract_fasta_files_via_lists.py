#!usr/bin/evn python3

import sys
import os.path

in_f = sys.argv[1]

id_seq_dict = {}
with open(in_f, 'r') as in_f_handle:
    for l in in_f_handle:
        l = l.strip()
        if l.startswith(">"):
            if l in id_seq_dict:
                continue
            else:
                id_seq_dict[l] = None


