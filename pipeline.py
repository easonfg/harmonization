from create_model_and_prediction.create_models import *
from create_model_and_prediction.pipeline_create_procrustes import *
from create_model_and_prediction.prediction_pipeline import *

########################################split 3 sites##############################
for i in range(0,10):
    # train whole data
    create_model('data/vocab', 'data/trainv_' + str(i))
    # train three 1/3 of the whole data
    create_model('data/vocab', 'data/3sites/trainv_' + str(i) + '_1')
    create_model('data/vocab', 'data/3sites/trainv_' + str(i) + '_2')
    create_model('data/vocab', 'data/3sites/trainv_' + str(i) + '_3')








results = []
for i in range(0,10):
    results.append(prediction_pipeline('two_sites/3sites/vocab_site1', 'two_sites/3sites/train_sets/trainv_' + str(i) + '_1_trained_m', 'two_sites/3sites/test_sets/test_' + str(i) + '_site1', ''))
    results.append(prediction_pipeline('two_sites/3sites/vocab_site2', 'two_sites/3sites/train_sets/trainv_' + str(i) + '_2_trained_m', 'two_sites/3sites/test_sets/test_' + str(i) + '_site2', ''))
    results.append(prediction_pipeline('two_sites/3sites/vocab_site3', 'two_sites/3sites/train_sets/trainv_' + str(i) + '_3_trained_m', 'two_sites/3sites/test_sets/test_' + str(i) + '_site3', ''))
    results.append(prediction_pipeline('two_sites/3sites/vocab_all1', 'two_sites/3sites/train_sets/trainv_' + str(i) +  '_comb', 'two_sites/3sites/test_sets/test_' + str(i) + '_site1', ''))
    results.append(prediction_pipeline('two_sites/3sites/vocab_all2', 'two_sites/3sites/train_sets/trainv_' + str(i) +  '_comb', 'two_sites/3sites/test_sets/test_' + str(i) + '_site2', ''))
    results.append(prediction_pipeline('two_sites/3sites/vocab_all3', 'two_sites/3sites/train_sets/trainv_' + str(i) +  '_comb', 'two_sites/3sites/test_sets/test_' + str(i) + '_site3', ''))


with open('org_pdps1.csv', 'w') as f:
    f.write('\n'.join(results))

results = []
for i in range(0,10):
    results.append(prediction_pipeline('vocab', 'data/trainv_' + str(i) + '_trained', 'data/test_' + str(i) + '', ''))


with open('whole_all_pdps1.csv', 'w') as f:
    f.write('\n'.join(results))

results = []
for i in range(0,10):
    results.append(prediction_pipeline('two_sites/3sites/vocab_site1', 'pro_tran/JH_pro/3sites/org_350dim/10o/trainv_' + str(i) + '_1_trained_m_proTran', 'two_sites/3sites/test_sets/test_' + str(i) + '_site1', ''))
    results.append(prediction_pipeline('two_sites/3sites/vocab_site2', 'pro_tran/JH_pro/3sites/org_350dim/10o/trainv_' + str(i) + '_2_trained_m_proTran', 'two_sites/3sites/test_sets/test_' + str(i) + '_site2', ''))
    results.append(prediction_pipeline('two_sites/3sites/vocab_site3', 'pro_tran/JH_pro/3sites/org_350dim/10o/trainv_' + str(i) + '_3_trained_m_proTran', 'two_sites/3sites/test_sets/test_' + str(i) + '_site3', ''))
    results.append(prediction_pipeline('two_sites/3sites/vocab_all1', 'pro_tran/JH_pro/3sites/org_350dim/10o/trainv_' + str(i) + '_comb_proTran', 'two_sites/3sites/test_sets/test_' + str(i) + '_site1', '_10o'))
    results.append(prediction_pipeline('two_sites/3sites/vocab_all2', 'pro_tran/JH_pro/3sites/org_350dim/10o/trainv_' + str(i) + '_comb_proTran', 'two_sites/3sites/test_sets/test_' + str(i) + '_site2', '_10o'))
    results.append(prediction_pipeline('two_sites/3sites/vocab_all3', 'pro_tran/JH_pro/3sites/org_350dim/10o/trainv_' + str(i) + '_comb_proTran', 'two_sites/3sites/test_sets/test_' + str(i) + '_site3', '_10o'))
#
with open('pro_10o_pdps1.csv', 'w') as f:
    f.write('\n'.join(results))



results = []
for i in range(0,10):
    results.append(prediction_pipeline('two_sites/3sites/vocab_all1', 'pro_tran/JH_pro/3sites/org_350dim/40o/trainv_' + str(i) + '_comb_proTran', 'two_sites/3sites/test_sets/test_' + str(i) + '_site1', '_40o'))
    results.append(prediction_pipeline('two_sites/3sites/vocab_all2', 'pro_tran/JH_pro/3sites/org_350dim/40o/trainv_' + str(i) + '_comb_proTran', 'two_sites/3sites/test_sets/test_' + str(i) + '_site2', '_40o'))
    results.append(prediction_pipeline('two_sites/3sites/vocab_all3', 'pro_tran/JH_pro/3sites/org_350dim/40o/trainv_' + str(i) + '_comb_proTran', 'two_sites/3sites/test_sets/test_' + str(i) + '_site3', '_40o'))

with open('pro_40o_pdps1.csv', 'w') as f:
    f.write('\n'.join(results))


#        results.append(prediction_pipeline('two_sites/3sites/vocab_all1', 'pro_tran/JH_pro/3sites/org_350dim/70o/trainv_' + str(i) + '_comb_proTran', 'two_sites/3sites/test_sets/test_' + str(i) + '_site1', '_70o'))
#        results.append(prediction_pipeline('two_sites/3sites/vocab_all2', 'pro_tran/JH_pro/3sites/org_350dim/70o/trainv_' + str(i) + '_comb_proTran', 'two_sites/3sites/test_sets/test_' + str(i) + '_site2', '_70o'))
#        results.append(prediction_pipeline('two_sites/3sites/vocab_all3', 'pro_tran/JH_pro/3sites/org_350dim/70o/trainv_' + str(i) + '_comb_proTran', 'two_sites/3sites/test_sets/test_' + str(i) + '_site3', '_70o'))
#
#

