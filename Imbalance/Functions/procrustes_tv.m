function [data1_new,data2_new,data1_list,data2_list,num] = procrustes_tv(data1,data2,data1_list,data2_list)

[data1,data2,data1_list,data2_list] = Ordering(data1,data2,data1_list,data2_list);

num = sum(ismember(data1_list,data2_list));

[data1_new,data2_new] = Procrustes3(data1,data2,data1_list,data2_list);

end

