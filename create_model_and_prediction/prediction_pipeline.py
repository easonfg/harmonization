from pdps import *
#from pdps_noDecay import *


#def prediction_pipeline(vocab_file, model_vectors, test_file, outname, name_suf = ''):
def prediction_pipeline(vocab_file, model_vectors, test_file, name_suf = ''):
    #model = SkipGram(vocab_file, 30, 100, 0, 0, 0, 'mimic', 'org')
    model = SkipGram(vocab_file, 30, 350, 0, 0, 0, 'mimic', 'org')
    #model = SkipGram(vocab_file, 30, 350, 8, 0, 0, 'mimic', 'org')
    model.load_hr_model(model_vectors)
    #import pdb; pdb.set_trace()
    model.valid(test_file)
    outname = model_vectors.split('/')[-1] + name_suf
    model.outname = outname
    model.write_stats()
    print outname, ',', model.sum_auc*1.0/len(model._diags)
    return outname +  ',' +  str(model.sum_auc*1.0/len(model._diags))


def test_prediction_pipeline(vocab_file, model_vectors, test_file, name_suf = 'test'):
    model = SkipGram(vocab_file, 30, 350, 8, 0, 0, 'mimic', 'org')
    model.load_hr_model(model_vectors)
    model.valid(test_file)
    outname = model_vectors.split('/')[-1] + name_suf
    model.outname = outname
    model.write_stats()
    print outname, ',', model.sum_auc*1.0/len(model._diags)

#prediction_pipeline('../Data/mimic_seq/vocab', 'org', 'nmdsExp_mtv0/mtv0_whole_trained', 'split_test_sets/trainv_0')
#prediction_pipeline('split_test_sets/vocab_twoSites', 'twoSites_w_orgM', 'nmdsExp_mtv0/mtv0_whole_trained', 'split_test_sets/trainv_0_twoSites')
#prediction_pipeline('split_test_sets/vocab_twoSites', 'nmdsExp_mtv0/mtv0_whole_trained', 'split_test_sets/test_0_twoSites', 'twoSites_orgM')
#prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv1/results/mds_ver2_better', 'split_test_sets/test_0_twoSites', 'mds_ver2')
#prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv1/results/mds_ver2_better', 'split_test_sets/test_0_twoSites', 'mds_ver2')
#prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv1/results/mds_ver1', 'split_test_sets/test_0_twoSites', 'mds_ver1')
#prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv1/results/pro_init_NMDS_noW_ver0', 'split_test_sets/test_0_twoSites', 'nmds_ver0')
#prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv1/results/pro_init_NMDS_wW', 'split_test_sets/test_0_twoSites', 'pro_init_NMDS_wW')
#prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv1/results/pro_init_NMDS_wW_1inAB', 'split_test_sets/test_0_twoSites', 'pro_init_NMDS_wW_1inAB')


#prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv1/proTran_combR', 'split_test_sets/test_0_twoSites', 'proTran_combR')
#prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv0/mtv0_whole_trained', 'split_test_sets/test_0', 'org_org')

#prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv0/mtv0_whole_trained', 'split_test_sets/test_0', 'org_org')
#prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv0/mtv0_whole_trained', 'split_test_sets/test_0_twoSites', 'twoSites_orgM')
#prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv0/results/mds_ver1', 'split_test_sets/test_0_twoSites', 'mtv0_mds_ver1')
#prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv0/results/mds_ver2_better', 'split_test_sets/test_0_twoSites', 'mtv0_mds_ver2')
#prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv0/results/pro_init_NMDS_noW_ver0', 'split_test_sets/test_0_twoSites', 'mtv0_nmds_ver0')
#prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv0/results/pro_init_NMDS_proNormalized_wW', 'split_test_sets/test_0_twoSites', 'mtv0_nmds_ver1')
#prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv0/results/pro_init_NMDS_proNormalized_wW_1inALL_AB', 'split_test_sets/test_0_twoSites', 'mtv0_nmds_ver2')
#prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv0/results/pro_init_NMDS_proNormalized_wW_1inAB', 'split_test_sets/test_0_twoSites', 'mtv0_nmds_ver2')
#prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv0/results/smooth_nmds_ver2', 'split_test_sets/test_0_twoSites', 'mtv0_nmds_ver2')
#
#print 'mtv2_org_org', prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv2/mtv2_whole_trained', 'split_test_sets/test_2', 'mtv2_org_org')
#print 'mtv2_twoSites_orgM', prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv2/mtv2_whole_trained', 'split_test_sets/test_2_twoSites', 'mtv2_twoSites_orgM')
#print 'org_model_twoSites', prediction_pipeline('split_test_sets/vocab_twoSites', 'nmdsExp_mtv2/mtv2_whole_trained', 'split_test_sets/test_2_twoSites', 'org_model_twoSites')
#print 'mtv2_twoSites_orgM_twositeDiags', prediction_pipeline('split_test_sets/vocab_twoSites', 'nmdsExp_mtv2/mtv2_all_trained', 'split_test_sets/test_2_twoSites', 'mtv2_twoSites_orgM_twositeDiags')
#print 'mtv2_twoSites_orgM_twositeDiags_new', prediction_pipeline('split_test_sets/vocab_twoSites_noNewDiags', 'nmdsExp_mtv2/mtv2_all_trained', 'split_test_sets/test_2_twoSites_onesiteDiags', 'mtv2_twoSites_orgM_twositeDiags_new')
#print 'mtv2_mds_ver1', prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv2/results/mds_ver1', 'split_test_sets/test_2_twoSites', 'mtv2_mds_ver1')
#print 'mtv2_mds_ver2', prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv2/results/mds_ver2', 'split_test_sets/test_2_twoSites', 'mtv2_mds_ver2')
#print 'mtv2_nmds_ver0', prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv2/results/pro_init_NMDS_noW_ver0', 'split_test_sets/test_2_twoSites', 'mtv2_nmds_ver0')
#print 'mtv2_nmds_ver1', prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv2/results/pro_init_NMDS_wW', 'split_test_sets/test_2_twoSites', 'mtv2_nmds_ver1')
#print 'mtv2_nmds_ver2', prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv2/results/pro_init_NMDS_wW_1inAB', 'split_test_sets/test_2_twoSites', 'mtv2_nmds_ver2')
#print 'mtv2_smooth_nmds_ver2', prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv2/results/smooth_nmds_ver2', 'split_test_sets/test_2_twoSites', 'mtv2_smooth_nmds_ver2')
#
#
#print 'mds_ver2_30', prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv2/diff_perc/results/mds_ver2_30', 'split_test_sets/test_2_twoSites', 'mds_ver2_30')
#print 'mds_ver2_50', prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv2/diff_perc/results/mds_ver2_50', 'split_test_sets/test_2_twoSites', 'mds_ver2_50')
#print 'mds_ver2_70', prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv2/diff_perc/results/mds_ver2_70', 'split_test_sets/test_2_twoSites', 'mds_ver2_70')
#print 'mds_ver2_90', prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv2/diff_perc/results/mds_ver2_90', 'split_test_sets/test_2_twoSites', 'mds_ver2_90')

#print 'smooth_nmds_ver2_30', prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv2/diff_perc/results/smooth_nmds_ver2_30', 'split_test_sets/test_2_twoSites', 'smooth_nmds_ver2_30')
#print 'smooth_nmds_ver2_50', prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv2/diff_perc/results/smooth_nmds_ver2_50', 'split_test_sets/test_2_twoSites', 'smooth_nmds_ver2_50')
#print 'smooth_nmds_ver2_70', prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv2/diff_perc/results/smooth_nmds_ver2_70', 'split_test_sets/test_2_twoSites', 'smooth_nmds_ver2_70')
#print 'smooth_nmds_ver2_90', prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv2/diff_perc/results/smooth_nmds_ver2_90', 'split_test_sets/test_2_twoSites', 'smooth_nmds_ver2_90')

#print 'mds_ver2_100overlap_80_20split', prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/mds_ver2_100', 'split_test_sets/test_2_twoSites', 'mds_ver2_100overlap_80_20split')
#print 'reg_nmds_ver2_100opverlap_80_20split', prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/reg_nmds_ver2_100', 'split_test_sets/test_2_twoSites', 'reg_nmds_ver2_100opverlap_80_20split')
#print 'smooth_nmds_ver2_100overlap_80_20_split', prediction_pipeline('split_test_sets/vocab_twoSites', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/smooth_nmds_ver2_100', 'split_test_sets/test_2_twoSites', 'smooth_nmds_ver2_100overlap_80_20_split')



