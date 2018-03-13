# this will preprocess the trained data by adding site specific suffices to the end of each words, essentially simulating the fact that each hospital uses different codes. this will also combine all the words from three sites to make a combined file


import pandas as pd

def comb(in_dir, rep, num_sites):
    #import pdb; pdb.set_trace()

    models = {}
    for i in range(1, num_sites + 1):
        models[i] = pd.read_csv(in_dir + 'trainv_' + rep + '_' + str(i) + '_trained', delimiter = ' ', skiprows = [0], index_col = 0, header = None)
        #m2 = pd.read_csv(model2, delimiter = ' ', skiprows = [0], index_col = 0, header = None)


    for i in range(1, num_sites + 1):
        ind = [word + '_m' + str(i) for word in models[i].index]
        models[i].index = ind

    m = pd.concat([v for k, v in models.iteritems()])

    with open('trainv_' + rep + '_comb', 'w') as f:
        f.write(' '.join([str(i) for i in list(m.shape)]) + '\n')
        m.to_csv(f, sep = ' ', header = None)


    for k, model in models.iteritems():
        with open('trainv_' + rep + '_' + str(k) + '_trained_m', 'w') as f:
            f.write(' '.join([str(i) for i in list(model.shape)]) + '\n')
            model.to_csv(f, sep = ' ', header = None)
            f.close()

#for i in range(0, 10):
#    comb('trainv_' + str(i) + '_50_1_many_delete_100_part_1_trained_proTran', 'trainv_' + str(i) + '_50_2_many_delete_100_part_1_trained_proTran')


#for i in range(0, 10):
#    comb('dimension_100/trainv_' + str(i) + '_50_1_trained_proTran', 'dimension_100/trainv_' + str(i) + '_50_2_trained_reduced_100_proTran')


for i in range(0, 10):
    comb('../../../data/3sites/', str(i), 3)
