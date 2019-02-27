function best = test()

%[matrix_a, column_cost] = ReadInData('17197.txt');
%[matrix_a, column_cost] = ReadInData('b727.dat');
[matrix_a, column_cost] = ReadInData('sppnw43.txt');
pop_size = 100;
% initialize the population
p2 = initialize(matrix_a, pop_size);

disp('initialize done')
[rows, cols] = size(matrix_a);

[~, ~, re] = findmin(p2, matrix_a, column_cost);
cost = re;
% genetic algo
for i = 1: 30
    %crossover and mutation
    %offspring2 = crossover(p2, 500, matrix_a, column_cost);
    %offspring2 = adaptive_mutation(offspring1, matrix_a, pop_size);
    feasible_count = 0;
    %% CHANGE here
    offspring = zeros(500, cols);
    %% this means one offspring each time:
    disp('generating children..')
    for j = 1: 500
        % generate
        offspring_temp = crossover(p2, 1, matrix_a, column_cost, i);
        % improve it
        offspring_temp = improvement_operator_2(offspring_temp,matrix_a, column_cost); 
        %offspring_temp = improveOperator_l(offspring_temp,matrix_a, column_cost); 
        % to make sure the result is new
        while ismember(offspring_temp, p2, 'rows') || isequal(offspring_temp, offspring, 'rows')
            % generate
            offspring_temp = crossover(p2, 1, matrix_a, column_cost, i);
            % improve it
            offspring_temp = improvement_operator_2(offspring_temp,matrix_a, column_cost); 
            %offspring_temp = improveOperator_l(offspring_temp,matrix_a, column_cost);
        end
        
        %temp_cost = fitness(column_cost, offspring_temp);
        while ismember(offspring_temp, offspring, 'rows')
            %disp('heyty')
            % generate
            offspring_temp = crossover(p2, 1, matrix_a, column_cost, i);
            % improve it
            offspring_temp = improvement_operator_2(offspring_temp,matrix_a, column_cost); 
            %offspring_temp = improveOperator_l(offspring_temp,matrix_a, column_cost);
        end
        offspring(j,:) = offspring_temp;
        if (feasible(offspring(j,:), matrix_a))
            feasible_count = feasible_count+1;
            %disp(['genration', num2str(i), 'feasible', num2str(j), '  ', num2str(feasible(offspring(j,:), matrix_a))])
        end

    end
    disp(['number of feasible solutions in children:', num2str(feasible_count)])
    [b, ~, ~] = findmin(offspring, matrix_a, column_cost);
    disp(['generation:', num2str(i),' best solution in children: ', num2str(b)])
    p2 = [p2; offspring];
    disp('ranking...');
    old_ranked = Stochatic_ranking(0.49, size(p2, 1), size(p2, 1), p2, matrix_a, column_cost);
    p2 = [old_ranked(1:pop_size,:)];
    
    [best(i), fea, re] = findmin(p2, matrix_a, column_cost);
    
    disp(['generation:', num2str(i),' best solution: ', num2str(best(i))]);
    cost = re;
   
end

end

