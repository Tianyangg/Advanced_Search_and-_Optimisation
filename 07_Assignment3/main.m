clear all;
[matrix_a, column_cost] = ReadInData('b727.dat');
pop_size = 100;
% initialize the population
p2 = initialize(matrix_a, pop_size);

[rows, cols] = size(matrix_a);
% genetic algo
for i = 1: 10
    offspring = crossover(p2, 200);
    offspring = adaptive_mutation(offspring, matrix_a, pop_size);
    for j = 1:size(offspring, 1)
        offspring(j,:) = improvement_operator(offspring(j,:), matrix_a, column_cost);
    end
    
    new_generation = [p2; offspring];
    ranked = Stochatic_ranking(0.5, rows, cols, new_generation, matrix_a, column_cost);
    p2 = ranked(1:pop_size,:);
end


%Stochatic_ranking(0.5, rows, cols, p, matrix_a, column_cost)