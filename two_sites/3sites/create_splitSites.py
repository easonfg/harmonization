import os

def splitSites(filename, out_dir, num_sites):

    for i in range(1, num_sites + 1):
        try:
            os.remove(out_dir + filename.split('/')[-1] + '_site' + str(i))
        except OSError:
            pass


    with open(filename, 'r') as f:
        s = f.readlines()

    #half_seq = []
    site1 =[]
    site2 =[]
    for each in s:
        chunks = each.strip().split('|')
        #new_d = [i + '_m' for i in chunks[0].split(',')]
        #chunk1 = chunks[0] + ',' + ','.join(new_d)
        #chunk1_half = chunks[0]

        seq = chunks[2].split()

        # first half and second half
        split_pt = len(seq)/num_sites

        seq_dict = {}
        for i in range(1, num_sites + 1):
            key = i
            value = [word + '_m' + str(i) for word in seq[(i - 1) * split_pt : (i)*split_pt]]
            seq_dict[key] = value

        new_seq = []
        for i in range(1, num_sites + 1):
            new_seq += seq_dict[i]


        final_diag_dict = {}
        for i in range(1, num_sites + 1):
            key = i
            value = [diag + '_m' + str(i) for diag in chunks[0].split(',')]
            final_diag_dict[i] = value


        final_seq = {}
        for i in range(1, num_sites + 1):
            key = i
            value = ','.join(final_diag_dict[i]) + '|' + chunks[1] + '|' + ' '.join(new_seq) + '|' + chunks[3]
            final_seq[key] = value
            #import pdb; pdb.set_trace()

        for i in range(1, num_sites + 1):
            #import pdb; pdb.set_trace()
            with open(out_dir + filename.split('/')[-1] + '_site' + str(i), 'a') as g:
                g.write((final_seq[i]) + '\n')
            g.close()



        #p1 = chunks[0] + '|' + chunks[1] +  '|' + ' '.join(new_seq) + '|' + chunks[3]
        #p2 = ','.join(chunk0_s2) + '|' + chunks[1] +  '|' + ' '.join(new_seq) + '|' + chunks[3]
        #new_p_half = chunk1_half + '|' + chunks[1] +  '|' + ' '.join(new_seq) + '|' + chunks[3]
        #twoSites_out.append(new_p)
        #twoSites_out_onesiteDiags.append(new_p_half)
        #site1.append(p1)
        #site2.append(p2)

        #half = chunks[0] + '|' + chunks[1] +  '|' + ' '.join(seq[:ind]) + '|' + chunks[3]
        #half_seq.append(half)

#    for i in range(1, num_sites + 1):
#        with open(out_dir + filename.split('/')[-1] + '_site' + str(i), 'w') as g:
#            g.write('\n'.join(site1))

    #with open(out_dir + filename.split('/')[-1] + '_site2', 'w') as g:
    #    g.write('\n'.join(site2))


#splitSites('../data/trainv_2')

#for i in range(0, 10):
#    splitSites('../data/test_' + str(i), 'half/')


#splitSites('../data/test_2', 'half/')


    #with open(filename.split('/')[-1] + '_twoSites', 'w') as g:
    #    g.write('\n'.join(twoSites_out))

    #with open(filename.split('/')[-1] + '_half', 'w') as g:
    #    g.write('\n'.join(half_seq))

    #with open(filename.split('/')[-1] + '_twoSites_onesiteDiags', 'w') as g:
    #    g.write('\n'.join(twoSites_out_onesiteDiags))



##create new vocabs for two sites with _m
def create_split_vocab(num_sites):
    #num_sites = 3
    for i in range(1, num_sites + 1):
        try:
            os.remove('vocab_site' + str(i))
        except OSError:
            pass


    with open('../../vocab', 'r') as h:
        s = h.readlines()


    all_words = []
    site_diags = {}


    #first line
    s0 = s[0].strip().split()

    for i in range(1, num_sites + 1):
        new_sent = [k + '_m' + str(i) for k in s0]
        with open('vocab_site' + str(i), 'a') as f:
            f.write(' '.join(new_sent) + '\n')
        f.close()
        all_words += new_sent

    #second line
    s1 = s[1].strip().split()

    for i in range(1, num_sites + 1):
        new_diag = [j + '_m' + str(i) for j in s1]
        with open('vocab_site' + str(i), 'a') as f:
            f.write(' '.join(new_diag))
        f.close()
        site_diags[i] = new_diag

    for i in range(1, num_sites + 1):
        with open('vocab_all' + str(i), 'w') as j:
            j.writelines(' '.join(all_words) + '\n')
            j.writelines(' '.join(site_diags[i]))


for i in range(0, 10):
    splitSites('../../data/test_' + str(i), '', 3)
