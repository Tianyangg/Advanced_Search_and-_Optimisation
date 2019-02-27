function f = fitness(cost, x)
%calculate the fitness sum of the cost
%costs = cost(:, x>=1);
%f = sum(costs);
f = x*cost';
end

