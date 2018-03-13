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
        #topN2 = [e[0] for e in a.most_similar(diag[:-2], topn = N) ]
        top = set(all_d).intersection(set(topN))
        if diag[:-2] in topN:
        #if diag[:-2] in topN and diag in topN2:
            #print diag
            #print len(top)
            d_ind = topN.index(diag[:-2])
            found_ind.append(d_ind)
            #print d_ind
            #print len(set(topN[:d_ind]).intersection(set(all_d)))
            #print topN
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
#org_sim = Word2Vec.load_word2vec_format('no_overlaps/sim/org_comb')


#org50 = analyze('../nmds2/org_comb')
#po50 = analyze('../nmds2/RproTran_comb')
#nr50 = analyze('../nmds2/nmdsTran/reg_init_NMDS_noW')
#np50 = analyze('../nmds2/nmdsTran/pro_init_NMDS_wW')
#
#org = analyze('../exp_20_80/org_comb')
#p = analyze('../exp_20_80/proTran_comb')
#n = analyze('../exp_20_80/nmdsTran/NMDS_20_80')

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


#o50 = analyze('../nmdsExp_mtv0/50_50/org_comb')
#p50 = analyze('../nmdsExp_mtv0/50_50/proTran_comb')


#nnW50 = analyze('../nmdsExp_mtv0/50_50/nmds_50_noW')
#nwW50 = analyze('../nmdsExp_mtv0/50_50/nmds_50_wW')
#nwuW50 = analyze('../nmdsExp_mtv0/50_50/nmds_50_wUniW')
#nw101W50 = analyze('../nmdsExp_mtv0/50_50/nmds_50_w_10_1_W')
#nwcW50 = analyze('../nmdsExp_mtv0/50_50/nmds_50_w_cat_1_W')
#niW50 = analyze('../nmdsExp_mtv0/50_50/nmds_50_w_inc_W')
#n5ABW50 = analyze('../nmdsExp_mtv0/50_50/nmds_50_w_5AB_W')
#n1ABW50 = analyze('../nmdsExp_mtv0/50_50/nmds_50_w_1AB_W')
#n3ABW50 = analyze('../nmdsExp_mtv0/50_50/nmds_50_w_3AB_W')
#n7ABW50 = analyze('../nmdsExp_mtv0/50_50/nmds_50_w_7AB_W')
#n7ABW80 = analyze('../nmdsExp_mtv0/80_20/nmds_80_20_w_7AB_W')
#n7ABW90 = analyze('../nmdsExp_mtv0/90_10/nmds_90_10_w_7AB_W')


#nnW501 = analyze('../nmdsExp_mtv1/50_50/nmds_50_noW')
#nwW501 = analyze('../nmdsExp_mtv1/50_50/nmds_50_wW')
#nwuW501 = analyze('../nmdsExp_mtv1/50_50/nmds_50_wUniW')
#nw101W501 = analyze('../nmdsExp_mtv1/50_50/nmds_50_w_10_1_W')
#nwcW501 = analyze('../nmdsExp_mtv1/50_50/nmds_50_w_cat_1_W')
#niW501 = analyze('../nmdsExp_mtv1/50_50/nmds_50_w_inc_W')
#n5ABW51 = analyze('../nmdsExp_mtv1/50_50/nmds_50_w_5AB_W')
#n1ABW51 = analyze('../nmdsExp_mtv1/50_50/nmds_50_w_1AB_W')
#n3ABW51 = analyze('../nmdsExp_mtv1/50_50/nmds_50_w_3AB_W')
#n7ABW51 = analyze('../nmdsExp_mtv1/50_50/nmds_50_w_7AB_W')

#n7ABW801 = analyze('../nmdsExp_mtv1/80_20/nmds_80_20_w_7AB_W')
#n7ABW901 = analyze('../nmdsExp_mtv1/90_10/nmds_90_10_w_7AB_W')