#print 'mtv2_org_org', prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv2/mtv2_whole_trained', 'split_test_sets/test_2', 'mtv2_org_org')
#print 'org_model_twoSites', prediction_pipeline('split_test_sets/vocab_twoSites', 'nmdsExp_mtv2/mtv2_all_trained', 'split_test_sets/test_2_twoSites', 'org_model_twoSites')
#print 'test', prediction_pipeline('split_test_sets/vocab_twoSites_noNewDiags', 'nmdsExp_mtv2/mtv2_all_trained', 'split_test_sets/test_2_twoSites', 'test')
##print 'mtv2_twoSites_orgM', prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv2/mtv2_whole_trained', 'split_test_sets/test_2_twoSites', 'mtv2_twoSites_orgM')
##print 'org_model_twoSites', prediction_pipeline('split_test_sets/vocab_twoSites', 'nmdsExp_mtv2/mtv2_whole_trained', 'split_test_sets/test_2_twoSites', 'org_model_twoSites')
##print 'mtv2_twoSites_orgM_twositeDiags', prediction_pipeline('split_test_sets/vocab_twoSites', 'nmdsExp_mtv2/mtv2_all_trained', 'split_test_sets/test_2_twoSites', 'mtv2_twoSites_orgM_twositeDiags')
#print 'org', prediction_pipeline('split_test_sets/vocab_twoSites_noNewDiags', 'nmdsExp_mtv2/mtv2_all_trained', 'split_test_sets/test_2_twoSites_onesiteDiags', 'mtv2_twoSites_orgM_twositeDiags_new')
#print 'mtv2_mds_ver1', prediction_pipeline('split_test_sets/vocab_twoSites_noNewDiags', '/Users/henry/Desktop/mtv2/results/mds_ver1', 'split_test_sets/test_2_twoSites_onesiteDiags', 'mtv2_mds_ver1')
#print 'mtv2_mds_ver2', prediction_pipeline('split_test_sets/vocab_twoSites_noNewDiags', '/Users/henry/Desktop/mtv2/results/mds_ver2', 'split_test_sets/test_2_twoSites_onesiteDiags', 'mtv2_mds_ver2')
#print 'mtv2_nmds_ver0', prediction_pipeline('split_test_sets/vocab_twoSites_noNewDiags', '/Users/henry/Desktop/mtv2/results/pro_init_NMDS_noW_ver0', 'split_test_sets/test_2_twoSites_onesiteDiags', 'mtv2_nmds_ver0')
#print 'mtv2_nmds_ver1', prediction_pipeline('split_test_sets/vocab_twoSites_noNewDiags', '/Users/henry/Desktop/mtv2/results/pro_init_NMDS_wW', 'split_test_sets/test_2_twoSites_onesiteDiags', 'mtv2_nmds_ver1')
#print 'mtv2_nmds_ver2', prediction_pipeline('split_test_sets/vocab_twoSites_noNewDiags', '/Users/henry/Desktop/mtv2/results/pro_init_NMDS_wW_1inAB', 'split_test_sets/test_2_twoSites_onesiteDiags', 'mtv2_nmds_ver2')
#print 'mtv2_smooth_nmds_ver2', prediction_pipeline('split_test_sets/vocab_twoSites_noNewDiags', '/Users/henry/Desktop/mtv2/results/smooth_nmds_ver2', 'split_test_sets/test_2_twoSites_onesiteDiags', 'mtv2_smooth_nmds_ver2')
#
#
#print 'mds_ver2_30', prediction_pipeline('split_test_sets/vocab_twoSites_noNewDiags', '/Users/henry/Desktop/mtv2/diff_perc/results/mds_ver2_30', 'split_test_sets/test_2_twoSites_onesiteDiags', 'mds_ver2_30')
#print 'mds_ver2_50', prediction_pipeline('split_test_sets/vocab_twoSites_noNewDiags', '/Users/henry/Desktop/mtv2/diff_perc/results/mds_ver2_50', 'split_test_sets/test_2_twoSites_onesiteDiags', 'mds_ver2_50')
#print 'mds_ver2_70', prediction_pipeline('split_test_sets/vocab_twoSites_noNewDiags', '/Users/henry/Desktop/mtv2/diff_perc/results/mds_ver2_70', 'split_test_sets/test_2_twoSites_onesiteDiags', 'mds_ver2_70')
#print 'mds_ver2_90', prediction_pipeline('split_test_sets/vocab_twoSites_noNewDiags', '/Users/henry/Desktop/mtv2/diff_perc/results/mds_ver2_90', 'split_test_sets/test_2_twoSites_onesiteDiags', 'mds_ver2_90')
#
#print 'smooth_nmds_ver2_30', prediction_pipeline('split_test_sets/vocab_twoSites_noNewDiags', '/Users/henry/Desktop/mtv2/diff_perc/results/smooth_nmds_ver2_30', 'split_test_sets/test_2_twoSites_onesiteDiags', 'smooth_nmds_ver2_30')
#print 'smooth_nmds_ver2_50', prediction_pipeline('split_test_sets/vocab_twoSites_noNewDiags', '/Users/henry/Desktop/mtv2/diff_perc/results/smooth_nmds_ver2_50', 'split_test_sets/test_2_twoSites_onesiteDiags', 'smooth_nmds_ver2_50')
#print 'smooth_nmds_ver2_70', prediction_pipeline('split_test_sets/vocab_twoSites_noNewDiags', '/Users/henry/Desktop/mtv2/diff_perc/results/smooth_nmds_ver2_70', 'split_test_sets/test_2_twoSites_onesiteDiags', 'smooth_nmds_ver2_70')
#print 'smooth_nmds_ver2_90', prediction_pipeline('split_test_sets/vocab_twoSites_noNewDiags', '/Users/henry/Desktop/mtv2/diff_perc/results/smooth_nmds_ver2_90', 'split_test_sets/test_2_twoSites_onesiteDiags', 'smooth_nmds_ver2_90')
#
#print 'mds_ver2_100overlap_80_20split', prediction_pipeline('split_test_sets/vocab_twoSites_noNewDiags', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/mds_ver2_100', 'split_test_sets/test_2_twoSites_onesiteDiags', 'mds_ver2_100overlap_80_20split')
#print 'reg_nmds_ver2_100opverlap_80_20split', prediction_pipeline('split_test_sets/vocab_twoSites_noNewDiags', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/reg_nmds_ver2_100', 'split_test_sets/test_2_twoSites_onesiteDiags', 'reg_nmds_ver2_100opverlap_80_20split')
#print 'smooth_nmds_ver2_100overlap_80_20_split', prediction_pipeline('split_test_sets/vocab_twoSites_noNewDiags', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/smooth_nmds_ver2_100', 'split_test_sets/test_2_twoSites_onesiteDiags', 'smooth_nmds_ver2_100overlap_80_20_split')


#print 'org_model_twoSites', prediction_pipeline('split_test_sets/vocab_twoSites', 'nmdsExp_mtv2/mtv2_whole_trained', 'split_test_sets/test_2_twoSites', 'org_model_twoSites')

#print '80percent_org', prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv2/80_20/trainv_2_80_1_trained', 'split_test_sets/test_2', 'org_model_80percent')
#print '20percent_org', prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv2/80_20/trainv_2_20_2_trained', 'split_test_sets/test_2', 'org_model_20percent')

#print '99percent_org', prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv2/99_1/trainv_2_99_1_trained', 'split_test_sets/test_2', 'org_model_99percent')
#print '99percent_after', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/mtv2/imbalanced/99_1/results/reg_nmds_ver2_100_p1', 'split_test_sets/test_2', 'org_model_99percent')
#print '1percent_org', prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv2/99_1/trainv_2_1_2_trained', 'split_test_sets/test_2', 'org_model_1percent')
#print '1percent_after', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/mtv2/imbalanced/99_1/results/reg_nmds_ver2_100_p2', 'split_test_sets/test_2', 'after_model_1percent')


#print '50percent_org', prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv2/50_50/trainv_2_50_1_trained', 'split_test_sets/test_2', 'org_model_50percent')
#print '50percent_after', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/mtv2/results/pro_init_NMDS_wW_1inAB_p1', 'split_test_sets/test_2', 'after_model_50percent')

#print '90percent_org', prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv2/90_10/trainv_2_90_1_trained', 'split_test_sets/test_2', 'org_model_90percent')
#print 'mds2_model_90percent', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/results/mds_ver2_100_p1', 'split_test_sets/test_2', 'mds2_model_90percent')
#print 'nmds0_model_90percent', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/results/nmds_ver0_100_p1', 'split_test_sets/test_2', 'nmds0_model_90percent')
#print 'nmds2_model_90percent', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/results/reg_nmds_ver2_100_p1', 'split_test_sets/test_2', 'nmds2_model_90percent')
#print 'smooth_nmds2_model_90percent', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/results/smooth_nmds_ver2_100_p1', 'split_test_sets/test_2', 'smooth_nmds2_model_90percent')
#
#
#
#print '10percent_org', prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv2/90_10/trainv_2_10_2_trained', 'split_test_sets/test_2', 'org_model_10percent')
#print '10percent_org', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/results/mds_ver2_100_p2', 'split_test_sets/test_2', 'mds2_model_10percent')
#print '10percent_org', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/results/nmds_ver0_100_p2', 'split_test_sets/test_2', 'nmds0_model_10percent')
#print '10percent_org', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/results/reg_nmds_ver2_100_p2', 'split_test_sets/test_2', 'nmds2_model_10percent')
#print '10percent_org', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/results/smooth_nmds_ver2_100_p2', 'split_test_sets/test_2', 'smooth_nmds2_model_10percent')

