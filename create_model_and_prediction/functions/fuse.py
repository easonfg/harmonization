import random
import numpy as np
import pandas as pd

#labels = np.genfromtxt('mimic_e_vectors', delimiter=' ', usecols=0, dtype=str)
#raw_data = np.genfromtxt('mimic_e_vectors', delimiter=" ")[:,1:]
#data = {label: row for label, row in zip(labels, raw_data)}

#print data

class create_data(object):

    def __init__(self, mimic_file, ucsd_file, separator):

        self.mimic = pd.read_csv(mimic_file, delimiter = separator, skiprows = [0], index_col = 0, header = None)
        self.ucsd = pd.read_csv(ucsd_file, delimiter = separator, skiprows = [0], index_col = 0, header = None)
        self.m_diag = [d for d in self.mimic.index if d.startswith('d')]
        self.u_diag = [d for d in self.ucsd.index if d.startswith('d')]
        #self.mimic = pd.read_csv('mimic_concat_f', delimiter = ' ', index_col = 0, header = None)
        #self.ucsd = pd.read_csv('ucsd_concat_f', delimiter = ' ', index_col = 0, header = None)
        #self.test = pd.read_csv('test', delimiter = ' ', index_col = 0, header = None)
        #self.test = self.test.ix[0:10, 0:5]

    #print mimic
    ##return row by row label
    #print len(mimic.loc['d_621'])
    ## return the first column
    #print (mimic.ix[0, :])
    ##return row by row index
    #print len(mimic.iloc[0])

    def output(self):
        print len(self.test.iloc[0])
        print len(self.test.ix[0, :])
        print len(self.test.index)
        self.eig_values, self.eig_vectors = np.linalg.eig(self.test)
        print self.eig_vectors

    def create_all_events(self, m_file, u_file):
        #for checking if numbers adds up
        m_orgCount = len(self.mimic.index)
        u_orgCount = len(self.ucsd.index)

        #find unique diag in mimic and ucsd
        intersect = set(self.m_diag).intersection(set(self.u_diag))
        self.uniq_mDiag = set(self.m_diag) - intersect
        self.uniq_uDiag = set(self.u_diag) - intersect

        count = 0
        for event in self.uniq_mDiag:
            self.ucsd.loc[event] = self.mimic.loc[event]

        for event in self.uniq_uDiag:
            self.mimic.loc[event] = self.ucsd.loc[event]

        self.ucsd.to_csv(u_file, sep = ' ', header = None)
        self.mimic.to_csv(m_file, sep = ' ', header = None)

        if len(self.mimic.index) == len(self.uniq_uDiag) + m_orgCount:
            print 'm passed'
        if len(self.ucsd.index) == len(self.uniq_mDiag) + u_orgCount:
            print 'u passed'

        with file(m_file, 'r') as original: data = original.read()
        with file(m_file, 'w') as modified: modified.write(str(self.mimic.shape[0]) + ' ' + str(self.mimic.shape[1]) + "\n" + data)

        with file(u_file, 'r') as original: data = original.read()
        with file(u_file, 'w') as modified: modified.write(str(self.ucsd.shape[0]) + ' ' + str(self.ucsd.shape[1]) + "\n" + data)



    def _find_int(self, b, withold, limit, cat, perc):
        #if b is true, use only diagnosises as corespondence
        if b == True:
            categories = cat.split()
            # find all diagnoses that are common in both datasets
            #m_ls = []
            #u_ls = []
            intersect = []
            for each in categories:
                tmp_m_diag = [i for i in self.mimic.index if i.startswith(each)]
                tmp_u_diag = [i for i in self.ucsd.index if i.startswith(each)]
                tmp_inter = set(tmp_m_diag).intersection(set(tmp_u_diag))
                tmp_inter = list(tmp_inter)

                if perc != 100:
                    tmp_inter = random.sample(tmp_inter, int(len(tmp_inter)*(perc/100.0)))

                intersect += tmp_inter

                #m_ls += tmp_m_diag
                #u_ls += tmp_u_diag

            #intersect=set(tmp_m_diag).intersection(set(tmp_u_diag))
            #intersect=set(m_ls).intersection(set(u_ls))



        # for creating witholds
            if withold == True:
                wList = 'd_428 d_276 d_427 d_250 d_401 d_E9413 d_E9398 d_E9301 d_E9300 d_E8708'.split()
                corr_diag = set([i for i in intersect if i not in wList])
            else:
                corr_diag = intersect

        else:
        # find common diagnoses and c, and s, and l, and p
            inter =self.ucsd.index.intersection(self.mimic.index)
            intersect = []
            p,c,s,l = 0, 0, 0, 0
            for e in inter:
                if e.startswith('d'):
                    intersect.append(e)
                else:
                    if e.startswith('p') and p < limit:
                        intersect.append(e)
                        p += 1
                    elif e.startswith('c') and c < limit*0.15:
                        intersect.append(e)
                        c += 1
                    elif e.startswith('s') and s < limit*0.15:
                        intersect.append(e)
                        s += 1
                    elif e.startswith('l') and l < limit*0.15:
                        intersect.append(e)
                        l += 1

        return corr_diag


    def procrustes(self, boolean, w, limit, cat, perc):

        intersect = self._find_int(boolean, w, limit, cat, perc)
        print len(intersect)
        #import pdb; pdb.set_trace()

        m_diag = self.mimic.loc[intersect]
        u_diag = self.ucsd.loc[intersect]

        ones = np.ones((len(intersect), 1))
        Um = np.matrix(m_diag).mean(0)
        Uu = np.matrix(u_diag).mean(0)

        #centralize with mean
        #m_diag_c = m_diag - ones*(Um)
        #u_diag_c = u_diag - ones*(Uu)
        m_diag_c = m_diag
        u_diag_c = u_diag

        U,S,V_t = np.linalg.svd(np.matrix(m_diag_c).transpose()*(np.matrix(u_diag_c)), full_matrices=False)
        Q = U*(V_t)

        k = sum(S)/np.trace(np.matrix(u_diag).transpose()*(np.matrix(u_diag)))

        #ones = np.ones((len(self.mimic), 1))
        #t_mimic = self.mimic - ones*(np.matrix(self.mimic).mean(0))
        #ones = np.ones((len(self.ucsd), 1))
        #t_ucsd = k*np.matrix(self.ucsd - ones*(np.matrix(self.ucsd).mean(0)))*Q
        #t_ucsd = pd.DataFrame(data=t_ucsd, index=self.ucsd.index)

        ones = np.ones((len(self.mimic), 1))
        #times K and Q after centralized
        #self.t_mimic = k*np.matrix(self.mimic - ones*(np.matrix(self.mimic).mean(0)))*Q
        self.t_mimic = k*np.matrix(self.mimic)*Q
        self.t_mimic = pd.DataFrame(data=self.t_mimic, index=self.mimic.index)
        ones = np.ones((len(self.ucsd), 1))
        #centralized
        #self.t_ucsd = (self.ucsd - ones*(np.matrix(self.ucsd).mean(0)))
        self.t_ucsd = (self.ucsd)

    #write out procrustes transformed files
    def write_out(self, name1, name2):
        #self.t_mimic.to_csv(name1, sep = ' ')
        #self.t_ucsd.to_csv(name2, sep = ' ')


        with open(name1, 'w') as f:
            f.write(' '.join([str(i) for i in list(self.t_mimic.shape)]) + '\n')
            self.t_mimic.to_csv(f, sep = ' ', header=None)
        f.close()

        with open(name2, 'w') as f:
            f.write(' '.join([str(i) for i in list(self.t_ucsd.shape)]) + '\n')
            self.t_ucsd.to_csv(f, sep = ' ', header=None)
        f.close()


        #with file(name1, 'r') as original:
        #    data = original.readlines()[1:]
        #with file(name1, 'w') as modified:
        #    modified.write(str(len(data)) + ' ' + str(len(data[0].split())-1) +  "\n" + ''.join(data))

        #with file(name2, 'r') as original:
        #    data = original.readlines()[1:]
        #with file(name2, 'w') as modified:
        #    modified.write(str(len(data)) + ' ' + str(len(data[0].split())-1) +  "\n" + ''.join(data))


    #write out combined procrustes transformed files
    def combine(self, filename):
        for event in self.t_ucsd.index:
            name = event + '_m'
            self.t_mimic.loc[name] = list(self.t_ucsd.loc[event])

        with open(filename, 'w') as f:
            f.write(' '.join([str(i) for i in list(self.t_mimic.shape)]) + '\n')
            self.t_mimic.to_csv(f, sep = ' ', header=None)
        f.close()


        #self.t_mimic.to_csv(filename, sep = ' ', header = None)

        #with file(filename, 'r') as original: data = original.read()
        #with file(filename, 'w') as modified: modified.write(str(self.t_mimic.shape[0]) + ' ' + str(self.t_mimic.shape[1]) + "\n" + data)

    def combine_raw(self, filename):
        for event in self.t_mimic.index:
            name = event
            self.t_ucsd.loc[name] = list(self.t_mimic.loc[event])

        self.t_ucsd.to_csv(filename, sep = ' ')

    # combine the orginial two files into org_comb
    def combine_org(self, filename):
        for event in self.ucsd.index:
            name = event + '_m'
            self.mimic.loc[name] = list(self.ucsd.loc[event])

        self.mimic.to_csv(filename, sep = ' ', header = None)

        with file(filename, 'r') as original: data = original.read()
        with file(filename, 'w') as modified: modified.write(str(self.mimic.shape[0]) + ' ' + str(self.mimic.shape[1]) + "\n" + data)

