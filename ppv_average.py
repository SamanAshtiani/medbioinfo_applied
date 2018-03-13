#!/usr/bin/env python3

import sys
import statistics
import pandas as pd

in_list = sys.argv[1]


def av_ppv(in_l):
    list_handle = open(in_list, 'r')
    ppv_sum = 0
    ppv_counter = 0
    ppv_list = []
    g_t_half = []
    for l in list_handle:
        #print(repr(l))
        l = l.strip()
        ppv_f_handle = open(l, 'r')
        ppv_line = ppv_f_handle.readline()
        #print(ppv_line)
        ppv = float(ppv_line.split(" ")[2])
        # print(ppv)
        ppv_sum += float(ppv)
        ppv_counter += 1
        # print(ppv_counter)
        ppv_list.append(ppv)
        if ppv >= 0.5:
            g_t_half.append(ppv)

        ppv_f_handle.close()

    list_handle.close()
    ppv_average = ppv_sum / ppv_counter
    print(ppv_average)
    std_deviation = statistics.pstdev(ppv_list)
    print("stdev:", std_deviation)
    max_ppv = max(ppv_list)
    print("max ppv", max_ppv)
    g_t = len(g_t_half)
    print("number of ppv's greater than 0.5: ", g_t)
    raw_data = { "DCA method" : ["plmDCA", "gDCA"],
                            "Mean_PPV" : [0.2027304003323601, 0.19631897686332136],
                           "stdev" : [0.13578235970558689, 0.1346329161438511],
                           "max ppv" : [0.560544217687, 0.537124802528],
                           "ppv > 0.5" : [26, 29]}
    ppv_df = pd.DataFrame(raw_data, columns= ["DCA method", "Mean", "stdev", "max ppv", "ppv > 0.5"])
    print(ppv_df)
    print(pd.crosstab(ppv_df.Mean_PPV, margins=True))


if __name__ == "__main__":
    av_ppv(in_list)


"""
ppv_plm_list.txt 
0.2027304003323601
stdev: 0.13578235970558689
max ppv 0.560544217687
number of ppv's greater than 0.4:  26


ppv_gdca_list.txt 
0.19631897686332136
stdev: 0.1346329161438511
max ppv 0.537124802528
number of ppv's greater than 0.5:  29

"""