#print 'big_site', prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv2/imbalanced/big_site_d_305_trained', 'split_test_sets/test_2', 'big_site')
#print 'small_site', prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv2/imbalanced/small_site_d_305_trained', 'split_test_sets/test_2', 'small_site')


#print '50_mds1', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/mtv2/results/mds_ver1_p1', 'split_test_sets/test_2', 'after_model_1percent')
#print '50_mds2', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/mtv2/results/mds_ver2_p1', 'split_test_sets/test_2', 'after_model_1percent')
#print '50_nmds0', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/mtv2/results/pro_init_NMDS_noW_ver0_p1', 'split_test_sets/test_2', 'after_model_1percent')
#print '50_nmds1', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/mtv2/results/pro_init_NMDS_wW_p1', 'split_test_sets/test_2', 'after_model_1percent')
#print '50_nmds2', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/mtv2/results/pro_init_NMDS_wW_1inAB_p1', 'split_test_sets/test_2', 'after_model_1percent')
#print '50_smooth_nmds2', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/mtv2/results/smooth_nmds_ver2_p1', 'split_test_sets/test_2', 'after_model_1percent')

#
#print '20_pro', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/proTran2_d_s_c_l_p_100', 'split_test_sets/test_2', 'after_model_1percent')
#print '20_mds1', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/mds_ver1_100_p2', 'split_test_sets/test_2', 'after_model_1percent')
#print '20_mds2', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/mds_ver2_100_p2', 'split_test_sets/test_2', 'after_model_1percent')
#print '20_nmds0', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/nmds_ver0_100_p2', 'split_test_sets/test_2', 'after_model_1percent')
##print '20_nmds1', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/pro_init_NMDS_wW_p2', 'split_test_sets/test_2', 'after_model_1percent')
#print '20_nmds2', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/reg_nmds_ver2_100_p2', 'split_test_sets/test_2', 'after_model_1percent')
#print '20_smooth_nmds2', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/smooth_nmds_ver2_100_p2', 'split_test_sets/test_2', 'after_model_1percent')


#print 'diabetes_cohort_whole', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/diabetes_cohorts/diabetes_cohort_whole_trained', 'split_test_sets/test_2', 'diabetes_cohort_whole')
#print 'diabetes_cohort_p1_trained', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/diabetes_cohorts/diabetes_cohort_p1_trained', 'split_test_sets/test_2', 'diabetes_cohort_p1_trained')
#print 'diabetes_cohort_p2_trained', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/diabetes_cohorts/diabetes_cohort_p2_trained', 'split_test_sets/test_2', 'diabetes_cohort_p2_trained')


#print 'diabetes_cohort_whole', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/diabetes_cohorts/half_cohort/diabetes_cohort_whole_trained', 'split_test_sets/test_2', 'diabetes_cohort_whole')
#print 'diabetes_cohort_p1_trained', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/diabetes_cohorts/half_cohort/diabetes_cohort_p1_trained', 'split_test_sets/test_2', 'diabetes_cohort_p1_trained')
#print 'diabetes_cohort_p2_trained', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/diabetes_cohorts/half_cohort/diabetes_cohort_p2_trained', 'split_test_sets/test_2', 'diabetes_cohort_p2_trained')


#print 'diabetes_cohort_whole', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/diabetes_cohorts/d_715/d_715_cohort_whole_trained', 'split_test_sets/test_2', 'diabetes_cohort_whole')
#print 'diabetes_cohort_p1_trained', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/diabetes_cohorts/d_715/d_715_cohort_whole_50_1_trained', 'split_test_sets/test_2', 'diabetes_cohort_p1_trained')
#print 'diabetes_cohort_p2_trained', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/diabetes_cohorts/d_715/d_715_cohort_whole_50_2_trained', 'split_test_sets/test_2', 'diabetes_cohort_p2_trained')


#print 'trainv_2_50_1_trained', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/missing_links/trainv_2_50_1_trained', 'split_test_sets/test_2', 'trainv_2_50_1_trained')
#print 'train_2_50_2_missing_link_trained', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/missing_links/train_2_50_2_missing_link_trained', 'split_test_sets/test_2', 'train_2_50_2_missing_link_trained')


#print 'trainv_2_50_1_trained', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/missing_links/80_20/trainv_2_80_1_trained', 'split_test_sets/test_2', 'trainv_2_80_1_trained')

#print 'train_2_50_2_missing_link_trained', prediction_pipeline('split_test_sets/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/missing_links/80_20/trainv_2_20_2_missing_link_trained', 'split_test_sets/test_2', 'trainv_2_20_2_missing_link_trained')



#print 'test_whole', prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv2/diabetes_cohorts/diabetes/diabetes_cohort_whole_trained', 'split_test_sets/test_2', 'test_whole')
#print 'test1', prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv2/diabetes_cohorts/diabetes/diabetes_cohort_p1_trained', 'split_test_sets/test_2', 'test1')
#print 'test2', prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv2/diabetes_cohorts/diabetes/diabetes_cohort_p2_trained', 'split_test_sets/test_2', 'test2')
#print 'not', prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv2/diabetes_cohorts/diabetes/not_diabetes_cohort_whole_trained', 'split_test_sets/test_2', 'test2')

#print 'whole', prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv2/mtv2_whole_trained', 'split_test_sets/test_2', 'whole')
##print 'deleteW1', prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv2/diabetes_cohorts/diabetes/deleteWord1_trained', 'split_test_sets/test_2', 'deleteW1')
#print 'deleteW1', prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv2/diabetes_cohorts/d_715/deleteWord_trained', 'split_test_sets/test_2', 'deleteWord')

#print 'whole', prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv2/diabetes_cohorts/d_715/d_715_cohort_whole_trained', 'split_test_sets/test_2', 'whole')
#print 'd715_1', prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv2/diabetes_cohorts/d_715/d_715_cohort_whole_50_1_trained', 'split_test_sets/test_2', 'deleteW1')
#print 'd715_2', prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv2/diabetes_cohorts/d_715/d_715_cohort_whole_50_2_trained', 'split_test_sets/test_2', 'deleteW2')

#print 'deleted_d_456', prediction_pipeline('split_test_sets/vocab', 'nmdsExp_mtv2/diabetes_cohorts/d_456/deleted_d_456_trained', 'split_test_sets/test_2', 'deleted_d_456')


#print '80_org', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/80_20/trainv_2_80_1_trained', '../Data/mimic_seq/test_2', '80_org')
#print '80_pro', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/proTran1_d_s_c_l_p_100', '../Data/mimic_seq/test_2', '80_pro')
#print '80_mds1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/mds_ver1_100_p1', '../Data/mimic_seq/test_2', '80_mds1')
#print '80_mds2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/mds_ver2_100_p1', '../Data/mimic_seq/test_2', '80_mds2')
#print '80_nmds0', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/nmds_ver0_100_p1', '../Data/mimic_seq/test_2', '80_nmds0')
##print '20_nmds1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/pro_init_NMDS_wW_p2', '../Data/mimic_seq/test_2', 'after_model_1percent')
#print '80_nmds2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/reg_nmds_ver2_100_p1', '../Data/mimic_seq/test_2', '80_nmds2')
#print '80_smooth_nmds2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/smooth_nmds_ver2_100_p1', '../Data/mimic_seq/test_2', '80_smooth_nmds2')
#
#print '20_org', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/80_20/trainv_2_20_2_trained', '../Data/mimic_seq/test_2', '20_org')
#print '20_pro', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/proTran2_d_s_c_l_p_100', '../Data/mimic_seq/test_2', '20_pro')
#print '20_mds1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/mds_ver1_100_p2', '../Data/mimic_seq/test_2', '20_mds1')
#print '20_mds2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/mds_ver2_100_p2', '../Data/mimic_seq/test_2', '20_mds2')
#print '20_nmds0', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/nmds_ver0_100_p2', '../Data/mimic_seq/test_2', '20_nmds0')
##print '20_nmds1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/pro_init_NMDS_wW_p2', '../Data/mimic_seq/test_2', 'after_model_1percent')
#print '20_nmds2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/reg_nmds_ver2_100_p2', '../Data/mimic_seq/test_2', '20_nmds2')
#print '20_smooth_nmds2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/smooth_nmds_ver2_100_p2', '../Data/mimic_seq/test_2', '20_smooth_nmds2')


