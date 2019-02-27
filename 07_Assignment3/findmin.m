function [minn, fea, ress] = findmin(p, mat, cost)
%
t = p;
fea = [];

for i = 1:size(t, 1)
    h = t(i,:)==1;
    cover = sum(mat(:,h),2);
    %cover = sum(mat(:,h),2);
    if isempty(find(cover == 0))
    %if isequal(cover, test_covere')
        fea= [fea; t(i,:)];
    end
end
ress = [];
for j = 1:size(fea,1)
    % calculate the cost
    %h = find(feasible(i,:)==1);
    ress(j) = fitness(cost, fea(j,:));
end
if ~isempty(ress)
    [minn, ind] = min(ress);
else
    minn = 20000;
    ind = 0;
end

end

