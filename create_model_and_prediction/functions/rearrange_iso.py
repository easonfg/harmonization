import numpy as np
import pandas as pd
#from gensim.models import Word2Vec

def rearrange(model1, model2, cat):
    #m1 = pd.read_csv('witholds/m0_20_1', delimiter = ' ', skiprows = [0], index_col = 0, header = None)
    #m2 = pd.read_csv('witholds/m0_20_2', delimiter = ' ', skiprows = [0], index_col = 0, header = None)
    #proTran = pd.read_csv('witholds/WproTran_comb', delimiter = ' ', skiprows = [0], index_col = 0, header = None)
    m1 = pd.read_csv(model1, delimiter = ' ', skiprows = [0], index_col = 0, header = None)
    m2 = pd.read_csv(model2, delimiter = ' ', skiprows = [0], index_col = 0, header = None)
    #proTran = pd.read_csv(comb, delimiter = ' ', skiprows = [0], index_col = 0, header = None)

    m2.index = [e+'_m' for e in m2.index]

    proTran = pd.concat([m1, m2])
    #import pdb; pdb.set_trace()

    #rearrange the matrix to have corr diag of each site on top
    site1 = set(m1.index)
    site2 = set(m2.index)
    d1 = []
    d2 = []

    for each in m1.index:
        if each.startswith(tuple(cat.split())):
            d1.append(each)
        #else:
        #    rest1.append(each)
    for each in m2.index:
        if each.startswith(tuple(cat.split())):
            d2.append(each)
        #else:
        #    rest2.append(each)

    pure_d2 = [d[:-2] for d in d2]
    corr_diag = set(d1).intersection(set(pure_d2))
    # for creating witholds
    #withold = True
    #if withold == True:
    #    wList = 'd_428 d_276 d_427 d_250 d_401 d_E9413 d_E9398 d_E9301 d_E9300 d_E8708'.split()
    #    corr_diag = set([i for i in corr_diag if i not in wList])

    rest1 = site1 - corr_diag
    rest1 = list(rest1)

    corr_diag1 = list(corr_diag)
    corr_diag2 = [e+'_m' for e in corr_diag1]
    rest2 = site2 - set(corr_diag2)
    rest2 = list(rest2)
    #cd2 = [e for e in d2 if e[:-2] in d1]


    rm1 = m1.reindex(corr_diag1+rest1)
    rm2 = m2.reindex(corr_diag2+rest2)
    RproTran = proTran.reindex(corr_diag1+rest1+corr_diag2+rest2)
    #import pdb; pdb.set_trace()
    rm2_ind = [i[:-2] for i in rm2.index]
    rm2.index = rm2_ind

    rm1.to_csv(model1+'R', sep = ' ')
    rm2.to_csv(model2+'R', sep = ' ')
    RproTran.to_csv('/'.join(model1.split('/')[:-1]) + '/org_combR', sep = ' ')

    #reformat(model1+'R')
    #reformat(model2+'R')
    #reformat(comb+'R')



def reformat(filename):
    with file(filename, 'r') as original:
        data = original.readlines()[1:]
    with file(filename, 'w') as modified:
        modified.write(str(len(data)) + ' ' + str(len(data[0].split())-1) +  "\n" + ''.join(data))

    #if withold == True:
    #    rm1.to_csv(model1 + 'R', sep = ' ')
    #    rm2.to_csv(model2 + 'R', sep = ' ')
    #    RproTran.to_csv(comb + 'R', sep = ' ')
    #else:
    #    rm1.to_csv('witholds/Rm0_20_1', sep = ' ')
    #    rm2.to_csv('witholds/Rm0_20_2', sep = ' ')
    #    RproTran.to_csv('witholds/RproTran_comb', sep = ' ')

#proTran = pd.read_csv('proTran_comb', delimiter = ' ', skiprows = [0], index_col = 0, header = None)
#
#RproTran = proTran.reindex(

#rearrange('sim/m1Sim', 'sim/m2Sim', 'sim/WproTran_sim_comb')
#rearrange('no_overlaps/raw_model1', 'no_overlaps/raw_model2', 'no_overlaps/Wraw_proTran_comb')
#rearrange('../nmdsExp_mtv0/50_50/trainv_0_50_1_trained', '../nmdsExp_mtv0/50_50/trainv_0_50_2_trained', '../nmdsExp_mtv0/50_50/org_comb')

#rearrange('/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/diabetes_cohorts/d_715/small_cohort_trained',
#          '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/diabetes_cohorts/d_715/big_cohort_trained',
#          '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/diabetes_cohorts/d_715/cohort_comb', 'd s c l p')


rearrange('/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/cut_first40/many_delete_1_99_trained',
          '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/cut_first40/many_delete_2_99_trained',
          'd s c l p')
