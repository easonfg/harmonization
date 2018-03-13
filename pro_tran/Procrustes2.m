function [data1_new,data2_new] = Procrustes3(t1, t2, common_ls)

% Procrustes 1 and 2 are wroted by Junghye Lee, Procrustes 3 is the most
% reliable function to get a result.

%% Orthogonal Procurstes Analysis

% only shared data

% X = data1(ismember(data1_list,data2_list),:);
% Y = data2(ismember(data2_list,data1_list),:);
% X = data1(common_ls1, :);
% Y = data2(common_ls2, :);
X = table2array(sortrows(t1(common_ls, :), 'RowNames'));
Y = table2array(sortrows(t2(common_ls, :), 'RowNames'));

[~,~,transform] = procrustes(X,Y,'scaling',false);

c = transform.c;
T = transform.T;
b = transform.b;

%% Validation

% whole data

% data1_new = data1;
% data2_new = b*data2*T+repmat(c(1,:),[size(data2,1),1]);
data1_new = table2array(t1);
data2 = table2array(t2);
data2_new = b*data2*T+repmat(c(1,:),[size(data2,1),1]);
end


