Result = [];

for k = 1:fold
    
    k
        
    [trn_s1,tst_s1] = folding(site1,CVO1,k);
    [trn_s2,tst_s2] = folding(site2,CVO2,k);
    
    fname = sprintf('%d_over_%d_Data_fold%d.mat',A,overlap,k)
    
    if exist(fname) ~= 2
        
        if overlap ~= 100
            
            fname = sprintf('over%d.mat',overlap)
            load(fname)
            
            test1 = test_overlap(tst_s1(:,3),event_diff_list,0);
            test1_ans = test_overlap(tst_s1(:,1),event_diff_list,1);
            
            fname = sprintf('%d_over_%d_Data_fold%d.mat',A,100,k) % You should have this file.
            load(fname)
            
            test2 = test;
            test2_ans = test_ans;
            
            train_s1_overlap(trn_s1(:,3),trn_s1(:,4),event_diff_list);
            train_s2(trn_s2(:,3),trn_s2(:,4))
            
            fprintf('Start w2v!!!!!')
            
            system('python W2V.py')
            
            [data1_list,data1] = import_tv('train_s1_overlap_w2v.txt');
            [data2_list,data2] = import_tv('train_s2_w2v.txt');
            
        elseif overlap == 100
            
            test = tst_s1(:,3);
            test_ans = tst_s1(:,1);
            
            for i=1:size(test,1)
                test{i} = strsplit(test{i}, ' ');
            end
            
            for i= 1:size(test_ans,1)
                test_ans{i} = strsplit(test_ans{i}, ',');
            end
            
            test1 = test;
            test1_ans = test_ans;
            
            test2 = test;
            test2_ans = test_ans;
            
            train_s1_nonoverlap(trn_s1(:,3),trn_s1(:,4));
            train_s2(trn_s2(:,3),trn_s2(:,4));
            
            fprintf('Start w2v!!!!!')
            
            system('python W2V.py')
            
            [data1_list,data1] = import_tv('train_s1_overlap_w2v.txt');
            [data2_list,data2] = import_tv('train_s2_w2v.txt');
            
        end
        
        fname = sprintf('%d_over_%d_Data_fold%d.mat',A,overlap,k)
        save(fname,'data1_list','data1','data2_list','data2','test','test_ans')
        
        delete('train_nonoverlap.txt','train_s1_overlap_w2v.txt','train_overlap.txt','train_s2_w2v.txt')
    else
        load(fname)
    end
       
    %% alignment
    
    fname = sprintf('%d_over_%d_%s_Align_Data_fold%d.mat',A,overlap,align,k);
    
    if exist(fname) ~= 2
        
        fac = 350;
        
        if strcmp(align,'pro')
            [d1,d2,d1_list,d2_list,num] = procrustes_tv(data1,data2,data1_list,data2_list);
        elseif strcmp(align,'no')
            [d1,d2,data1_list,data2_list] = Ordering(data1,data2,data1_list,data2_list);
            num = sum(ismember(data1_list,data2_list));
            d1_list = data1_list;
            d2_list = data2_list;
        end
        
        fname = sprintf('%d_over_%d_%s_Align_Data_fold%d.mat',A,overlap,align,k)
        save(fname,'d1_list','d1','d2_list','d2')
        
    else
        load(fname)
    end

    %% fusion

    num = sum(ismember(d1_list,d2_list));
    
    if fusion
        
        a = ratio;
        b = 1-ratio;
        
        new_dia = a*d1(1:num,:)+b*d2(1:num,:);
        
        d1 = [new_dia;d1(num+1:end,:)];
        d2 = [new_dia;d2(num+1:end,:)];
        
        [d1,d2] = new_ev(d1,d2,1,num,0.5,0.5);
        
    end
    
    %% patient vector (tst)
    
    fname = sprintf('%d_over_%d_%s_PV_fold%d.mat',A,overlap,align,k);
    
    if exist(fname)~=2
        
        decay = 8;
        pa_vec1 = PDPS_PV2(decay,test1,d1,d2,d1_list,d2_list,0);
        pa_vec2 = PDPS_PV2(decay,test2,d2,d1,d2_list,d1_list,0);
        
        fname = sprintf('%d_over_%d_%s_PV_fold%d.mat',A,overlap,align,k)
        save(fname,'pa_vec1','pa_vec2')
    else
        load(fname)
    end
    
    %% Prediction - PDPS
    
    fname = sprintf('%d_over_%d_%s_AUC_fold%d.mat',A,overlap,align,k,fold);
    
    if exist(fname)~=2
        
        [a1,AUC1] = Probability2(d1,d1_list,pa_vec1,test1_ans);
        [a4,AUC4] = Probability2(d2,d2_list,pa_vec2,test2_ans);
        
        a = [a1,a4]';
        AUC = [AUC1;AUC4];
        
        Local = [mean(AUC,2),AUC]
        fname = sprintf('%d_over_%d_%s_AUC_fold%d.mat',A,overlap,align,k)
        save(fname,'Local','a')
        
    else
        load(fname) 
    end
    
    Result = [Result,mean(AUC,2)]
   
end

Final_Result = [mean(Result,2),Result];
