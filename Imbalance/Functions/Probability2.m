function [final_dia1_list,AUC] = Probability2(d1,d1_list,pa_vec1,test_ans)

ind = strncmpi(d1_list, 'd_', 2);
dia1_list = d1_list(ind);
new_dia1 = d1(ind, :);

load('common.mat')
final_dia1_list = dia1_list(ismember(dia1_list,common));
final_dia1 = new_dia1(ismember(dia1_list,common),:);

label = [];
for i=1:size(test_ans,1)
    label = [label;ismember(final_dia1_list,test_ans{i})'];
end

S1 = squareform(pdist([final_dia1;pa_vec1],'cosine'));
S1 = S1(1:size(final_dia1,1),size(final_dia1,1)+1:end)';
predict1 = 1-S1;

for i=1:size(label,2)
    if sum(label(:,i) == 0) == size(label,1)
        AUC(i) = 0;
    else
        [~,~,~,AUC(i)] = perfcurve(label(:,i),predict1(:,i),1);
    end
    i
end

end

