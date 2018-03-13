function [total_trn,total_tst] = folding(total,CVO,fold)


%% CV

total_trn = total(CVO.training(fold),:);
total_tst = total(CVO.test(fold),:);


end

