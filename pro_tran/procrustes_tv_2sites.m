%function [data1_new,data2_new,data1_list,data2_list,num] = procrustes_tv(data1_dir,data2_dir,data1_list,data2_list)
function [data1_new,data2_new,data1_list,data2_list,num] = procrustes_tv(data1_dir,data2_dir, overlap, out_dir)


t1 = readtable(data1_dir, 'Delimiter', ' ', 'ReadVariableNames', false, 'ReadRowNames', true, 'HeaderLines', 1);
t2 = readtable(data2_dir, 'Delimiter', ' ', 'ReadVariableNames', false, 'ReadRowNames', true, 'HeaderLines', 1);

% data1 = table2array(t1);
% data2 = table2array(t2);
data1_list = t1.Properties.RowNames;
data2_list = t2.Properties.RowNames;
%data1_list = org_data1_list;
%data2_list = org_data2_list;



% if shared == 1
%     for i=1:length(data1_list)
%         if length(findstr(data1_list{i},'d_')) < 1
%             data1_list{i} = strcat(data1_list{i},'_m');
%         end
%     end
% end

%[data1,data2,data1_list,data2_list] = Ordering(data1,data2,data1_list,data2_list);


% common_ind1 = find(ismember(data1_list,data2_list));
% common_ind2 = find(ismember(data2_list,data1_list));
common = data1_list(ismember(data1_list, data2_list));
num = round(sum(ismember(data1_list,data2_list))*overlap/100);
% common_ls1 = datasample(common_ind1, num, 'Replace', false);
% common_ls2 = datasample(common_ind2, num, 'Replace', false);
common_ls = datasample(common, num, 'Replace', false);
[data1_new_tmp,data2_new_tmp] = Procrustes2(t1,t2,common_ls);


common_ls1 = find(ismember(data1_list, common_ls));
common_ls2 = find(ismember(data2_list, common_ls));


rest1 = find(~ismember(data1_list, common_ls));
rest2 = find(~ismember(data2_list, common_ls));


data1_new = vertcat(data1_new_tmp(common_ls1, :), data1_new_tmp(rest1, :));
data2_new = vertcat(data2_new_tmp(common_ls2, :), data2_new_tmp(rest2, :));

data1_list = vertcat(data1_list(common_ls1, :), data1_list(rest1, :));
data2_list = vertcat(data2_list(common_ls2, :), data2_list(rest2, :));


%for k = 1 : length(data1_list)
%    cellContents = data1_list{k};
%    % Truncate and stick back into the cell
%    data1_list{k} = strcat(cellContents, '_m', num2str(1));
%end
%
%for k = 1 : length(data2_list)
%    cellContents = data2_list{k};
%    % Truncate and stick back into the cell
%    data2_list{k} = strcat(cellContents, '_m', num2str(2));
%end


outname1 = strsplit(data1_dir,'/')
outname2 = strsplit(data2_dir,'/')
outname1 = char(outname1(end))
outname2 = char(outname2(end))


outfile1 = strcat(out_dir, outname1, '_proTran')
outfile2 = strcat(out_dir, outname2, '_proTran')


fileID = fopen(outfile1, 'w');
fmt = '%d %d\n';
fprintf(fileID, fmt, size(data1_new));
fclose(fileID);

out = horzcat(data1_list,num2cell(data1_new));
fileID = fopen(outfile1, 'a');
NumCol = 100;
baseString = ['%8f '];
formatSpec = repmat(baseString,1,NumCol);
formatSpec = strcat(['%s ', formatSpec(1:size(formatSpec,2)-1), '\n']);
[nrows,ncols] = size(out);
for row = 1:nrows
    fprintf(fileID,formatSpec,out{row,:});
end


fileID = fopen(outfile2, 'w');
fmt = '%d %d\n';
fprintf(fileID, fmt, size(data2_new));
fclose(fileID);

out = horzcat(data2_list,num2cell(data2_new));
fileID = fopen(outfile2, 'a');
NumCol = 100;
baseString = ['%8f '];
formatSpec = repmat(baseString,1,NumCol);
formatSpec = strcat(['%s ', formatSpec(1:size(formatSpec,2)-1), '\n']);
[nrows,ncols] = size(out);
for row = 1:nrows
    fprintf(fileID,formatSpec,out{row,:});
end


% if shared == 1
%     for i=1:length(data1_list)
%         if length(findstr(data1_list{i},'_m')) == 1
%             tmp = strsplit(data1_list{i},'_m');
%             data1_list(i) = tmp(1);
%         end
%     end
% end

end


