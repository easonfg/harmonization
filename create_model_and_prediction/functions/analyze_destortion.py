from gensim.models import Word2Vec

#o1 = Word2Vec.load_word2vec_format('m0_20_1')
#o2 = Word2Vec.load_word2vec_format('m0_20_2')
##
#p1 = Word2Vec.load_word2vec_format('pro_m1')
#p2 = Word2Vec.load_word2vec_format('pro_m2')
##
###RIn1 = Word2Vec.load_word2vec_format('nmdsTran/regI_nmdsnoW1')
###RIn2 = Word2Vec.load_word2vec_format('nmdsTran/regI_nmdsnoW2')
##m1 = Word2Vec.load_word2vec_format('../nmds/geo_tran/m1_geoTran')
##m2 = Word2Vec.load_word2vec_format('../nmds/geo_tran/m2_geoTran')
##
#PIn1 = Word2Vec.load_word2vec_format('nmdsTran/proI_nmdswW1')
#PIn2 = Word2Vec.load_word2vec_format('nmdsTran/proI_nmdswW2')
#
#ow1 = Word2Vec.load_word2vec_format('../mimic_models/mtv0_100_1')
#ow2 = Word2Vec.load_word2vec_format('../mimic_models/mtv0_100_2')



def distortion(model, org):

    range =  [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 3000]
    results = []
    model = Word2Vec.load_word2vec_format(model)
    org = Word2Vec.load_word2vec_format(org)
    range.append(len(model.vocab))

    for n in range:
        result = 0
        for modelw in model.vocab.keys():
            result += ((len(set([e1[0] for e1 in model.most_similar(modelw, topn = n)]).intersection(set([ow1[0] for ow1 in org.most_similar(modelw, topn = n)]))) *1.0))/n

        results.append( 1-result/len(model.vocab.keys()))
    return results

#whole = distortion('../mimic_models/mtv0_100_1', '../mimic_models/mtv0_100_2', n)
#o1 = distortion('../nmds2/m0_20_1', '../mimic_models/mtv0_100_1', n)
#o2 = distortion('../nmds2/m0_20_2', '../mimic_models/mtv0_100_1', n)
#n1 = distortion('../nmds2/nmdsTran/proI_nmdswW1', '../mimic_models/mtv0_100_1')
#n2 = distortion('../nmds2/nmdsTran/proI_nmdswW2', '../mimic_models/mtv0_100_1')
##
##o20p = distortion('../exp_20_80/mtv0_20p', '../mimic_models/mtv0_100_1', n)
##o80p = distortion('../exp_20_80/mtv0_80p', '../mimic_models/mtv0_100_1', n)
#
#
#no1 = distortion('../nmds2/nmdsTran/regI_nmdsnoW1', '../mimic_models/mtv0_100_1')
#no2 = distortion('../nmds2/nmdsTran/regI_nmdsnoW2', '../mimic_models/mtv0_100_1')


#o1 = distortion('../nmdsExp_mtv0/50_50/trainv_0_50_1_trained', '../nmdsExp_mtv0/mtv0_whole_trained')
#o2 = distortion('../nmdsExp_mtv0/50_50/trainv_0_50_2_trained', '../nmdsExp_mtv0/mtv0_whole_trained')


#nmds50nW1 = distortion('../nmdsExp_mtv0/50_50/nmds_50_noW_p1', '../nmdsExp_mtv0/mtv0_whole_trained')
#nmds50nW2 = distortion('../nmdsExp_mtv0/50_50/nmds_50_noW_p2', '../nmdsExp_mtv0/mtv0_whole_trained')
#
#nmds50wW1 = distortion('../nmdsExp_mtv0/50_50/nmds_50_wW_p1', '../nmdsExp_mtv0/mtv0_whole_trained')
#nmds50wW2 = distortion('../nmdsExp_mtv0/50_50/nmds_50_wW_p2', '../nmdsExp_mtv0/mtv0_whole_trained')
#
#

#o80_1 = distortion('../nmdsExp_mtv0/80_20/trainv_0_80_1_trained', '../nmdsExp_mtv0/mtv0_whole_trained')
#o80_2 = distortion('../nmdsExp_mtv0/80_20/trainv_0_20_2_trained', '../nmdsExp_mtv0/mtv0_whole_trained')

