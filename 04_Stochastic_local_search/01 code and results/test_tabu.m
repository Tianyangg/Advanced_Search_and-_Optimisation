function solutions = test_tabu(c)
% this is the test for tabu_search
solutions = zeros(1,30);
for counter = 1:30
    [solutions(counter), route] = tabu_search_sa(c,0.01);
end

plot(solutions)
end

