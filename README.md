1. go to https://github.com/wael34218/SequentialPhenotypePredictor and follow instruction until you have completed all the 'Data Preparation' steps. by the end you should have training sets and test sets in the data folder.

2. go to folder data/3sites/ and run create_frac_raw_data.py to create 3 sites with suffices and a combine model.

3. to train the whole models and the local models run line 6 - 13 in pipeline.py. This is done with 10-fold cross validation

4. to transform the three sites into a common space, use pro_tran/multi_func.m. It uses procrustes_tv_3sites.m for three sites. procrustes_tv_2sites.m transforms just two sites

5. in order to do prediction for the three sites, new simulated test_sets need to be created. use two_sites/3sites/create_splitSites.py

5. predictions can be ran in pipeline.py again using line 21 and beyond if you want to calculate the AUC.