#nmds80nW1 = distortion('../nmdsExp_mtv0/80_20/nmds_80_20_noW_p1', '../nmdsExp_mtv0/mtv0_whole_trained')
#nmds80nW2 = distortion('../nmdsExp_mtv0/80_20/nmds_80_20_noW_p2', '../nmdsExp_mtv0/mtv0_whole_trained')
#
#nmds80wW1 = distortion('../nmdsExp_mtv0/80_20/nmds_80_20_wW_p1', '../nmdsExp_mtv0/mtv0_whole_trained')
#nmds80wW2 = distortion('../nmdsExp_mtv0/80_20/nmds_80_20_wW_p2', '../nmdsExp_mtv0/mtv0_whole_trained')
#
#
#o90_1 = distortion('../nmdsExp_mtv0/90_10/trainv_0_90_1_trained', '../nmdsExp_mtv0/mtv0_whole_trained')
#o90_2 = distortion('../nmdsExp_mtv0/90_10/trainv_0_10_2_trained', '../nmdsExp_mtv0/mtv0_whole_trained')
#nmds90nW1 = distortion('../nmdsExp_mtv0/90_10/nmds_90_10_noW_p1', '../nmdsExp_mtv0/mtv0_whole_trained')
#nmds90nW2 = distortion('../nmdsExp_mtv0/90_10/nmds_90_10_noW_p2', '../nmdsExp_mtv0/mtv0_whole_trained')
#
#nmds90wW1 = distortion('../nmdsExp_mtv0/90_10/nmds_90_10_wW_p1', '../nmdsExp_mtv0/mtv0_whole_trained')
#nmds90wW2 = distortion('../nmdsExp_mtv0/90_10/nmds_90_10_wW_p2', '../nmdsExp_mtv0/mtv0_whole_trained')



#nmds50wW0_half_1 = distortion('../nmdsExp_mtv0/50_50/nmds_50_wW_halfDiags_p1', '../nmdsExp_mtv0/mtv0_whole_trained')
#nmds50wW0_half_2 = distortion('../nmdsExp_mtv0/50_50/nmds_50_wW_halfDiags_p2', '../nmdsExp_mtv0/mtv0_whole_trained')
#nmds50wW0_q_1 = distortion('../nmdsExp_mtv0/50_50/nmds_50_wW_25Diags_p1', '../nmdsExp_mtv0/mtv0_whole_trained')
#nmds50wW0_q_2 = distortion('../nmdsExp_mtv0/50_50/nmds_50_wW_25Diags_p2', '../nmdsExp_mtv0/mtv0_whole_trained')
#nmds50wW0_t_1 = distortion('../nmdsExp_mtv0/50_50/nmds_50_wW_tenthDiags_p1', '../nmdsExp_mtv0/mtv0_whole_trained')
#nmds50wW0_t_2 = distortion('../nmdsExp_mtv0/50_50/nmds_50_wW_tenthDiags_p2', '../nmdsExp_mtv0/mtv0_whole_trained')
#


#mtv1_org1 = distortion('../nmdsExp_mtv1/50_50/trainv_1_50_1_trained', '../nmdsExp_mtv1/mtv1_whole_trained')
#mtv1_org2 = distortion('../nmdsExp_mtv1/50_50/trainv_1_50_2_trained', '../nmdsExp_mtv1/mtv1_whole_trained')
#nmds50wW1_whole1 = distortion('../nmdsExp_mtv1/50_50/nmds_50_w_7AB_W_p1', '../nmdsExp_mtv1/mtv1_whole_trained')
#nmds50wW1_whole2 = distortion('../nmdsExp_mtv1/50_50/nmds_50_w_7AB_W_p2', '../nmdsExp_mtv1/mtv1_whole_trained')
#nmds50wW1_h_1 = distortion('../nmdsExp_mtv1/50_50/nmds_50_wW_halfDiags_p1', '../nmdsExp_mtv1/mtv1_whole_trained')
#nmds50wW1_h_2 = distortion('../nmdsExp_mtv1/50_50/nmds_50_wW_halfDiags_p2', '../nmdsExp_mtv1/mtv1_whole_trained')
#nmds50wW1_q_1 = distortion('../nmdsExp_mtv1/50_50/nmds_50_wW_qDiags_p1', '../nmdsExp_mtv1/mtv1_whole_trained')
#nmds50wW1_q_2 = distortion('../nmdsExp_mtv1/50_50/nmds_50_wW_qDiags_p2', '../nmdsExp_mtv1/mtv1_whole_trained')
#nmds50wW1_t_1 = distortion('../nmdsExp_mtv1/50_50/nmds_50_wW_tenthDiags_p1', '../nmdsExp_mtv1/mtv1_whole_trained')
#nmds50wW1_t_2 = distortion('../nmdsExp_mtv1/50_50/nmds_50_wW_tenthDiags_p2', '../nmdsExp_mtv1/mtv1_whole_trained')


