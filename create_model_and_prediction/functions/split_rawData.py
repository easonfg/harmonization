import os

def split(in_dir, infile, ratio_1, ratio_2):
    with open(in_dir + infile) as f:
        #for s in enumerate(f):
        m100 = [s.rstrip() for i, s in enumerate(f)]
    f.close()

    dir = in_dir + str(ratio_1) + '_' + str(ratio_2) + '/'

    if not os.path.exists(dir):
        os.makedirs(dir)


    m100_1 = m100[0:len(m100) * ratio_1/100]
    m100_2 = m100[len(m100) * ratio_1/100:]

    split_1 = dir + infile + '_' + str(ratio_1) + '_1'
    split_2 = dir + infile + '_' + str(ratio_2) + '_2'

    with open(split_1, 'w') as f:
        f.write('\n'.join(m100_1))
    f.close()

    with open(split_2, 'w') as f:
        f.write('\n'.join(m100_2))
    f.close()

    return dir, split_1, split_2

#split('../nmdsExp_mtv0/', 'trainv_0', 50, 50)
#split('../nmdsExp_mtv0/', 'trainv_0', 80, 20)
#split('../nmdsExp_mtv0/', 'trainv_0', 90, 10)

#split('../nmdsExp_mtv2/', 'trainv_2', 95, )
#split('../nmdsExp_mtv2/', 'trainv_2', 99, 1)
