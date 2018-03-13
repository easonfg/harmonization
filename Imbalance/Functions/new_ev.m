function [d1,d2] = new_ev(d1,d2,k,num,a,b)

% IDX = knnsearch(X,Y) % in X for each point in Y
idx_1 = knnsearch(d2,d1,'Distance','cosine','k',k);
idx_2 = knnsearch(d1,d2,'Distance','cosine','k',k);

new_d1 = [];
new_d2 = [];
for i=num+1:size(idx_2,1)
    new_d2 = [new_d2; a*(d2(i,:))+b*mean(d1(idx_2(i,:),:))]; % we can change it 
end

for i=num+1:size(idx_1,1)
    new_d1 = [new_d1; a*(d1(i,:))+b*mean(d2(idx_1(i,:),:))];
end

d1 = [d1(1:num,:);new_d1];
d2 = [d2(1:num,:);new_d2];

end

