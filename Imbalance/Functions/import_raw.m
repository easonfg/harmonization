function [data1,data2,data3,data4]=import_raw(filename)

delimiter = '|';
formatSpec = '%q%q%q%q%[^\n\r]';
fileID = fopen(filename,'r');

dataArray = textscan(fileID, formatSpec, 'Delimiter', delimiter,  'ReturnOnError', false);
fclose(fileID);

raw = repmat({''},length(dataArray{1}),length(dataArray)-1);
for col=1:length(dataArray)-1
    raw(1:length(dataArray{col}),col) = dataArray{col};
end
numericData = NaN(size(dataArray{1},1),size(dataArray,2));

rawNumericColumns = {};
rawCellColumns = raw(:, [1,2,3,4]);

R = cellfun(@(x) ~isnumeric(x) && ~islogical(x),rawNumericColumns); 
rawNumericColumns(R) = {NaN}; 

data1 = rawCellColumns(:, 1);
data2 = rawCellColumns(:, 2);
data3 = rawCellColumns(:, 3);
data4 = rawCellColumns(:, 4);

clearvars filename delimiter formatSpec fileID dataArray ans raw col numericData rawNumericColumns rawCellColumns R;