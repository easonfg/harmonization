function [data1_new,data2_new] = Procrustes3(data1,data2,data1_list,data2_list)

%% Orthogonal Procurstes Analysis

% only shared data

X = data1(ismember(data1_list,data2_list),:);
Y = data2(ismember(data2_list,data1_list),:);

[~,~,transform] = procrustes(X,Y,'scaling',false);

c = transform.c;
T = transform.T;
b = transform.b;

%% Validation

% whole data

data1_new = data1;
data2_new = b*data2*T+repmat(c(1,:),[size(data2,1),1]);

end

