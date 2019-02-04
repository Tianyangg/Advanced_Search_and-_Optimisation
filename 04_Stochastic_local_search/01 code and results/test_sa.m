function solutions = test_sa(c)
% this is the test for tabu_search
solutions = zeros(1,30);
for counter = 1:30
    [solutions(counter), route] = simulate_annealing(c, 0.01);
end

plot(solutions)
end

