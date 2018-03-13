%% 80%/20%

clear all
clc

ratio = 0.8;
A = ratio*100;
fname = sprintf('%dData1.mat',A);
load(fname)

method = {'no','pro'};
over = [100,70,40];
fold = 10;
fusion = 1;

for ot=1:length(method)
    for st=1:length(over)
        overlap = over(st)
        align = cell2mat(method(ot))
        Prediction
        fn = sprintf('%d_Result_f_%d_%s.mat',A,overlap,align);
        save(fn,'Prediction_Result')
    end
end

%% 90%/10%

clear all
clc

ratio = 0.9;
A = ratio*100;
fname = sprintf('%dData1.mat',A);
load(fname)

method = {'no','pro'};
over = [100,70,40];
fold = 10;
fusion = 1;

for ot=1:length(method)
    for st=1:length(over)
        overlap = over(st)
        align = cell2mat(method(ot))
        Prediction
        fn = sprintf('%d_Result_f_%d_%s.mat',A,overlap,align);
        save(fn,'Prediction_Result')
    end
end

%% 95%/5%

clear all
clc

ratio = 0.95;
A = ratio*100;
fname = sprintf('%dData1.mat',A);
load(fname)

method = {'no','pro'};
over = [100,70,40];
fold = 10;
fusion = 1;

for ot=1:length(method)
    for st=1:length(over)
        overlap = over(st)
        align = cell2mat(method(ot))
        Prediction
        fn = sprintf('%d_Result_f_%d_%s.mat',A,overlap,align);
        save(fn,'Prediction_Result')
    end
end