#print '80_50over_org', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/80_20/trainv_2_80_1_trained', '../Data/mimic_seq/test_2', '80_50over_org')
#print '80_50over_pro', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/proTran1_d_s_c_l_p_50', '../Data/mimic_seq/test_2', '80_50over_pro')
##print '80_mds1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/mds_ver2_100_p1', '../Data/mimic_seq/test_2', '80_mds1')
#print '80_50over_mds2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/mds_ver2_50_p1', '../Data/mimic_seq/test_2', '80_50over_mds2')
#print '80_50over_nmds0', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/nmds_ver0_50_p1', '../Data/mimic_seq/test_2', '80_50over_nmds0')
##print '20_nmds1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/pro_init_NMDS_wW_p2', '../Data/mimic_seq/test_2', 'after_model_1percent')
##print '80_50over_nmds2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/reg_nmds_ver2_50_p1', '../Data/mimic_seq/test_2', '80_50over_nmds2')
#print '80_50over_smooth_nmds2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/smooth_nmds_ver2_50_p1', '../Data/mimic_seq/test_2', '80_50over_smooth_nmds2')
#
#print '20_50over_org', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/80_20/trainv_2_20_2_trained', '../Data/mimic_seq/test_2', '20_50over_org')
#print '20_50over_pro', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/proTran2_d_s_c_l_p_50', '../Data/mimic_seq/test_2', '20_50over_pro')
##print '80_mds1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/mds_ver2_100_p1', '../Data/mimic_seq/test_2', '80_mds1')
#print '20_50over_mds2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/mds_ver2_50_p2', '../Data/mimic_seq/test_2', '20_50over_mds2')
#print '20_50over_nmds0', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/nmds_ver0_50_p2', '../Data/mimic_seq/test_2', '20_50over_nmds0')
##print '20_nmds1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/pro_init_NMDS_wW_p2', '../Data/mimic_seq/test_2', 'after_model_1percent')
##print '20_50over_nmds2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/reg_nmds_ver2_50_p2', '../Data/mimic_seq/test_2', '20_50over_nmds2')
#print '20_50over_smooth_nmds2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/smooth_nmds_ver2_50_p2', '../Data/mimic_seq/test_2', '20_50over_smooth_nmds2')


#print '80_org', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/mtv2_whole_trained', '../Data/mimic_seq/test_2', 'whole_org')
#print 'whole', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/diabetes_cohorts/d_715/d_715_cohort_whole_trained', '../Data/mimic_seq/test_2', 'whole')
#print 'd_715_1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/diabetes_cohorts/d_715/d_715_cohort_whole_95_1_trained', '../Data/mimic_seq/test_2', 'test1')
#print 'd_715_2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/diabetes_cohorts/d_715/d_715_cohort_whole_5_2_trained', '../Data/mimic_seq/test_2', 'test2')


#print 'whole', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/diabetes_cohorts/d_715/d_715_cohort_whole_trained', '../Data/mimic_seq/test_2', 'whole')
#print 'd_715_1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/diabetes_cohorts/d_715/d_715_cohort_whole_99_1_trained', '../Data/mimic_seq/test_2', 'test1')
#print 'd_715_2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/diabetes_cohorts/d_715/d_715_cohort_whole_1_2_trained', '../Data/mimic_seq/test_2', 'test2')


#print 'd_715_1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/diabetes_cohorts/d_715/test1_trained', '../Data/mimic_seq/test_2', 'test1')



#print 'whole_org', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/mtv2_whole_trained', '../Data/mimic_seq/test_2', 'whole_org')
#print 'many_delete_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/cut_first40/many_delete_1_99_trained', '../Data/mimic_seq/test_2', 'many_delete_1_first40')
#print 'many_delete_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/cut_first40/many_delete_2_99_trained', '../Data/mimic_seq/test_2', 'many_delete_2_first40')
#print 'many_deletes_pro_1_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/proTran1_d_s_c_l_p_80', '../Data/mimic_seq/test_2', 'many_deletes_pro_1_first40')
#print 'many_deletes_pro_2_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/proTran2_d_s_c_l_p_80', '../Data/mimic_seq/test_2', 'many_deletes_pro_2_first40')
#print 'many_deletes_mds2_1_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/mds_ver2_99_80_p1', '../Data/mimic_seq/test_2', 'many_deletes_mds2_1_first40')
#print 'many_deletes_mds2_2_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/mds_ver2_99_80_p2', '../Data/mimic_seq/test_2', 'many_deletes_mds2_2_first40')
#print 'many_deletes_nmds0_1_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver0_99_80_p1', '../Data/mimic_seq/test_2', 'many_deletes_nmds0_1_first40')
#print 'many_deletes_nmds0_2_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver0_99_80_p2', '../Data/mimic_seq/test_2', 'many_deletes_nmds0_2_first40')
#print 'many_deletes_nmds2_1_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver2_99_80_p1', '../Data/mimic_seq/test_2', 'many_deletes_nmds2_1_first40')
#print 'many_deletes_nmds2_2_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver2_99_80_p2', '../Data/mimic_seq/test_2', 'many_deletes_nmds2_2_first40')


#print 'whole_org', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/mtv2_whole_trained', '../Data/mimic_seq/test_2', 'whole_org')
#print 'many_delete', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/many_delete_1_99_trained', '../Data/mimic_seq/test_2', 'many_delete_1')
#print 'many_delete', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/many_delete_2_99_trained', '../Data/mimic_seq/test_2', 'many_delete_2')
#print 'many_deletes_pro_1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/proTran1_d_s_c_l_p_80', '../Data/mimic_seq/test_2', 'many_deletes_pro_1')
#print 'many_deletes_pro_2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/proTran2_d_s_c_l_p_80', '../Data/mimic_seq/test_2', 'many_deletes_pro_2')
#print 'many_deletes_mds2_1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/results/mds_ver2_99_80_p1', '../Data/mimic_seq/test_2', 'many_deletes_mds2_1')
#print 'many_deletes_mds2_2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/results/mds_ver2_99_80_p2', '../Data/mimic_seq/test_2', 'many_deletes_mds2_2')
#print 'many_deletes_nmds0_1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/results/nmds_ver0_99_80_p1', '../Data/mimic_seq/test_2', 'many_deletes_nmds0_1')
#print 'many_deletes_nmds0_2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/results/nmds_ver0_99_80_p2', '../Data/mimic_seq/test_2', 'many_deletes_nmds0_2')
#print 'many_deletes_nmds2_1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/results/nmds_ver2_99_80_p1', '../Data/mimic_seq/test_2', 'many_deletes_nmds2_1')
#print 'many_deletes_nmds2_2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/results/nmds_ver2_99_80_p2', '../Data/mimic_seq/test_2', 'many_deletes_nmds2_2')

#print 'whole_org_mtv1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv1/mtv1_whole_trained', '../Data/mimic_seq/test_1', 'whole_org_mtv1')
#print 'many_delete_first40_mtv1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv1/many_deletes/cut_first40/many_delete_1_99_trained', '../Data/mimic_seq/test_1', 'many_delete_1_first40_mtv1')
#print 'many_delete_first40_mtv1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv1/many_deletes/cut_first40/many_delete_2_99_trained', '../Data/mimic_seq/test_1', 'many_delete_2_first40_mtv1')
#print 'many_deletes_pro_1_first40_mtv1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv1/many_deletes/cut_first40/proTran1_d_s_c_l_p_80', '../Data/mimic_seq/test_1', 'many_deletes_pro_1_first40_mtv1')
#print 'many_deletes_pro_2_first40_mtv1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv1/many_deletes/cut_first40/proTran2_d_s_c_l_p_80', '../Data/mimic_seq/test_1', 'many_deletes_pro_2_first40_mtv1')
#print 'many_deletes_mds2_1_first40_mtv1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv1/many_deletes/cut_first40/results/mds_ver2_99_80_p1', '../Data/mimic_seq/test_1', 'many_deletes_mds2_1_first40_mtv1')
#print 'many_deletes_mds2_2_first40_mtv1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv1/many_deletes/cut_first40/results/mds_ver2_99_80_p2', '../Data/mimic_seq/test_1', 'many_deletes_mds2_2_first40_mtv1')
#print 'many_deletes_nmds0_1_first40_mtv1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv1/many_deletes/cut_first40/results/nmds_ver0_99_80_p1', '../Data/mimic_seq/test_1', 'many_deletes_nmds0_1_first40_mtv1')
#print 'many_deletes_nmds0_2_first40_mtv1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv1/many_deletes/cut_first40/results/nmds_ver0_99_80_p2', '../Data/mimic_seq/test_1', 'many_deletes_nmds0_2_first40_mtv1')
#print 'many_deletes_nmds2_1_first40_mtv1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv1/many_deletes/cut_first40/results/nmds_ver2_99_80_p1', '../Data/mimic_seq/test_1', 'many_deletes_nmds2_1_first40_mtv1')
#print 'many_deletes_nmds2_2_first40_mtv1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv1/many_deletes/cut_first40/results/nmds_ver2_99_80_p2', '../Data/mimic_seq/test_1', 'many_deletes_nmds2_2_first40_mtv1')
#print 'many_deletes_smooth_nmds2_1_first40_mtv1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv1/many_deletes/cut_first40/results/smooth_nmds_ver2_99_80_p1', '../Data/mimic_seq/test_1', 'many_deletes_smooth_nmds2_1_first40_mtv1')
#print 'many_deletes_smooth_nmds2_2_first40_mtv1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv1/many_deletes/cut_first40/results/smooth_nmds_ver2_99_80_p2', '../Data/mimic_seq/test_1', 'many_deletes_smooth_nmds2_2_first40_mtv1')