# has wrong header for proTran
def reformat_org_p(infile):
    with open(infile, 'r') as org:
        s = org.readlines()

    s = s[1:]

    with open(infile + '_model', 'w') as mod:
        mod.write(str(len(s)) + ' ' + str(len(s[0].split(' '))-1) + '\n' + ''.join([' '.join(e.split(' '))for e in s]))

def reformat_org(infile):
    with open(infile, 'r') as org:
        s = org.readlines()

    s = s[1:]

    with open(infile + '_model', 'w') as mod:
        mod.write(str(len(s)) + ' ' + str(len(s[0].split(','))-1) + '\n' + ''.join([' '.join(e.split(','))for e in s]))

def reformat_tran(infile):
    with open(infile, 'r') as org:
        s = org.readlines()

    with open(infile, 'w') as mod:
        mod.write(str(len(s)) + ' ' + str(len(s[0].split(' '))-1) + '\n' + ''.join(s))




#d = create_data('witholds/m0_20_1', 'witholds/m0_20_2', ' ')
#d.procrustes(True, True, 30)
#d.combine('witholds/WproTran_comb')

#d = create_data('witholds/m0_20_1', 'witholds/m0_20_2', ' ')
#d.procrustes(True, True, 30)
#d.combine('witholds/WproTran_comb')

#d = create_data('sim/m1Sim', 'sim/m2Sim', ',')
#d.procrustes(True, True, 30)
#d.combine('sim/WproTran_sim_comb')

#d = create_data('no_overlaps/raw_model1', 'no_overlaps/raw_model2', ' ')
#d.procrustes(True, True, 30)
#d.combine('no_overlaps/Wraw_proTran_comb')

#d = create_data('no_overlaps/sim/m1Sim', 'no_overlaps/sim/m2Sim', ' ')
#d.procrustes(True, True, 30)
#d.combine('no_overlaps/sim/Wsim_proTran_comb')

