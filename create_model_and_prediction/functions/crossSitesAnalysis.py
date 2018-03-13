from gensim.models import Word2Vec


def analyze(model):

    a = Word2Vec.load_word2vec_format(model)
    #d1 = [d for d in a.vocab.keys() if d.startswith('d') and not d.endswith('m')]
    #d2 = [d for d in a.vocab.keys() if d.startswith('d') and d.endswith('m')]
    d1 = [d for d in a.vocab.keys() if not d.endswith('m')]
    d2 = [d for d in a.vocab.keys() if d.endswith('m')]
    all_d = d1 + d2

    pure_d2 = [d[:-2] for d in d2]
    corr_diag = set(d1).intersection(set(pure_d2))

    cd2 = [e for e in d2 if e[:-2] in d1]

    #N = 2000
    N = len(all_d)
    count = 0
    found_ind = []
    not_found = []
    perfect = []
    top10 = []
    top50 = []
    top100 = []
    top200 = []
    top300 = []
    top400 = []
    top500 = []
    gt500 = []

    for diag in cd2:
        #import pdb; pdb.set_trace()
        #topN = [e[0] for e in a.most_similar(diag, topn = N) if e[0].startswith('d')]
        topN = [e[0] for e in a.most_similar(diag, topn = N) ]
        topN = [i for i in topN if not i.endswith('_m')]
        top = set(all_d).intersection(set(topN))
        if diag[:-2] in topN:
            #print diag
            #print len(top)
            d_ind = topN.index(diag[:-2])
            found_ind.append(d_ind)
            #print d_ind
            #print len(set(topN[:d_ind]).intersection(set(all_d)))
            #print topN[:10]
            count += 1
        else:
            not_found.append(diag)


        if topN.index(diag[:-2]) == 0:
            perfect.append(diag[:-2])
        if topN.index(diag[:-2]) <= 10:
            top10.append(diag[:-2])
        if topN.index(diag[:-2]) <= 50:
            top50.append(diag[:-2])
        if topN.index(diag[:-2]) <= 100:
            top100.append(diag[:-2])
        if topN.index(diag[:-2]) <= 200:
            top200.append(diag[:-2])
        if topN.index(diag[:-2]) <= 300:
            top300.append(diag[:-2])
        if topN.index(diag[:-2]) <= 400:
            top400.append(diag[:-2])
        if topN.index(diag[:-2]) <= 500:
            top500.append(diag[:-2])
        if topN.index(diag[:-2]) > 500:
            gt500.append(diag[:-2])



    print 'not_found', not_found
    print 'found', count
    print 'total', len(corr_diag)
    print 'percentage', count*1.0/len(corr_diag)
    print 'found index', found_ind
    print 'perfect', perfect


    first = sum(0 == x for x in found_ind)
    to10 = sum(0 < x <= 10 for x in found_ind)
    to50 = sum(10 < x <= 50 for x in found_ind)
    to100 = sum(50 < x <= 100 for x in found_ind)
    to200 = sum(100 < x <= 200 for x in found_ind)
    to300 = sum(200 < x <= 300 for x in found_ind)
    to400 = sum(300 < x <= 400 for x in found_ind)
    to500 = sum(400 < x <= 500 for x in found_ind)
    to600 = sum(500 < x <= 600 for x in found_ind)
    to700 = sum(600 < x <= 700 for x in found_ind)
    to800 = sum(700 < x <= 800 for x in found_ind)
    to900 = sum(800 < x <= 900 for x in found_ind)
    gt900 = sum(900 < x for x in found_ind)


    results = [first, to10, to50, to100, to200, to300, to400, to500, to600, to700, to800, to900, gt900]
    return [results, perfect, top10, top50, top100, top200, top300, top400, top500, gt500]

#proTran = Word2Vec.load_word2vec_format('RproTran_comb')
#geoTran = Word2Vec.load_word2vec_format('geo_tran/geoTran_comb')
#nmds_dw = Word2Vec.load_word2vec_format('witholds/just_diag/nmdsTran_dw')
#nmdsTran_dw_sim = Word2Vec.load_word2vec_format('sim/just_diag/nmdsTran_w_sim')
#proTran_dw_sim = Word2Vec.load_word2vec_format('sim/just_diag/proTran_sim_d')
#proTran_exp = Word2Vec.load_word2vec_format('sim12_comb')



#proTran_sim = Word2Vec.load_word2vec_format('no_overlaps/sim/Wsim_proTran_comb')
#rps, pps, t10ps, t50ps, t100ps = analyze(proTran_sim)
#
#org_sim = Word2Vec.load_word2vec_format('no_overlaps/sim/org_comb')
#ros, pos, t10os, t50os, t100os = analyze(org_sim)
#
#
#org50 = analyze('../nmds2/org_comb')
#po50 = analyze('../nmds2/RproTran_comb')
#nr50 = analyze('../nmds2/nmdsTran/reg_init_NMDS_noW')
#np50 = analyze('../nmds2/nmdsTran/pro_init_NMDS_wW')
#
#org = analyze('../exp_20_80/org_comb')
#p = analyze('../exp_20_80/proTran_comb')
#n = analyze('../exp_20_80/nmdsTran/NMDS_20_80')