#print '20_org', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/80_20/trainv_2_20_2_trained', '../Data/mimic_seq/test_2', '20_org')
##print 'F20_org', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/JH_fused/org_p1', '../Data/mimic_seq/test_2', 'F20_org')
#print 'F20_pro', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/JH_fused/proTran_comb_d_s_c_l_p_100R_p2', '../Data/mimic_seq/test_2', 'F20_pro')
#print 'F20_mds1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/JH_fused/mds_ver1_100_p2', '../Data/mimic_seq/test_2', 'F20_mds1')
#print 'F20_mds2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/JH_fused/mds_ver2_100_p2', '../Data/mimic_seq/test_2', 'F20_mds2')
#print 'F20_nmds0', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/JH_fused/nmds_ver0_100_p2', '../Data/mimic_seq/test_2', 'F20_nmds0')
#print 'F20_nmds1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/JH_fused/nmds_ver1_100_p2', '../Data/mimic_seq/test_2', 'F20_nmds1')
#print 'F20_nmds2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/JH_fused/reg_nmds_ver2_100_p2', '../Data/mimic_seq/test_2', 'F20_nmds2')
#print 'F20_smooth_nmds2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/JH_fused/smooth_nmds_ver2_100_p2', '../Data/mimic_seq/test_2', 'F20_smooth_nmds2')
#
#print '80_org', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/80_20/trainv_2_80_1_trained', '../Data/mimic_seq/test_2', '80_org')
##print 'F80_org', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/JH_fused/org_p2', '../Data/mimic_seq/test_2', 'F80_org')
#print 'F80_pro', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/JH_fused/proTran_comb_d_s_c_l_p_100R_p1', '../Data/mimic_seq/test_2', 'F80_pro')
#print 'F80_mds1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/JH_fused/mds_ver1_100_p1', '../Data/mimic_seq/test_2', 'F80_mds1')
#print 'F80_mds2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/JH_fused/mds_ver2_100_p1', '../Data/mimic_seq/test_2', 'F80_mds2')
#print 'F80_nmds0', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/JH_fused/nmds_ver0_100_p1', '../Data/mimic_seq/test_2', 'F80_nmds0')
#print 'F80_nmds1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/JH_fused/nmds_ver1_100_p1', '../Data/mimic_seq/test_2', 'F80_nmds1')
#print 'F80_nmds2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/JH_fused/reg_nmds_ver2_100_p1', '../Data/mimic_seq/test_2', 'F80_nmds2')
#print 'F80_smooth_nmds2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/JH_fused/smooth_nmds_ver2_100_p1', '../Data/mimic_seq/test_2', 'F80_smooth_nmds2')


#print 'Fwhole_org', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/mtv2_whole_trained', '../Data/mimic_seq/test_2', 'Fwhole_org')
#print 'Fmany_delete_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/JH_fuse/many_del_f40_org_99_1_p1', '../Data/mimic_seq/test_2', 'Fmany_delete_1_first40')
#print 'Fmany_delete_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/JH_fuse/many_del_f40_org_99_1_p2', '../Data/mimic_seq/test_2', 'Fmany_delete_2_first40')
#print 'Fmany_deletes_pro_1_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/JH_fuse/many_del_f40_pro_99_1_p1', '../Data/mimic_seq/test_2', 'Fmany_deletes_pro_1_first40')
#print 'Fmany_deletes_pro_2_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/JH_fuse/many_del_f40_pro_99_1_p2', '../Data/mimic_seq/test_2', 'Fmany_deletes_pro_2_first40')
#print 'Fmany_deletes_mds2_1_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/JH_fuse/many_del_f40_mds2_99_1_p1', '../Data/mimic_seq/test_2', 'Fmany_deletes_mds2_1_first40')
#print 'Fmany_deletes_mds2_2_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/JH_fuse/many_del_f40_mds2_99_1_p2', '../Data/mimic_seq/test_2', 'Fmany_deletes_mds2_2_first40')
#print 'Fmany_deletes_nmds0_1_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/JH_fuse/many_del_f40_nmds0_99_1_p1', '../Data/mimic_seq/test_2', 'Fmany_deletes_nmds0_1_first40')
#print 'Fmany_deletes_nmds0_2_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/JH_fuse/many_del_f40_nmds0_99_1_p2', '../Data/mimic_seq/test_2', 'Fmany_deletes_nmds0_2_first40')
#print 'Fmany_deletes_nmds2_1_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/JH_fuse/many_del_f40_nmds2_99_1_p1', '../Data/mimic_seq/test_2', 'Fmany_deletes_nmds2_1_first40')
#print 'Fmany_deletes_nmds2_2_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/JH_fuse/many_del_f40_nmds2_99_1_p2', '../Data/mimic_seq/test_2', 'Fmany_deletes_nmds2_2_first40')


#print 'Fwhole_org', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/mtv2_whole_trained', '../Data/mimic_seq/test_2', 'Fwhole_org')
#print 'Fmany_delete', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/many_delete_1_99_trained', '../Data/mimic_seq/test_2', 'Fmany_delete_1')
#print 'Fmany_delete', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/many_delete_2_99_trained', '../Data/mimic_seq/test_2', 'Fmany_delete_2')
#print 'Fmany_deletes_pro_1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/proTran1_d_s_c_l_p_80', '../Data/mimic_seq/test_2', 'Fmany_deletes_pro_1')
#print 'Fmany_deletes_pro_2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/proTran2_d_s_c_l_p_80', '../Data/mimic_seq/test_2', 'Fmany_deletes_pro_2')
#print 'Fmany_deletes_mds2_1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/results/mds_ver2_99_80_p1', '../Data/mimic_seq/test_2', 'Fmany_deletes_mds2_1')
#print 'Fmany_deletes_mds2_2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/results/mds_ver2_99_80_p2', '../Data/mimic_seq/test_2', 'Fmany_deletes_mds2_2')
#print 'Fmany_deletes_nmds0_1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/results/nmds_ver0_99_80_p1', '../Data/mimic_seq/test_2', 'Fmany_deletes_nmds0_1')
#print 'Fmany_deletes_nmds0_2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/results/nmds_ver0_99_80_p2', '../Data/mimic_seq/test_2', 'Fmany_deletes_nmds0_2')
#print 'Fmany_deletes_nmds2_1', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/results/nmds_ver2_99_80_p1', '../Data/mimic_seq/test_2', 'Fmany_deletes_nmds2_1')
#print 'Fmany_deletes_nmds2_2', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/results/nmds_ver2_99_80_p2', '../Data/mimic_seq/test_2', 'Fmany_deletes_nmds2_2')


#print 'whole_org', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/mtv2_whole_trained', '../Data/mimic_seq/test_2', 'whole_org')
#print 'many_delete_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/cut_first40/many_delete_1_100_trained', '../Data/mimic_seq/test_2', 'many_delete_1_100_first40')
#print 'many_delete_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/cut_first40/many_delete_2_100_trained', '../Data/mimic_seq/test_2', 'many_delete_2_100_first40')


