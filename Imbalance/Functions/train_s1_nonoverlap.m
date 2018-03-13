function train_s1_nonoverlap(c3,c4)

% it has overlap
filename = 'train_overlap.txt';
fid=fopen(filename,'w');
for i=1:length(c3)
    fprintf(fid,'%s %s\n',c3{i},c4{i});
end
fclose(fid);

end

