from pdps import *
import re
import fileinput
import numpy as np
#from pdes import *

def create_model(vocab_file, infile):
    #model = SkipGram(vocab_file, 30, 100, 0, 0, 0, 'mimic', 'org')
    model = SkipGram(vocab_file, 30, 350, 0, 0, 0, 'mimic', 'org')
    #model = CbowSim(vocab_file, 30, 350, 0, 0, 0, 'mimic', 'org')
    #model = CbowSim(vocab_file, 30, 350, 8, 0, 0, 'mimic', 'org')
    model.train(infile)
    outname = infile + '_trained'
    #model._model.syn1[model._model.vocab[''].index]
    #model._model.syn0 = np.delete(model._model.syn0, (model._model.vocab[''].index), axis = 0)
    #del model._model.vocab['']
    model.save_hr_model(outname)


