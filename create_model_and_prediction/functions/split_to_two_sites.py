import pandas as pd

def splitInto2(org):

    with file(org, 'r') as original:
        data = original.readlines()
    with file(org, 'w') as modified:
        modified.write(str(len(data)) + ' ' + str(len(data[0].split())-1) +  "\n" + ''.join(data))

    whole = pd.read_csv(org, delimiter = ' ', skiprows = [0], index_col = 0, header = None)

    p1I = [i for i in whole.index if not i.endswith('_m')]
    p1 = whole.loc[p1I,:]

    p2I = [i for i in whole.index if i.endswith('_m')]
    p2 = whole.loc[p2I,:]
    newI2 = [i[:-2] for i in p2I]
    p2.index = newI2

    part1 = org + '_p1'
    part2 = org + '_p2'

    p1.to_csv(part1, sep = ' ')
    p2.to_csv(part2, sep = ' ')

    with file(part1, 'r') as original:
        data = original.readlines()[1:]
    with file(part1, 'w') as modified:
        modified.write(str(len(data)) + ' ' + str(len(data[0].split())-1) +  "\n" + ''.join(data))

    with file(part2, 'r') as original:
        data = original.readlines()[1:]
    with file(part2, 'w') as modified:
        modified.write(str(len(data)) + ' ' + str(len(data[0].split())-1) +  "\n" + ''.join(data))



#splitInto2('../nmdsExp_mtv2/50_50/nmds_50_noW')
#splitInto2('../nmdsExp_mtv2/50_50/nmds_50_wW')
##splitInto2('../nmdsExp_mtv2/80_20/nmds_80_20_noW')
#splitInto2('../nmdsExp_mtv2/80_20/nmds_80_20_wW')
##splitInto2('../nmdsExp_mtv2/90_10/nmds_90_10_noW')
#splitInto2('../nmdsExp_mtv2/90_10/nmds_90_10_wW')

#splitInto2('../nmdsExp_mtv0/50_50/nmds_50_w_cat_1_W')
#splitInto2('../nmdsExp_mtv1/50_50/nmds_50_w_cat_1_W')

#splitInto2('../nmdsExp_mtv0/80_20/nmds_80_20_w_7AB_W')
#splitInto2('../nmdsExp_mtv0/90_10/nmds_90_10_w_7AB_W')
#splitInto2('../nmdsExp_mtv1/80_20/nmds_80_20_w_7AB_W')
#splitInto2('../nmdsExp_mtv1/90_10/nmds_90_10_w_7AB_W')
#splitInto2('../nmdsExp_mtv2/50_50/nmds_50_w_7AB_W')
#splitInto2('../nmdsExp_mtv2/80_20/nmds_80_20_w_7AB_W')
#splitInto2('../nmdsExp_mtv2/90_10/nmds_90_10_w_7AB_W')
#splitInto2('../nmdsExp_mtv4/50_50/nmds_50_noW')
#splitInto2('../nmdsExp_mtv3/50_50/nmds_50_w_7AB_W')
#splitInto2('../nmdsExp_mtv2/50_50/nmds_50_wW_halfDiags')
#splitInto2('../nmdsExp_mtv2/50_50/nmds_50_wW_qDiags')
#splitInto2('../nmdsExp_mtv2/50_50/nmds_50_wW_tenthDiags')
#
#splitInto2('../nmdsExp_mtv3/50_50/nmds_50_wW_halfDiags')
#splitInto2('../nmdsExp_mtv3/50_50/nmds_50_wW_qDiags')
#splitInto2('../nmdsExp_mtv3/50_50/nmds_50_wW_tenthDiags')
#
#splitInto2('../nmdsExp_mtv4/50_50/nmds_50_wW_halfDiags')
#splitInto2('../nmdsExp_mtv4/50_50/nmds_50_wW_qDiags')
#splitInto2('../nmdsExp_mtv4/50_50/nmds_50_wW_tenthDiags')

#splitInto2('../nmdsExp_mtv0/50_50/ver0_mtv0')
#splitInto2('../nmdsExp_mtv0/50_50/ver1_mtv0')
#splitInto2('../nmdsExp_mtv0/50_50/ver1_iter1')
#splitInto2('../nmdsExp_mtv0/50_50/ver2_iter1')
#splitInto2('../nmdsExp_mtv0/50_50/ver0_iter0_H')
#splitInto2('../nmdsExp_mtv0/50_50/new_method/ver0_iter10')
#splitInto2('../nmdsExp_mtv0/50_50/new_method/ver1_iter10')
#splitInto2('../nmdsExp_mtv0/50_50/new_method/ver2_iter10')
#splitInto2('../nmdsExp_mtv0/50_50/new_method/ver0_iter30')
#splitInto2('../nmdsExp_mtv0/50_50/new_method/ver1_iter30')
#splitInto2('../nmdsExp_mtv0/50_50/new_method/ver2_iter0')
#splitInto2('../nmdsExp_mtv0/50_50/new_method/ver0_iter0_H')
#splitInto2('../nmdsExp_mtv0/50_50/old_method/ver0_iter0')
#splitInto2('../nmdsExp_mtv0/50_50/old_method/ver0_iter10')
#splitInto2('../nmdsExp_mtv0/50_50/old_method/ver0_iter6')
#splitInto2('../nmdsExp_mtv0/50_50/new_method_JH/ver0_iter0')
#splitInto2('../nmdsExp_mtv0/50_50/new_method_JH/ver0_iter1')
#splitInto2('../nmdsExp_mtv0/50_50/new_method_JH/ver1_iter0')
#splitInto2('../nmdsExp_mtv0/50_50/new_method_JH/ver1_iter1')
#splitInto2('../nmdsExp_mtv0/50_50/new_method_JH/ver1_iter2')
splitInto2('../nmdsExp_mtv0/50_50/new_method_JH/ver2_iter0')
splitInto2('../nmdsExp_mtv0/50_50/new_method_JH/ver2_iter1')


#splitInto2('../nmdsExp_mtv0/50_50/nmds_50_w_7AB_W')
#splitInto2('../nmdsExp_mtv1/50_50/nmds_50_w_1AB_W')
#splitInto2('../nmdsExp_mtv1/50_50/nmds_50_w_3AB_W')
#splitInto2('../nmdsExp_mtv1/50_50/nmds_50_w_7AB_W')


#splitInto2('../nmdsExp_mtv0/50_50/nmds_50_noW')
#splitInto2('../nmdsExp_mtv0/80_20/nmds_80_20_noW')
#splitInto2('../nmdsExp_mtv0/90_10/nmds_90_10_noW')
#
#splitInto2('../nmdsExp_mtv1/50_50/nmds_50_noW')
#splitInto2('../nmdsExp_mtv1/80_20/nmds_80_20_noW')
#splitInto2('../nmdsExp_mtv1/90_10/nmds_90_10_noW')
#
#splitInto2('../nmdsExp_mtv2/50_50/nmds_50_noW')
#splitInto2('../nmdsExp_mtv2/80_20/nmds_80_20_noW')
#splitInto2('../nmdsExp_mtv2/90_10/nmds_90_10_noW')
