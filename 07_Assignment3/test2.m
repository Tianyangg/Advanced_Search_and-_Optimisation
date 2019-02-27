function best = test2()

%[matrix_a, column_cost] = ReadInData('17197.txt');
%[matrix_a, column_cost] = ReadInData('b727.dat');
[matrix_a, column_cost] = ReadInData('sppnw42.txt');
pop_size = 100;
% initialize the population
p2 = initialize(matrix_a, pop_size);
% %ANOTHER INITIALIZE
% p2 = zeros(pop_size, size(matrix_a,2));
% for i = 1:pop_size
%     ini = StochasticSetCover_l(matrix_a, column_cost);
%     if ismember(ini, p2)
%         i = i-1;
%     else
%         p2(i,:) = ini;
%     end
% end
% disp('initialize done')
% [rows, cols] = size(matrix_a);
% for i = 1:pop_size
%     feasible(p2(i,:), matrix_a)
% end
% genetic algo
for i = 1: 20000
    % rank the population
    feasible_count = 0;
    for j = 1:size(p2, 1)
        %offspring(j,:) = improvement_operator(offspring2(j,:), matrix_a, column_cost);
        p2(j,:) = improveOperator_l(p2(j,:),matrix_a, column_cost); 
        if (feasible(p2(j,:), matrix_a))
            feasible_count = feasible_count+1;
        end
    end
    %disp(['number of feasible solutions in children:', num2str(feasible_count)])

    %p2 = improveOperator_l(p2, matrix_a, column_cost);
    ranked = Stochatic_ranking(0.47, size(p2, 1), size(p2, 1), p2, matrix_a, column_cost);
    
    %crossover and mutation
    offspring2 = crossover(ranked, 1, matrix_a, column_cost);
    %offspring2 = adaptive_mutation(offspring1, matrix_a, pop_size);
    
    offspring = improveOperator_l(offspring2,matrix_a, column_cost);
    while ismember(offspring, p2, 'rows')
        offspring2 = crossover(ranked, 1, matrix_a, column_cost);
        offspring = improveOperator_l(offspring2,matrix_a, column_cost);
        disp('generating bbuchongfu')
    end
    if (feasible(offspring, matrix_a))
        disp(['genration', num2str(i), 'feasible'])
    end
    
    p2 = [ranked(1:pop_size-1,:); offspring];
    %p_old = [p2; offspring];
    %ranked = Stochatic_ranking(0.47, size(p_old, 1), size(p_old, 1), p_old, matrix_a, column_cost);
    % replace
    %p2 = ranked(1:pop_size,:);
    [best(i+1), fea, re] = findmin(p2, matrix_a, column_cost);
   
    disp(['generation: ', num2str(i),' ', num2str(best(i))])
    
end

end

