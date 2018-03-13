from fuse import *
from rearrange import *
from split import *
import os
import sys




#def pipeline(f1, f2, out):
#    d = create_data(f1, f2, ' ')
#    d.procrustes(True, withold, 30)
#    d.combine(out)
#    rearrange(f1, f2, out, withold)

def pipeline(org_file):
    new_dir, split_1, split_2 = split('../nmdsExp_mtv0/', 'trainv_0', 50, 50)
    model = SkipGram(data_path + 'vocab', args.window, args.size, args.decay, bal, prior, ds, args.model)
    model.train(split_1)
    d = create_data(split_1, split_2, ' ')
    d.procrustes(True, False, 30)
    d.combine(new_dir + 'proTran_comb')
    rearrange(split_1, split_2, pro_out)

#pipeline('no_overlaps/sim/m1Sim', 'no_overlaps/sim/m2Sim', 'no_overlaps/sim/Wsim_proTran_comb', True)
#pipeline('no_overlaps/no_witholds/raw_model1', 'no_overlaps/no_witholds/raw_model2', 'no_overlaps/no_witholds/proTran_comb', False)
#pipeline('exp/m1Sim_model', 'exp/m2Sim_model', 'exp/witholds/Wsim_proTran_comb', True)

pipeline('../nmdsExp_mtv0/train_v0')
