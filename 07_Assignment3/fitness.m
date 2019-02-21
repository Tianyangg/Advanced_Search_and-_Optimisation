function f = fitness(cost, x)
%calculate the fitness sum of the cost
costs = cost(:, x);
f = sum(costs);
end

