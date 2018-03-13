#!/usr/bin/env python3

import os


def more_than_3tm_helices(list_dir):

    # final_list = []
    dir_list = os.listdir(list_dir)
    for f in dir_list:
        with open(os.path.join(list_dir, f), 'r') as f_handle:
            for line in f_handle:
                line = line.strip()
                # print(line)
                if line.startswith("<CHAIN"):
                    # print(line)
                    splitted_line = line.split('"')
                    if int(splitted_line[3]) > 3:
                        # print(splitted_line[1])
                        chain_id = splitted_line[1]
                        pdb_id = f.strip().split('.')[0]
                        print(pdb_id)
                        final_id = ">"+str(pdb_id)+"_"+chain_id
                        # int(final_id)
                        # final_list.append(final_id)
                        # return final_id
                        print(final_id)
                        with open("final_pdbtm_list.txt", 'a') as list_handle:
                            list_handle.write(final_id+'\n')
    # print(final_list)
    # return final_list

if __name__ == "__main__":
    more_than_3tm_helices("/mnt/4tb/PconsC4_membrane/xml_pdbtm_morethan3_helices/")
