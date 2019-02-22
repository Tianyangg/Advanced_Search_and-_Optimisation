t = p2;
feasible = [];
test_covere(1: 29) = 1;
for i = 1:size(t, 1)
    h = find(t(i,:)==1)
    cover = sum(matrix_a(:,h),2)
    if isequal(cover, test_covere')
        feasible = [feasible; t(i,:)]
    end
end

for j = 1:size(feasible,1)
    % calculate the cost
    %h = find(feasible(i,:)==1);
    ress(j) = fitness(column_cost, feasible(j,:));
end
[minn, ind] = min(ress)