function y = output(outfile, NumCol, data_new, data_list)
  fileID = fopen(outfile, 'w');
  fmt = '%d %d\n';
  fprintf(fileID, fmt, size(data_new));
  fclose(fileID);

  out = horzcat(data_list,num2cell(data_new));
  fileID = fopen(outfile, 'a');
  baseString = ['%8f '];
  formatSpec = repmat(baseString,1,NumCol);
  formatSpec = strcat(['%s ', formatSpec(1:size(formatSpec,2)-1), '\n']);
  [nrows,ncols] = size(out);
  for row = 1:nrows
        fprintf(fileID,formatSpec,out{row,:});
  end
