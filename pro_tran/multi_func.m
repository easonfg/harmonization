
%%%%%% pro org 350 dimension%%%%
%%%%10 percent overlaps
%for i =0:9
%  procrustes_tv_3sites(char(strcat('../../../two_sites/3sites/train_sets/trainv_', num2str(i), '_1_trained_m')), ...
%                       char(strcat('../../../two_sites/3sites/train_sets/trainv_', num2str(i), '_2_trained_m')), ...
%                       char(strcat('../../../two_sites/3sites/train_sets/trainv_', num2str(i), '_3_trained_m')),10, 350, 'org_350dim/10o/');
%end


%%%%70 percent overlaps
for i =0:9
  procrustes_tv_3sites(char(strcat('../../../two_sites/3sites/train_sets/trainv_', num2str(i), '_1_trained_m')), ...
                       char(strcat('../../../two_sites/3sites/train_sets/trainv_', num2str(i), '_2_trained_m')), ...
                       char(strcat('../../../two_sites/3sites/train_sets/trainv_', num2str(i), '_3_trained_m')),70, 350, 'org_350dim/70o/');
end


%%%%40 percent overlaps
%for i =0:9
%  procrustes_tv_3sites(char(strcat('../../../two_sites/3sites/train_sets/trainv_', num2str(i), '_1_trained_m')), ...
%                       char(strcat('../../../two_sites/3sites/train_sets/trainv_', num2str(i), '_2_trained_m')), ...
%                       char(strcat('../../../two_sites/3sites/train_sets/trainv_', num2str(i), '_3_trained_m')),40, 350, 'org_350dim/40o/');
%end
