#!/usr/bin/env python3

import sys
import os.path

in_list = sys.argv[1]

print(in_list, "contains fasta sequences")
with open(in_list, 'r') as inlist_handle:
    for l in inlist_handle:

        if l.startswith(">"):
            f_name = l.lstrip(">").strip()+".fasta"
            header = l.strip()
            seq = inlist_handle.readline().strip()
            with open(os.path.join("/mnt/4tb/PconsC4_membrane/hhblits/fasta_files/", f_name), 'w') as extracted_f_handle:
                extracted_f_handle.write(header+"\n")
                extracted_f_handle.write(seq+"\n")
        id = l.strip().strip(">")
        with open("id_file.txt", 'a') as id_handle:
            id_handle.write(id+"\n")