#print 'whole_org', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/mtv2_whole_trained', '../Data/mimic_seq/test_2', 'whole_org')
#print 'many_delete_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/cut_first40/many_delete_1_100_trained', '../Data/mimic_seq/test_2', 'many_delete_1_100_first40')
#print 'many_delete_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/cut_first40/many_delete_2_100_trained', '../Data/mimic_seq/test_2', 'many_delete_2_100_first40')
#print 'many_deletes_mds2_1_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/proTran_comb_d_s_c_l_p_70R_p1', '../Data/mimic_seq/test_2', 'many_deletes_mds2_1_first40')
#print 'many_deletes_mds2_2_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/proTran_comb_d_s_c_l_p_70R_p2', '../Data/mimic_seq/test_2', 'many_deletes_mds2_2_first40')
#print 'many_deletes_mds2_1_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/mds_ver2_100_70_p1', '../Data/mimic_seq/test_2', 'many_deletes_mds2_1_first40')
#print 'many_deletes_mds2_2_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/mds_ver2_100_70_p2', '../Data/mimic_seq/test_2', 'many_deletes_mds2_2_first40')
#print 'many_deletes_nmds0_1_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver0_100_70_p1', '../Data/mimic_seq/test_2', 'many_deletes_nmds0_1_first40')
#print 'many_deletes_nmds0_2_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver0_100_70_p2', '../Data/mimic_seq/test_2', 'many_deletes_nmds0_2_first40')
#print 'many_deletes_nmds2_1_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver2_100_70_p1', '../Data/mimic_seq/test_2', 'many_deletes_nmds2_1_first40')
#print 'many_deletes_nmds2_2_first40', prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver2_100_70_p2', '../Data/mimic_seq/test_2', 'many_deletes_nmds2_2_first40')


#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/mtv2_whole_trained', '../Data/mimic_seq/test_2', 'whole_org')
##print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/cut_first40/many_delete_1_100_trained', '../Data/mimic_seq/test_2', 'many_delete_1_100_first40', '_70overlap')
##print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/cut_first40/many_delete_2_100_trained', '../Data/mimic_seq/test_2', 'many_delete_2_100_first40', '_70overlap')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/cut_first40/many_delete_1_100_trained_a', '../Data/mimic_seq/test_2', 'many_delete_1_100_first40', '_70overlap')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/cut_first40/many_delete_2_100_trained_a', '../Data/mimic_seq/test_2', 'many_delete_2_100_first40', '_70overlap')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/proTran_comb_d_s_c_l_p_70R_p1_a', '../Data/mimic_seq/test_2', 'many_deletes_pro_1_100_first40', '_70overlap')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/proTran_comb_d_s_c_l_p_70R_p2_a', '../Data/mimic_seq/test_2', 'many_deletes_pro_2_100_first40', '_70overlap')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/mds_ver2_100_70_p1_a', '../Data/mimic_seq/test_2', 'many_deletes_mds2_1_100_first40', '_70overlap')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/mds_ver2_100_70_p2_a', '../Data/mimic_seq/test_2', 'many_deletes_mds2_2_100_first40', '_70overlap')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver0_100_70_p1_a', '../Data/mimic_seq/test_2', 'many_deletes_nmds0_1_100_first40', '_70overlap')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver0_100_70_p2_a', '../Data/mimic_seq/test_2', 'many_deletes_nmds0_2_100_first40', '_70overlap')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver2_100_70_p1_a', '../Data/mimic_seq/test_2', 'many_deletes_nmds2_1_100_first40', '_70overlap')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver2_100_70_p2_a', '../Data/mimic_seq/test_2', 'many_deletes_nmds2_2_100_first40', '_70overlap')

#
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/mtv2_whole_trained', '../Data/mimic_seq/test_2', 'whole_org')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/cut_first40/many_delete_1_100_trained', '../Data/mimic_seq/test_2', 'many_delete_1_100_first40', '_70overlap')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/cut_first40/many_delete_2_100_trained', '../Data/mimic_seq/test_2', 'many_delete_2_100_first40', '_70overlap')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/cut_first40/many_delete_1_100_trained_d', '../Data/mimic_seq/test_2', 'many_delete_1_100_first40', '_70overlap_d')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/cut_first40/many_delete_2_100_trained_d', '../Data/mimic_seq/test_2', 'many_delete_2_100_first40', '_70overlap_d')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/proTran_comb_d_s_c_l_p_70R_p1_d', '../Data/mimic_seq/test_2', 'many_deletes_pro_1_100_first40', '_70overlap_d')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/proTran_comb_d_s_c_l_p_70R_p2_d', '../Data/mimic_seq/test_2', 'many_deletes_pro_2_100_first40', '_70overlap_d')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/mds_ver2_100_70_p1_d', '../Data/mimic_seq/test_2', 'many_deletes_mds2_1_100_first40', '_70overlap_d')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/mds_ver2_100_70_p2_d', '../Data/mimic_seq/test_2', 'many_deletes_mds2_2_100_first40', '_70overlap_d')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver0_100_70_p1_d', '../Data/mimic_seq/test_2', 'many_deletes_nmds0_1_100_first40', '_70overlap_d')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver0_100_70_p2_d', '../Data/mimic_seq/test_2', 'many_deletes_nmds0_2_100_first40', '_70overlap_d')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver2_100_70_p1_d', '../Data/mimic_seq/test_2', 'many_deletes_nmds2_1_100_first40', '_70overlap_d')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver2_100_70_p2_d', '../Data/mimic_seq/test_2', 'many_deletes_nmds2_2_100_first40', '_70overlap_d')


#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/mtv2_whole_trained', '../Data/mimic_seq/test_2', 'test_whole_org')


#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/mtv2_whole_trained', '../Data/mimic_seq/test_2', 'whole_org_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/cut_first40/many_delete_1_100_trained', '../Data/mimic_seq/test_2', 'many_delete_1_100_first40', '_70overlap_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/cut_first40/many_delete_2_100_trained', '../Data/mimic_seq/test_2', 'many_delete_2_100_first40', '_70overlap_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/cut_first40/many_delete_1_100_trained_d', '../Data/mimic_seq/test_2', 'many_delete_1_100_first40', '_70overlap_d_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/cut_first40/many_delete_2_100_trained_d', '../Data/mimic_seq/test_2', 'many_delete_2_100_first40', '_70overlap_d_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/proTran_comb_d_s_c_l_p_70R_p1_d', '../Data/mimic_seq/test_2', 'many_deletes_pro_1_100_first40', '_70overlap_d_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/proTran_comb_d_s_c_l_p_70R_p2_d', '../Data/mimic_seq/test_2', 'many_deletes_pro_2_100_first40', '_70overlap_d_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/mds_ver2_100_70_p1_d', '../Data/mimic_seq/test_2', 'many_deletes_mds2_1_100_first40', '_70overlap_d_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/mds_ver2_100_70_p2_d', '../Data/mimic_seq/test_2', 'many_deletes_mds2_2_100_first40', '_70overlap_d_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver0_100_70_p1_d', '../Data/mimic_seq/test_2', 'many_deletes_nmds0_1_100_first40', '_70overlap_d_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver0_100_70_p2_d', '../Data/mimic_seq/test_2', 'many_deletes_nmds0_2_100_first40', '_70overlap_d_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver2_100_70_p1_d', '../Data/mimic_seq/test_2', 'many_deletes_nmds2_1_100_first40', '_70overlap_d_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver2_100_70_p2_d', '../Data/mimic_seq/test_2', 'many_deletes_nmds2_2_100_first40', '_70overlap_d_pred1')


#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/mtv2_whole_trained', '../Data/mimic_seq/test_2', '')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/cut_first40/many_delete_1_99_trained', '../Data/mimic_seq/test_2', 'many_delete_1_99_first40', '')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/cut_first40/many_delete_2_99_trained', '../Data/mimic_seq/test_2', 'many_delete_2_99_first40', '')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/proTran_comb_d_s_c_l_p_80R_p1', '../Data/mimic_seq/test_2', 'many_deletes_pro_1_99_first40', '')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/proTran_comb_d_s_c_l_p_80R_p2', '../Data/mimic_seq/test_2', 'many_deletes_pro_2_99_first40', '')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/mds_ver2_99_80_p1', '../Data/mimic_seq/test_2', 'many_deletes_mds2_1_99_first40', '')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/mds_ver2_99_80_p2', '../Data/mimic_seq/test_2', 'many_deletes_mds2_2_99_first40', '')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver0_99_80_p1', '../Data/mimic_seq/test_2', 'many_deletes_nmds0_1_99_first40', '')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver0_99_80_p2', '../Data/mimic_seq/test_2', 'many_deletes_nmds0_2_99_first40', '')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver2_99_80_p1', '../Data/mimic_seq/test_2', 'many_deletes_nmds2_1_99_first40', '')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver2_99_80_p2', '../Data/mimic_seq/test_2', 'many_deletes_nmds2_2_99_first40', '')


