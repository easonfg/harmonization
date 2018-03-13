import re

#def split(in_dir, infile, ratio_1, ratio_2):

def create_imbalanced(in_dir, infile, diag, big, small):
    #in_dir = '../nmdsExp_mtv2/'; infile = 'trainv_2'
    with open(in_dir + infile) as f:
        #for s in enumerate(f):
        s = [s.rstrip() for i, s in enumerate(f)]
    f.close()

    cohort = []
    rest = []

    for each in s:
        all_words = []
        chunks = each.strip().split('|')
        for word in chunks:
            all_words += re.split(' |,', word)
        #import pdb; pdb.set_trace()
        if diag in all_words:
            cohort.append(each)
        else:
            rest.append(each)

    split_pt = int(len(cohort)*big)
    rest_split_pt = int(len(cohort)*small)

    #big_site = cohort[:split_pt] + rest[:rest_split_pt]
    #small_site = cohort[split_pt:] + rest[rest_split_pt:rest_split_pt+split_pt]

    big_site = cohort[:split_pt] + rest
    small_site = cohort[split_pt:] + rest

    with open('../nmdsExp_mtv2/imbalanced/big_site'+'_'+diag, 'w') as g:
        g.write('\n'.join(big_site))


    with open('../nmdsExp_mtv2/imbalanced/small_site'+'_'+diag, 'w') as h:
        h.write('\n'.join(small_site))


create_imbalanced('../nmdsExp_mtv2/', 'trainv_2', 'd_305', 0.99, 0.01)
