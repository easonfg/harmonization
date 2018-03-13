function [T_M_Data,T_U_Data,T_M_list,T_U_list] = Ordering(data1,data2,data1_list,data2_list)

% New ordering

M_I = find(ismember(data1_list,data2_list)==1);
U_I = find(ismember(data2_list,data1_list)==1);
M_C = data1_list(M_I);
U_C = data2_list(U_I);
M_Data = data1(M_I,:);
U_Data = data2(U_I,:);

[M_C, idx_M] = sort(M_C);
[U_C, idx_U] = sort(U_C);

M_Data = M_Data(idx_M,:);
U_Data = U_Data(idx_U,:);

M_r_I = find(ismember(data1_list,data2_list)==0);
U_r_I = find(ismember(data2_list,data1_list)==0);
M_r_C = data1_list(M_r_I);
U_r_C = data2_list(U_r_I);
M_r_Data = data1(M_r_I,:);
U_r_Data = data2(U_r_I,:);

[M_r_C, idx_r_M] = sort(M_r_C);
[U_r_C, idx_r_U] = sort(U_r_C);

M_r_Data = M_r_Data(idx_r_M,:);
U_r_Data = U_r_Data(idx_r_U,:);

T_M_Data = [M_Data;M_r_Data];
T_U_Data = [U_Data;U_r_Data];

T_M_list = [M_C;M_r_C];
T_U_list = [U_C;U_r_C];

end

