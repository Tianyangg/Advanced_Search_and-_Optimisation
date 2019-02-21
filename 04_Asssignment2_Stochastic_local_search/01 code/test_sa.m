function solutions = test_sa()
% this is the test for tabu_search
c = read_file('ulysses22.tsp');
temp = 180;

solutions = zeros(1,30);
for counter = 1:30
    [solutions(counter), route] = simulate_annealing(c, temp);
end

plot(solutions)
end

