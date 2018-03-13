%% Not Correspondence Events Generation

tfilename = 'train1_org.txt';
[c3,c4] = train_import(tfilename);
filename = 'event.txt';
fid=fopen(filename,'w');
for i=1:length(c3)
    fprintf(fid,'%s %s\n',c3{i},c4{i});
end
fclose(fid);

fid = fopen(filename);
words = textscan(fid, '%s');
event_list = unique(words{1,1});

over = [100,70,40];

for i=1:length(over)
    
    overlap = over(i);
    
    a = randperm(length(event_list));
    event_diff_list = event_list(a(1:round(length(a)*((100-overlap)/100))));
    
    diffname = sprintf('over%d.mat',overlap);
    save(diffname,'event_diff_list')

end

%% Total Data Generation

tfilename = 'train1_org.txt'; % total patient history sequences 
[c1,c2,c3,c4] = import_raw(tfilename); 
total = [c1,c2,c3,c4];

rate = [0.8,0.9,0.95];

for i=1:length(rate)
    ratio = rate(i); % for the large hospital
    A = ratio*100;
    k = round(ratio*length(c3));
    
    site1 = total(1:k,:);
    site2 = total(k+1:end,:);
    
    fold = 10;
    CVO1 = cvpartition(size(site1,1),'kfold',fold);
    CVO2 = cvpartition(size(site2,1),'kfold',fold);
    
    dataname = sprintf('%dData1.mat',A);
    save(dataname,'CVO1','CVO2','site1','site2')
end
