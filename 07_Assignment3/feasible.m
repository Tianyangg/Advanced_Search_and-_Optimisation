function f = feasible(individual, A)
% if a solution is feasible return true, else return false

index = individual==1;
cover = sum(A(:, index), 2);
if isempty(find(cover == 0))
    f = 1;
else
    f = 0;
end
end

