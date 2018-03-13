function [pa_vec1,pa_vec2] = PDPS_PV2(decay,test,d1,d2,d1_list,d2_list,opt)

for i = 1:size(d1_list)
    new_d1(i, :) = d1(i, :)/norm(d1(i, :));
end
% new_d1 = d1;

pa_vec1 = zeros(size(test,1),size(new_d1,2));
for i=1:size(test,1)
    tmp_pa = test{i}; 
    tmp_mtx = [];
    for j=1:length(tmp_pa)
        if sum(ismember(d1_list,tmp_pa{j})) ~= 0
            tmp_ev = new_d1(ismember(d1_list,tmp_pa{j}),:);
            tmp_ev = tmp_ev(1,:); % just in case
            tmp_mtx = [tmp_mtx;tmp_ev*exp(decay*(j-length(tmp_pa))/length(tmp_pa))];
        end
    end
    if length(tmp_mtx)~=0
        pa_vec1(i,:) = mean(tmp_mtx, 1);
        pa_vec1(i,:) = pa_vec1(i,:)/norm(pa_vec1(i,:));
    else
        pa_vec1(i,:) = 0;
    end
    i
end

if opt == 1
    
    for i = 1:size(d2_list)
        new_d2(i, :) = d2(i, :)/norm(d2(i, :));
    end
    
    pa_vec2 = zeros(size(test,1),size(new_d2,2));
    for i=1:size(test,1)
        tmp_pa = test{i}; 
        tmp_mtx = [];
        for j=1:length(tmp_pa)
            if sum(ismember(d2_list,tmp_pa{j})) ~= 0
                tmp_ev = new_d2(ismember(d2_list,tmp_pa{j}),:);
                tmp_ev = tmp_ev(1,:); % just in case
                tmp_mtx = [tmp_mtx;tmp_ev*exp(decay*(j-length(tmp_pa))/length(tmp_pa))];   
            end
        end
        if length(tmp_mtx)~=0
            pa_vec2(i,:) = mean(tmp_mtx, 1);
            pa_vec2(i,:) = pa_vec2(i,:)/norm(pa_vec2(i,:));
        else
            pa_vec2(i,:) = 0;
        end
        i
    end
    
end

end

