function solutions = test_tabu()
% this is the test for tabu_search
c = read_file('ulysses22.tsp');
solutions = zeros(1,30);

for counter = 1:30
    solutions(counter) = local_search(c);
end
end

