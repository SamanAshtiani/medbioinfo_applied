#!/usr/bin/env python3

import os
import urllib.request

DIR = "/mnt/4tb/PconsC4_membrane/contact_vis/pdb_files"
url = "https://files.rcsb.org/download/"
id_handle = open("id_file.txt", 'r')
for l in id_handle:
    name = l.strip().split("_")[0]+".pdb"
    file_path = os.path.join(DIR, name)
    # print(name)
    # print(file_path)
    if not os.path.isfile(file_path):
        # print("not in path")
        # print(url+name)
        urllib.request.urlretrieve(url+name, file_path)
id_handle.close()