#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/mtv2_whole_trained', '../Data/mimic_seq/test_2', 'org_whole', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/cut_first40/many_delete_1_99_trained', '../Data/mimic_seq/test_2', 'many_delete_1_99_first40', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/many_deletes/cut_first40/many_delete_2_99_trained', '../Data/mimic_seq/test_2', 'many_delete_2_99_first40', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/proTran_comb_d_s_c_l_p_80R_p1', '../Data/mimic_seq/test_2', 'many_deletes_pro_1_99_first40', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/proTran_comb_d_s_c_l_p_80R_p2', '../Data/mimic_seq/test_2', 'many_deletes_pro_2_99_first40', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/mds_ver2_99_80_p1', '../Data/mimic_seq/test_2', 'many_deletes_mds2_1_99_first40', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/mds_ver2_99_80_p2', '../Data/mimic_seq/test_2', 'many_deletes_mds2_2_99_first40', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver0_99_80_p1', '../Data/mimic_seq/test_2', 'many_deletes_nmds0_1_99_first40', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver0_99_80_p2', '../Data/mimic_seq/test_2', 'many_deletes_nmds0_2_99_first40', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver2_99_80_p1', '../Data/mimic_seq/test_2', 'many_deletes_nmds2_1_99_first40', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver2_99_80_p2', '../Data/mimic_seq/test_2', 'many_deletes_nmds2_2_99_first40', '_pred1')


#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver2_99_80_p1', '../Data/mimic_seq/test_2', 'many_deletes_nmds2_1_99_first40', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_first40/results/nmds_ver2_99_80_p2', '../Data/mimic_seq/test_2', 'many_deletes_nmds2_2_99_first40', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/Shuang/results/nmds_ver2_99_80_p1', '../Data/mimic_seq/test_2', 'many_deletes_nmds2_1_99_first40', '_shuang_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/Shuang/results/nmds_ver2_99_80_p2', '../Data/mimic_seq/test_2', 'many_deletes_nmds2_2_99_first40', '_shuang_pred1')

##################################################rep 1##################################################
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_1_trained', '../Data/mimic_seq/test_1', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_1_50_many_delete_1_100_trained_d', '../Data/mimic_seq/test_1', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_1_50_many_delete_2_100_trained_d', '../Data/mimic_seq/test_1', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_1_proTran1_d_s_c_l_p_70_d', '../Data/mimic_seq/test_1', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_1_proTran2_d_s_c_l_p_70_d', '../Data/mimic_seq/test_1', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t1_nmds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_1', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t1_nmds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_1', '_pred0')
###################################################rep 1##################################################
#
#
###################################################rep 3##################################################
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_3_trained', '../Data/mimic_seq/test_3', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_3_50_many_delete_1_100_trained_d', '../Data/mimic_seq/test_3', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_3_50_many_delete_2_100_trained_d', '../Data/mimic_seq/test_3', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_3_proTran1_d_s_c_l_p_70_d', '../Data/mimic_seq/test_3', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_3_proTran2_d_s_c_l_p_70_d', '../Data/mimic_seq/test_3', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t3_nmds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_3', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t3_nmds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_3', '_pred0')
#####################################################################################################
#
#
###################################################rep 4##################################################
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_4_trained', '../Data/mimic_seq/test_4', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_4_50_many_delete_1_100_trained_d', '../Data/mimic_seq/test_4', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_4_50_many_delete_2_100_trained_d', '../Data/mimic_seq/test_4', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_4_proTran1_d_s_c_l_p_70_d', '../Data/mimic_seq/test_4', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_4_proTran2_d_s_c_l_p_70_d', '../Data/mimic_seq/test_4', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t4_nmds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_4', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t4_nmds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_4', '_pred0')
#####################################################################################################
#
################mds reps#####################################################################################
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t1_mds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_1', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t3_mds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_3', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t4_mds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_4', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t1_mds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_1', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t3_mds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_3', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t4_mds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_4', '_pred0')
################mds reps#####################################################################################



#################################################rep 0##################################################
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_0_trained', '../Data/mimic_seq/test_0', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_0_50_many_delete_1_100_trained_d', '../Data/mimic_seq/test_0', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_0_50_many_delete_2_100_trained_d', '../Data/mimic_seq/test_0', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_0_proTran1_d_s_c_l_p_70_d', '../Data/mimic_seq/test_0', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_0_proTran2_d_s_c_l_p_70_d', '../Data/mimic_seq/test_0', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t0_mds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_0', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t0_mds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_0', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t0_nmds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_0', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t0_nmds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_0', '_pred0')
#####################################################################################################
#
#
###################################################rep 5##################################################
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_5_trained', '../Data/mimic_seq/test_5', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_5_50_many_delete_1_100_trained_d', '../Data/mimic_seq/test_5', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_5_50_many_delete_2_100_trained_d', '../Data/mimic_seq/test_5', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_5_proTran1_d_s_c_l_p_70_d', '../Data/mimic_seq/test_5', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_5_proTran2_d_s_c_l_p_70_d', '../Data/mimic_seq/test_5', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t5_mds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_5', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t5_mds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_5', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t5_nmds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_5', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t5_nmds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_5', '_pred0')
#####################################################################################################
#
###################################################rep 8##################################################
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_8_trained', '../Data/mimic_seq/test_8', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_8_50_many_delete_1_100_trained_d', '../Data/mimic_seq/test_8', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_8_50_many_delete_2_100_trained_d', '../Data/mimic_seq/test_8', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_8_proTran1_d_s_c_l_p_70_d', '../Data/mimic_seq/test_8', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_8_proTran2_d_s_c_l_p_70_d', '../Data/mimic_seq/test_8', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t8_mds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_8', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t8_mds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_8', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t8_nmds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_8', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t8_nmds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_8', '_pred0')
#####################################################################################################
#
#
###################################################rep 9##################################################
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_9_trained', '../Data/mimic_seq/test_9', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_9_50_many_delete_1_100_trained_d', '../Data/mimic_seq/test_9', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_9_50_many_delete_2_100_trained_d', '../Data/mimic_seq/test_9', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_9_proTran1_d_s_c_l_p_70_d', '../Data/mimic_seq/test_9', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_9_proTran2_d_s_c_l_p_70_d', '../Data/mimic_seq/test_9', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t9_mds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_9', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t9_mds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_9', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t9_nmds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_9', '_pred0')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t9_nmds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_9', '_pred0')
#####################################################################################################
#
#
#
##################################################rep 0##################################################
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_0_trained', '../Data/mimic_seq/test_0', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_0_50_many_delete_1_100_trained_d', '../Data/mimic_seq/test_0', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_0_50_many_delete_2_100_trained_d', '../Data/mimic_seq/test_0', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_0_proTran1_d_s_c_l_p_70_d', '../Data/mimic_seq/test_0', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_0_proTran2_d_s_c_l_p_70_d', '../Data/mimic_seq/test_0', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t0_mds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_0', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t0_mds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_0', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t0_nmds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_0', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t0_nmds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_0', '_pred1')
#####################################################################################################
#
#
###################################################rep 5##################################################
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_5_trained', '../Data/mimic_seq/test_5', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_5_50_many_delete_1_100_trained_d', '../Data/mimic_seq/test_5', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_5_50_many_delete_2_100_trained_d', '../Data/mimic_seq/test_5', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_5_proTran1_d_s_c_l_p_70_d', '../Data/mimic_seq/test_5', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_5_proTran2_d_s_c_l_p_70_d', '../Data/mimic_seq/test_5', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t5_mds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_5', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t5_mds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_5', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t5_nmds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_5', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t5_nmds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_5', '_pred1')
#####################################################################################################
#

###################################################rep 6##################################################
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_6_trained', '../Data/mimic_seq/test_6', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_6_50_many_delete_1_100_trained_d', '../Data/mimic_seq/test_6', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_6_50_many_delete_2_100_trained_d', '../Data/mimic_seq/test_6', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_6_proTran1_d_s_c_l_p_70_d', '../Data/mimic_seq/test_6', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_6_proTran2_d_s_c_l_p_70_d', '../Data/mimic_seq/test_6', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t6_mds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_6', '_pred1')
##print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t6_mds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_6', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/70overlap/t6_nmds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_6', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/70overlap/t6_nmds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_6', '_pred1')
#####################################################################################################
#
#
###################################################rep 7##################################################
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_7_trained', '../Data/mimic_seq/test_7', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_7_50_many_delete_1_100_trained_d', '../Data/mimic_seq/test_7', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_7_50_many_delete_2_100_trained_d', '../Data/mimic_seq/test_7', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_7_proTran1_d_s_c_l_p_70_d', '../Data/mimic_seq/test_7', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_7_proTran2_d_s_c_l_p_70_d', '../Data/mimic_seq/test_7', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t7_mds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_7', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t7_mds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_7', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/70overlap/t7_nmds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_7', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/70overlap/t7_nmds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_7', '_pred1')
######################################################################################################
#
####################################################rep 8##################################################
##print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_8_trained', '../Data/mimic_seq/test_8', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_8_50_many_delete_1_100_trained_d', '../Data/mimic_seq/test_8', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_8_50_many_delete_2_100_trained_d', '../Data/mimic_seq/test_8', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_8_proTran1_d_s_c_l_p_70_d', '../Data/mimic_seq/test_8', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_8_proTran2_d_s_c_l_p_70_d', '../Data/mimic_seq/test_8', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t8_mds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_8', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t8_mds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_8', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t8_nmds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_8', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t8_nmds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_8', '_pred1')
#####################################################################################################
#
#
###################################################rep 9##################################################
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_9_trained', '../Data/mimic_seq/test_9', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_9_50_many_delete_1_100_trained_d', '../Data/mimic_seq/test_9', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_9_50_many_delete_2_100_trained_d', '../Data/mimic_seq/test_9', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_9_proTran1_d_s_c_l_p_70_d', '../Data/mimic_seq/test_9', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_9_proTran2_d_s_c_l_p_70_d', '../Data/mimic_seq/test_9', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t9_mds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_9', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t9_mds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_9', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t9_nmds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_9', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t9_nmds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_9', '_pred1')
####################################################################################################


