function train_s1_overlap(c3,c4,event_diff_list)

% it has overlap
filename = 'event.txt';
fid=fopen(filename,'w');
for i=1:length(c3)
    fprintf(fid,'%s %s\n',c3{i},c4{i});
    i
end
fclose(fid);

data = certain_event(filename,event_diff_list,0);

delete(filename);

filename = 'train_overlap.txt';
fid=fopen(filename,'w');
for i=1:length(c3)
    fprintf(fid,'%s\n',data{i});
    i
end
fclose(fid);

end

