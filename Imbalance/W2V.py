import os
import argparse
import math
import gensim
import pandas as pd

def jh_pv(infile,outfile):
    with open(infile) as f:
        s = f.readlines()
        events = []
        for i, line in enumerate(s):
            events.append(line.replace("\n", "").split(" "))
       
    model = gensim.models.Word2Vec(events, sg=1, size=350, window=30, min_count=1, workers=20)
    model.wv.save_word2vec_format(outfile)

jh_pv('train_overlap.txt','train_s1_overlap_w2v.txt')
jh_pv('train_nonoverlap.txt','train_s2_w2v.txt')

