import pandas as pd

def create_org_comb(f1, f2, outname):
    m1 = pd.read_csv(f1, delimiter = ' ', skiprows = [0], index_col = 0, header = None)
    m2 = pd.read_csv(f2, delimiter = ' ', skiprows = [0], index_col = 0, header = None)

    ind = [i+'_m' for i in m2.index]

    m2.index = ind

    m = pd.concat([m1, m2])

    m.to_csv(outname, sep = ' ', header = False)

create_org_comb('d_008_big_trained', 'd_008_small_trained', 'd_008_org_comb')