#mtv2_org1 = distortion('../nmdsExp_mtv2/50_50/trainv_2_50_1_trained', '../nmdsExp_mtv2/mtv2_whole_trained')
#mtv2_org2 = distortion('../nmdsExp_mtv2/50_50/trainv_2_50_2_trained', '../nmdsExp_mtv2/mtv2_whole_trained')
#nmds50wW2_whole1 = distortion('../nmdsExp_mtv2/50_50/nmds_50_w_7AB_W_p1', '../nmdsExp_mtv2/mtv2_whole_trained')
#nmds50wW2_whole2 = distortion('../nmdsExp_mtv2/50_50/nmds_50_w_7AB_W_p2', '../nmdsExp_mtv2/mtv2_whole_trained')
#nmds50wW2_h_1 = distortion('../nmdsExp_mtv2/50_50/nmds_50_wW_halfDiags_p1', '../nmdsExp_mtv2/mtv2_whole_trained')
#nmds50wW2_h_2 = distortion('../nmdsExp_mtv2/50_50/nmds_50_wW_halfDiags_p2', '../nmdsExp_mtv2/mtv2_whole_trained')
#nmds50wW2_q_1 = distortion('../nmdsExp_mtv2/50_50/nmds_50_wW_qDiags_p1', '../nmdsExp_mtv2/mtv2_whole_trained')
#nmds50wW2_q_2 = distortion('../nmdsExp_mtv2/50_50/nmds_50_wW_qDiags_p2', '../nmdsExp_mtv2/mtv2_whole_trained')
#nmds50wW2_t_1 = distortion('../nmdsExp_mtv2/50_50/nmds_50_wW_tenthDiags_p1', '../nmdsExp_mtv2/mtv2_whole_trained')
#nmds50wW2_t_2 = distortion('../nmdsExp_mtv2/50_50/nmds_50_wW_tenthDiags_p2', '../nmdsExp_mtv2/mtv2_whole_trained')
#
#mtv3_org1 = distortion('../nmdsExp_mtv3/50_50/trainv_3_50_1_trained', '../nmdsExp_mtv3/mtv3_whole_trained')
#mtv3_org2 = distortion('../nmdsExp_mtv3/50_50/trainv_3_50_2_trained', '../nmdsExp_mtv3/mtv3_whole_trained')
#nmds50wW3_whole1 = distortion('../nmdsExp_mtv3/50_50/nmds_50_w_7AB_W_p1', '../nmdsExp_mtv3/mtv3_whole_trained')
#nmds50wW3_whole2 = distortion('../nmdsExp_mtv3/50_50/nmds_50_w_7AB_W_p2', '../nmdsExp_mtv3/mtv3_whole_trained')
#nmds50wW3_h_1 = distortion('../nmdsExp_mtv3/50_50/nmds_50_wW_halfDiags_p1', '../nmdsExp_mtv3/mtv3_whole_trained')
#nmds50wW3_h_2 = distortion('../nmdsExp_mtv3/50_50/nmds_50_wW_halfDiags_p2', '../nmdsExp_mtv3/mtv3_whole_trained')
#nmds50wW3_q_1 = distortion('../nmdsExp_mtv3/50_50/nmds_50_wW_qDiags_p1', '../nmdsExp_mtv3/mtv3_whole_trained')
#nmds50wW3_q_2 = distortion('../nmdsExp_mtv3/50_50/nmds_50_wW_qDiags_p2', '../nmdsExp_mtv3/mtv3_whole_trained')
#nmds50wW3_t_1 = distortion('../nmdsExp_mtv3/50_50/nmds_50_wW_tenthDiags_p1', '../nmdsExp_mtv3/mtv3_whole_trained')
#nmds50wW3_t_2 = distortion('../nmdsExp_mtv3/50_50/nmds_50_wW_tenthDiags_p2', '../nmdsExp_mtv3/mtv3_whole_trained')
#
#mtv4_org1 = distortion('../nmdsExp_mtv4/50_50/trainv_4_50_1_trained', '../nmdsExp_mtv4/mtv4_whole_trained')
#mtv4_org2 = distortion('../nmdsExp_mtv4/50_50/trainv_4_50_2_trained', '../nmdsExp_mtv4/mtv4_whole_trained')
#nmds50wW4_whole1 = distortion('../nmdsExp_mtv4/50_50/nmds_50_w_7AB_W_p1', '../nmdsExp_mtv4/mtv4_whole_trained')
#nmds50wW4_whole2 = distortion('../nmdsExp_mtv4/50_50/nmds_50_w_7AB_W_p2', '../nmdsExp_mtv4/mtv4_whole_trained')
#nmds50wW4_h_1 = distortion('../nmdsExp_mtv4/50_50/nmds_50_wW_halfDiags_p1', '../nmdsExp_mtv4/mtv4_whole_trained')
#nmds50wW4_h_2 = distortion('../nmdsExp_mtv4/50_50/nmds_50_wW_halfDiags_p2', '../nmdsExp_mtv4/mtv4_whole_trained')
#nmds50wW4_q_1 = distortion('../nmdsExp_mtv4/50_50/nmds_50_wW_qDiags_p1', '../nmdsExp_mtv4/mtv4_whole_trained')
#nmds50wW4_q_2 = distortion('../nmdsExp_mtv4/50_50/nmds_50_wW_qDiags_p2', '../nmdsExp_mtv4/mtv4_whole_trained')
#nmds50wW4_t_1 = distortion('../nmdsExp_mtv4/50_50/nmds_50_wW_tenthDiags_p1', '../nmdsExp_mtv4/mtv4_whole_trained')
#nmds50wW4_t_2 = distortion('../nmdsExp_mtv4/50_50/nmds_50_wW_tenthDiags_p2', '../nmdsExp_mtv4/mtv4_whole_trained')

ver0_1 = distortion('../nmdsExp_mtv0/50_50/ver0_mtv0_p1', '../nmdsExp_mtv0/mtv0_whole_trained')
ver0_2 = distortion('../nmdsExp_mtv0/50_50/ver0_mtv0_p2', '../nmdsExp_mtv0/mtv0_whole_trained')
