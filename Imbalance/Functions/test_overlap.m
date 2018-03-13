function data = test_overlap(c3,event_diff_list,opt)

filename = 'event.txt';
fid=fopen(filename,'w');
for i=1:length(c3)
    fprintf(fid,'%s\n',c3{i});
end
fclose(fid);

data = certain_event(filename,event_diff_list,opt);

delete(filename);

end