#nnW502 = analyze('../nmdsExp_mtv2/50_50/nmds_50_noW')
#n7ABW502 = analyze('../nmdsExp_mtv2/50_50/nmds_50_w_7AB_W')
#n7ABW802 = analyze('../nmdsExp_mtv2/80_20/nmds_80_20_w_7AB_W')
#n7ABW902 = analyze('../nmdsExp_mtv2/90_10/nmds_90_10_w_7AB_W')

#nnW500 = analyze('../nmdsExp_mtv0/50_50/nmds_50_noW')
##nnW800 = analyze('../nmdsExp_mtv0/80_20/nmds_80_20_noW')
##nnW900 = analyze('../nmdsExp_mtv0/90_10/nmds_90_10_noW')
##
#nnW501 = analyze('../nmdsExp_mtv1/50_50/nmds_50_noW')
##nnW801 = analyze('../nmdsExp_mtv1/80_20/nmds_80_20_noW')
##nnW901 = analyze('../nmdsExp_mtv1/90_10/nmds_90_10_noW')
##
#nnW502 = analyze('../nmdsExp_mtv2/50_50/nmds_50_noW')
##nnW802 = analyze('../nmdsExp_mtv2/80_20/nmds_80_20_noW')
##nnW902 = analyze('../nmdsExp_mtv2/90_10/nmds_90_10_noW')



#nnW80 = analyze('../nmdsExp_mtv0/80_20/nmds_80_20_noW')
#nwW80 = analyze('../nmdsExp_mtv0/80_20/nmds_80_20_wW')
#nnW90 = analyze('../nmdsExp_mtv0/90_10/nmds_90_10_noW')
#nwW90 = analyze('../nmdsExp_mtv0/90_10/nmds_90_10_wW')
#
#nnW801 = analyze('../nmdsExp_mtv1/80_20/nmds_80_20_noW')
#nwW801 = analyze('../nmdsExp_mtv1/80_20/nmds_80_20_wW')
#nnW901 = analyze('../nmdsExp_mtv1/90_10/nmds_90_10_noW')
#nwW901 = analyze('../nmdsExp_mtv1/90_10/nmds_90_10_wW')
#
#nnW802 = analyze('../nmdsExp_mtv2/80_20/nmds_80_20_noW')
#nwW802 = analyze('../nmdsExp_mtv2/80_20/nmds_80_20_wW')
#nnW902 = analyze('../nmdsExp_mtv2/90_10/nmds_90_10_noW')
#nwW902 = analyze('../nmdsExp_mtv2/90_10/nmds_90_10_wW')

#o504 = analyze('../nmdsExp_mtv4/50_50/org_comb')
#p504 = analyze('../nmdsExp_mtv4/50_50/proTran_comb')
#nnW504 = analyze('../nmdsExp_mtv4/50_50/nmds_50_noW')
#n7ABW504 = analyze('../nmdsExp_mtv4/50_50/nmds_50_w_7AB_W')

#t0 = analyze('../nmdsExp_mtv0/50_50/nmds_50_wW_tenthDiags')
#q0 = analyze('../nmdsExp_mtv0/50_50/nmds_50_wW_25Diags')
#h1 = analyze('../nmdsExp_mtv1/50_50/nmds_50_wW_halfDiags')
#q1 = analyze('../nmdsExp_mtv1/50_50/nmds_50_wW_qDiags')
#t1 = analyze('../nmdsExp_mtv1/50_50/nmds_50_wW_tenthDiags')

#h2 = analyze('../nmdsExp_mtv2/50_50/nmds_50_wW_halfDiags')
#q2 = analyze('../nmdsExp_mtv2/50_50/nmds_50_wW_qDiags')
#t2 = analyze('../nmdsExp_mtv2/50_50/nmds_50_wW_tenthDiags')
#
#h3 = analyze('../nmdsExp_mtv3/50_50/nmds_50_wW_halfDiags')
#q3 = analyze('../nmdsExp_mtv3/50_50/nmds_50_wW_qDiags')
#t3 = analyze('../nmdsExp_mtv3/50_50/nmds_50_wW_tenthDiags')
#
#h4 = analyze('../nmdsExp_mtv4/50_50/nmds_50_wW_halfDiags')
#q4 = analyze('../nmdsExp_mtv4/50_50/nmds_50_wW_qDiags')
#t4 = analyze('../nmdsExp_mtv4/50_50/nmds_50_wW_tenthDiags')


