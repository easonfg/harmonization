import os

def split(in_dir, infile, num_sites):
    with open(in_dir + infile) as f:
        #for s in enumerate(f):
        m100 = [s.rstrip() for i, s in enumerate(f)]
        #m100 = s.rstrip()
    f.close()

    #out_dir = in_dir + str(ratio_1) + '_' + str(ratio_2) + '/'

    #if not os.path.exists(out_dir):
    #    os.makedirs(out_dir)
    split_pt = len(m100)/num_sites

    site_dic = {}
    for i in range(1, num_sites + 1):
        key = str(i)
        value = m100[(i - 1) * split_pt : (i)*split_pt]
        site_dic[key] = value


    for k, v in site_dic.iteritems():
        with open(infile + '_' + k, 'w') as f:
            f.write('\n'.join(v))
        f.close()

for i in range(0, 10):
    split('../', 'trainv_' + str(i), 3)
