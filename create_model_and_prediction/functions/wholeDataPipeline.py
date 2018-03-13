from pdps import *

def wholeData_pipeline(vocab_file, infile, outname):
    model = SkipGram(vocab_file, 30, 350, 8, 0, 0, 'mimic', 'org')
    model.train(infile)
    model.save_hr_model(outname)


#wholeData_pipeline('../Data/mimic_seq/vocab', 'nmdsExp_mtv1/trainv_1', 'nmdsExp_mtv1/mtv1_whole_trained')
#wholeData_pipeline('../Data/mimic_seq/vocab', 'nmdsExp_mtv2/trainv_2', 'nmdsExp_mtv2/mtv2_whole_trained')
#wholeData_pipeline('../Data/mimic_seq/vocab', 'nmdsExp_mtv3/trainv_3', 'nmdsExp_mtv3/mtv3_whole_trained')
#wholeData_pipeline('../Data/mimic_seq/vocab', 'nmdsExp_mtv4/trainv_4', 'nmdsExp_mtv4/mtv4_whole_trained')
#

#prediction_pipeline('../Data/mimic_seq/vocab', 'org', 'nmdsExp_mtv0/mtv0_whole_trained', 'split_test_sets/trainv_0')
#prediction_pipeline('split_test_sets/vocab_twoSites', 'twoSites_w_orgM', 'nmdsExp_mtv0/mtv0_whole_trained', 'split_test_sets/trainv_0_twoSites')
#prediction_pipeline('split_test_sets/vocab_twoSites', 'twoSites_w_fusedM', 'nmdsExp_mtv0/50_50/nmds_50_w_7AB_W', 'split_test_sets/trainv_0_twoSites')


#wholeData_pipeline('../Data/mimic_seq/vocab', 'nmdsExp_mtv2/95_5/trainv_2_95_1', 'nmdsExp_mtv2/95_5/trainv_2_95_1_trained')
#wholeData_pipeline('../Data/mimic_seq/vocab', 'nmdsExp_mtv2/95_5/trainv_2_5_2', 'nmdsExp_mtv2/95_5/trainv_2_5_2_trained')

#wholeData_pipeline('../Data/mimic_seq/vocab', 'nmdsExp_mtv2/95_5/trainv_2_95_1', 'nmdsExp_mtv2/95_5/trainv_2_95_1_trained')
#wholeData_pipeline('../Data/mimic_seq/vocab', 'nmdsExp_mtv2/95_5/trainv_2_5_2', 'nmdsExp_mtv2/95_5/trainv_2_5_2_trained')