##################################################rep 9##################################################
#print test_prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_9_trained', '../Data/mimic_seq/test_9', '_pred1_test')
#print test_prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_9_50_many_delete_1_100_trained_d', '../Data/mimic_seq/test_9', '_pred1_test')
#print test_prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_9_50_many_delete_2_100_trained_d', '../Data/mimic_seq/test_9', '_pred1_test')
#print test_prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_9_proTran1_d_s_c_l_p_70_d', '../Data/mimic_seq/test_9', '_pred1_test')
#print test_prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_9_proTran2_d_s_c_l_p_70_d', '../Data/mimic_seq/test_9', '_pred1_test')
#print test_prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t9_mds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_9', '_pred1_test')
#print test_prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/mds2_results/t9_mds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_9', '_pred1_test')
#print test_prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t9_nmds_ver2_100d_70d_p1_d', '../Data/mimic_seq/test_9', '_pred1_test')
#print test_prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t9_nmds_ver2_100d_70d_p2_d', '../Data/mimic_seq/test_9', '_pred1_test')
###################################################################################################


#print test_prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_2_trained', '../Data/mimic_seq/test_2', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/proTran1_d_s_c_l_p_50', '../Data/mimic_seq/test_2', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/proTran2_d_s_c_l_p_50', '../Data/mimic_seq/test_2', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/mds_ver2_50_p1', '../Data/mimic_seq/test_2', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/mds_ver2_50_p2', '../Data/mimic_seq/test_2', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/nmds_ver0_50_p1', '../Data/mimic_seq/test_2', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/nmds_ver0_50_p2', '../Data/mimic_seq/test_2', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/smooth_nmds_ver2_50_p1', '../Data/mimic_seq/test_2', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/smooth_nmds_ver2_50_p2', '../Data/mimic_seq/test_2', '_pred1')


#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/results/mds_ver2_100_p1', '../Data/mimic_seq/test_2', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/results/mds_ver2_100_p2', '../Data/mimic_seq/test_2', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/results/nmds_ver0_100_p1', '../Data/mimic_seq/test_2', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/results/nmds_ver0_100_p2', '../Data/mimic_seq/test_2', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/results/reg_nmds_ver2_100_p1', '../Data/mimic_seq/test_2', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/results/reg_nmds_ver2_100_p2', '../Data/mimic_seq/test_2', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/results/smooth_nmds_ver2_100_p1', '../Data/mimic_seq/test_2', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/results/smooth_nmds_ver2_100_p2', '../Data/mimic_seq/test_2', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/proTran1_d_s_c_l_p_100', '../Data/mimic_seq/test_2', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/proTran2_d_s_c_l_p_100', '../Data/mimic_seq/test_2', '_pred1')


#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/JH_fused/many_deletes_nmds2_99_1_p1', '../Data/mimic_seq/test_2', '_F_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/JH_fused/many_deletes_nmds2_99_1_p2', '../Data/mimic_seq/test_2', '_F_pred1')


#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_2_80_1_many_delete_100_trained_d', '../Data/mimic_seq/test_2', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/cut_data/trainv_2_20_2_many_delete_100_trained_d', '../Data/mimic_seq/test_2', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_2_80_proTran1_d_s_c_l_p_40_d', '../Data/mimic_seq/test_2', '_pred1')
#print prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_2_20_proTran2_d_s_c_l_p_40_d', '../Data/mimic_seq/test_2', '_pred1')


#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_2_trained', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_2_95_proTran1_d_s_c_l_p_40', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/results/t2_nmds_ver2_noCut_95_5_40o_p1', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_2_5_2proTran2_d_s_c_l_p_40', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/results/t2_nmds_ver2_noCut_95_5_40o_p2', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_2_95_proTran1_d_s_c_l_p_70', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/results/t2_nmds_ver2_noCut_95_5_70o_p1', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_2_5_2proTran2_d_s_c_l_p_70', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/results/t2_nmds_ver2_noCut_95_5_70o_p2', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_2_95_proTran1_d_s_c_l_p_100', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/results/t2_nmds_ver2_noCut_95_5_100o_p1', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_2_5_2proTran2_d_s_c_l_p_100', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/results/t2_nmds_ver2_noCut_95_5_100o_p2', '../Data/mimic_seq/test_2', '')



#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_2_trained', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/proTran1_d_s_c_l_p_50', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/proTran2_d_s_c_l_p_50', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/mds_ver2_50_p1', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/mds_ver2_50_p2', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/nmds_ver0_50_p1', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/nmds_ver0_50_p2', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/smooth_nmds_ver2_50_p1', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/80_20/results/smooth_nmds_ver2_50_p2', '../Data/mimic_seq/test_2', '')
#
#
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_2_trained', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/proTran1_d_s_c_l_p_100', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/proTran2_d_s_c_l_p_100', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/results/mds_ver2_100_p1', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/results/mds_ver2_100_p2', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/results/nmds_ver0_100_p1', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/results/nmds_ver0_100_p2', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/results/reg_nmds_ver2_100_p1', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/results/reg_nmds_ver2_100_p2', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/results/smooth_nmds_ver2_100_p1', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/imbalanced/90_10/results/smooth_nmds_ver2_100_p2', '../Data/mimic_seq/test_2', '')


#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t2_nmds_ver2_noCut_95_5_40o_p1', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/org_tran_method/results/t2_nmds_ver2_noCut_95_5_40o_p2', '../Data/mimic_seq/test_2', '')
#
#
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_2_95_proTran1_d_s_c_l_p_40', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/pro_tran/trainv_2_5_2proTran2_d_s_c_l_p_40', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/results/t2_nmds_ver2_noCut_95_5_40o_p1', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/nmds2/results/t2_nmds_ver2_noCut_95_5_40o_p2', '../Data/mimic_seq/test_2', '')


#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/50_50/trainv_2_50_1_trained', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/SequentialPhenotypePredictor/Prediction/nmdsExp_mtv2/50_50/trainv_2_50_2_trained', '../Data/mimic_seq/test_2', '')


#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_2_trained', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/50_50/trainv_0_50_1_trained', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/50_50/trainv_0_50_2_trained', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/50_50/trainv_1_50_1_trained', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/50_50/trainv_1_50_2_trained', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/50_50/trainv_2_50_1_trained', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/50_50/trainv_2_50_2_trained', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/50_50/trainv_3_50_1_trained', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/50_50/trainv_3_50_2_trained', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/50_50/trainv_4_50_1_trained', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/50_50/trainv_4_50_2_trained', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/50_50/trainv_5_50_1_trained', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/50_50/trainv_5_50_2_trained', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/50_50/trainv_6_50_1_trained', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/50_50/trainv_6_50_2_trained', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/50_50/trainv_7_50_1_trained', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/50_50/trainv_7_50_2_trained', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/50_50/trainv_8_50_1_trained', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/50_50/trainv_8_50_2_trained', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/50_50/trainv_9_50_1_trained', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/50_50/trainv_9_50_2_trained', '../Data/mimic_seq/test_2', '')


#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_0_trained', '../Data/mimic_seq/test_0', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_1_trained', '../Data/mimic_seq/test_1', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_2_trained', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_3_trained', '../Data/mimic_seq/test_3', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_4_trained', '../Data/mimic_seq/test_4', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_5_trained', '../Data/mimic_seq/test_5', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_6_trained', '../Data/mimic_seq/test_6', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_7_trained', '../Data/mimic_seq/test_7', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_8_trained', '../Data/mimic_seq/test_8', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/all_codes/data/trainv_9_trained', '../Data/mimic_seq/test_9', '')

#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_second40/proTran1_d_s_c_l_p_80', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_second40/proTran2_d_s_c_l_p_80', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_second40/results/nmds_ver0_99_80_p1', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_second40/results/nmds_ver0_99_80_p2', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_second40/results/nmds_ver2_99_80_p1', '../Data/mimic_seq/test_2', '')
#prediction_pipeline('../Data/mimic_seq/vocab', '/Users/henry/Desktop/mtv2/many_deletes/cut_second40/results/nmds_ver2_99_80_p2', '../Data/mimic_seq/test_2', '')