#o50 = analyze('../nmdsExp_mtv1/50_50/org_comb')
#p50 = analyze('../nmdsExp_mtv1/50_50/proTran_comb')
#nnW50 = analyze('../nmdsExp_mtv1/50_50/nmds_50_noW')
#nwW50 = analyze('../nmdsExp_mtv1/50_50/nmds_50_wW')
#
#o80 = analyze('../nmdsExp_mtv1/80_20/org_comb')
#p80 = analyze('../nmdsExp_mtv1/80_20/proTran_comb')
#nnW80 = analyze('../nmdsExp_mtv1/80_20/nmds_80_20_noW')
#nwW80 = analyze('../nmdsExp_mtv1/80_20/nmds_80_20_wW')
#
#o90 = analyze('../nmdsExp_mtv1/90_10/org_comb')
#p90 = analyze('../nmdsExp_mtv1/90_10/proTran_comb')
#nnW90 = analyze('../nmdsExp_mtv1/90_10/nmds_90_10_noW')
#nwW90 = analyze('../nmdsExp_mtv1/90_10/nmds_90_10_wW')


#o50 = analyze('../nmdsExp_mtv0/50_50/org_comb')
#p50 = analyze('../nmdsExp_mtv0/50_50/proTran_comb')
#nnW50 = analyze('../nmdsExp_mtv0/50_50/nmds_50_noW')
#nwW50 = analyze('../nmdsExp_mtv0/50_50/nmds_50_wW')
#
#
#o80 = analyze('../nmdsExp_mtv0/80_20/org_comb')
#p80 = analyze('../nmdsExp_mtv0/80_20/proTran_comb')
#nnW80 = analyze('../nmdsExp_mtv0/80_20/nmds_80_20_noW')
#nwW80 = analyze('../nmdsExp_mtv0/80_20/nmds_80_20_wW')
#
#o90 = analyze('../nmdsExp_mtv0/90_10/org_comb')
#p90 = analyze('../nmdsExp_mtv0/90_10/proTran_comb')
#nnW90 = analyze('../nmdsExp_mtv0/90_10/nmds_90_10_noW')
#nwW90 = analyze('../nmdsExp_mtv0/90_10/nmds_90_10_wW')


#nnW50 = analyze('../nmdsExp_mtv0/50_50/nmds_50_noW')
#nwW50 = analyze('../nmdsExp_mtv0/50_50/nmds_50_w_7AB_W')
#
#nnW501 = analyze('../nmdsExp_mtv1/50_50/nmds_50_noW')
#nwW501 = analyze('../nmdsExp_mtv1/50_50/nmds_50_w_7AB_W')

#o50 = analyze('../nmdsExp_mtv3/50_50/org_comb')
#p50 = analyze('../nmdsExp_mtv3/50_50/proTran_comb')
#nnW502 = analyze('../nmdsExp_mtv3/50_50/nmds_50_noW')
#n7ABW502 = analyze('../nmdsExp_mtv3/50_50/nmds_50_w_7AB_W')

#o50 = analyze('../nmdsExp_mtv4/50_50/org_comb')
#p50 = analyze('../nmdsExp_mtv4/50_50/proTran_comb')
#nnW502 = analyze('../nmdsExp_mtv4/50_50/nmds_50_noW')
#n7ABW502 = analyze('../nmdsExp_mtv4/50_50/nmds_50_w_7AB_W')
#ver0 = analyze('../nmdsExp_mtv0/50_50/ver0_mtv0')
ver2 = analyze('/Users/Eas/Documents/MATLAB/lsqisotonic_altered/mtv0/results/pro_init_NMDS_wW_1inAB')
ver2_norm = analyze('/Users/Eas/Documents/MATLAB/lsqisotonic_altered/mtv0/results/pro_init_NMDS_proNormalized_wW_1inAB')
smooth_ver2 = analyze('/Users/Eas/Documents/MATLAB/lsqisotonic_altered/mtv0/results/smooth_nmds_proNormalized_ver2')

#nwuW501 = analyze('../nmdsExp_mtv1/50_50/nmds_50_wUniW')
#nw101W501 = analyze('../nmdsExp_mtv1/50_50/nmds_50_w_10_1_W')
#nwcW501 = analyze('../nmdsExp_mtv1/50_50/nmds_50_w_cat_1_W')

#nnW500 = analyze('../nmdsExp_mtv0/50_50/nmds_50_noW')
#nnW800 = analyze('../nmdsExp_mtv0/80_20/nmds_80_20_noW')
#nnW900 = analyze('../nmdsExp_mtv0/90_10/nmds_90_10_noW')
#
#nnW501 = analyze('../nmdsExp_mtv1/50_50/nmds_50_noW')
#nnW801 = analyze('../nmdsExp_mtv1/80_20/nmds_80_20_noW')
#nnW901 = analyze('../nmdsExp_mtv1/90_10/nmds_90_10_noW')
#
#nnW502 = analyze('../nmdsExp_mtv2/50_50/nmds_50_noW')
#nnW802 = analyze('../nmdsExp_mtv2/80_20/nmds_80_20_noW')
#nnW902 = analyze('../nmdsExp_mtv2/90_10/nmds_90_10_noW')


def catCount(L, cat):
    sub = [event for event in L if event.startswith(cat)]
    print len(sub)
    return sub


#p = analyze(proTran)
###b = analyze(geoTran)
#n = analyze(nmdsTran)
##d = analyze(nmds_dw)
#ns = analyze(nmdsTran_dw_sim)
#ps = analyze(proTran_dw_sim)
