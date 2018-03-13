function [c1,c2] = train_import(filename)

delimiter = '|';

formatSpec = '%*q%*q%q%q%[^\n\r]';

fileID = fopen(filename,'r');
dataArray = textscan(fileID, formatSpec, 'Delimiter', delimiter, 'EmptyValue' ,NaN, 'ReturnOnError', false);
fclose(fileID);

c1 = dataArray{:, 1};
c2 = dataArray{:, 2};

clearvars filename delimiter formatSpec fileID dataArray ans;