#ver0 = analyze('../nmdsExp_mtv0/50_50/ver0_mtv0')
#ver0 = analyze('../nmdsExp_mtv0/50_50/ver1_mtv0')
#ver1 = analyze('../nmdsExp_mtv0/50_50/ver1_iter1')
#ver2 = analyze('../nmdsExp_mtv0/50_50/ver2_iter1')
#ver2_iter10 = analyze('../nmdsExp_mtv0/50_50/ver2_iter10')

#ver0_iter0 = analyze('../nmdsExp_mtv0/50_50/old_method/ver0_iter0')
#ver0_iter10 = analyze('../nmdsExp_mtv0/50_50/old_method/ver0_iter10')
#ver0_iter6 = analyze('../nmdsExp_mtv0/50_50/old_method/ver0_iter6')

ver0_iter0 = analyze('../nmdsExp_mtv0/50_50/new_method_JH/ver0_iter0')
ver0_iter1 = analyze('../nmdsExp_mtv0/50_50/new_method_JH/ver0_iter1')
ver1_iter0 = analyze('../nmdsExp_mtv0/50_50/new_method_JH/ver1_iter0')
ver1_iter1 = analyze('../nmdsExp_mtv0/50_50/new_method_JH/ver1_iter1')
ver1_iter2 = analyze('../nmdsExp_mtv0/50_50/new_method_JH/ver1_iter2')
ver2_iter0 = analyze('../nmdsExp_mtv0/50_50/new_method_JH/ver2_iter0')
ver2_iter1 = analyze('../nmdsExp_mtv0/50_50/new_method_JH/ver2_iter1')

#ver0_iter0_H = analyze('../nmdsExp_mtv0/50_50/new_method/ver0_iter0_H')
#ver0_iter10 = analyze('../nmdsExp_mtv0/50_50/new_method/ver0_iter10')
#ver0_iter30 = analyze('../nmdsExp_mtv0/50_50/new_method/ver0_iter30')
#ver1_iter10 = analyze('../nmdsExp_mtv0/50_50/new_method/ver1_iter10')
#ver1_iter30 = analyze('../nmdsExp_mtv0/50_50/new_method/ver1_iter30')
#ver2_iter0 = analyze('../nmdsExp_mtv0/50_50/new_method/ver2_iter0')
#ver2_iter10 = analyze('../nmdsExp_mtv0/50_50/new_method/ver2_iter10')
#mds0 = analyze('../nmdsExp_mtv0/50_50/mds_50')


def catCount(L, cat):
    sub = [event for event in L if event.startswith(cat)]
    print len(sub)
    return sub

def intersect(model, cat):
    o1d = [d for d in model.vocab.keys() if d.startswith(cat) and not d.endswith('_m')]
    o2d = [d[:-2] for d in model.vocab.keys() if d.startswith(cat) and d.endswith('_m')]
    inter = set(o1d).intersection(set(o2d))
    return inter

#count the same neighbors
def neighbor_difference(ls, model, n):
    final = []
    for each in ls:
        s1 = set([e[0] for e in model.most_similar(each, topn = n)])
        s2 = set([e[0][:-2] for e in model.most_similar(each+'_m', topn = n)])
        final.append(len(s1.intersection(s2)) * 1.0/(2*n))

    return sum(final) * 1.0/len(ls)


# count the number of other categories in neigbors
def company(ls, model, cat, n):
    final = []
    for each in ls:
        s1 = set([e[0] for e in model.most_similar(each, topn = n) if not e[0].startswith(cat)])
        s2 = set([e[0][:-2] for e in model.most_similar(each+'_m', topn = n) if not e[0].startswith(cat)])
        final.append( (len(s1) + len(s2)) * 1.0/(2*n))

    return sum(final) * 1.0/len(ls)


