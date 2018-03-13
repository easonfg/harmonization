function train_s2(c3,c4)

filename = 'train_nonoverlap.txt';
fid=fopen(filename,'w');
for i=1:length(c3)
    fprintf(fid,'%s %s\n',c3{i},c4{i});
end
fclose(fid);

end

