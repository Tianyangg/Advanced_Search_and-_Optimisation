function [fitness, total_profit, total_cons_vio, best_solution] = BGA_template
% Solving project selection problme using Binary GA


% Generate 4 bits are enough for our problem: 4 projects
num_bit = 4;

% Parameters
crossover_prob = 0.85;
mutation_prob = 1/num_bit;
num_ind = 7;
max_iter = 10000;
num_parents = floor(num_ind * 0.3);

% Generate initial solution
pop = randi([0 1], num_ind , num_bit);

% Calculate fitness for the initial population
fitness = [];
fitness = cal_fitness(pop);

% Sort the individuals in the population according to their fitness values
% Note: we are maximising profit (the more profit, the better the
% individual)
[~, sorted_idx] = sort(fitness, 'descend');
pop = pop(sorted_idx,:);


termination_flag = false;
t=1;
while termination_flag == false
    
    
    %  Select parents from the population based on their fitness using truncation selection   
    parents = pop(1:num_parents,:);
    %offerspring = parents;
    
    
    
    %% apply crossover    
    for j=1:floor(num_parents/2)      
        % Randomly select two individuals from parents
        size_parents = size(parents);
        ind_index = randsample(size_parents(1), 2);
        individuals = parents(ind_index, :);
        % Randomly select a bit as cross point
        cross_point = randi([1 num_bit - 1],1);
        % Swap the bits beyond the cross point
        temp1 = individuals(1,:);
        temp2 = individuals(2,:);
        
        offspring(1, 1:cross_point) = temp1(1:cross_point);
        offspring(1, cross_point+1: num_bit) = temp2(cross_point+1:num_bit);
        offspring(2, 1:cross_point) = temp2(1:cross_point);
        offspring(2, cross_point+1: num_bit) = temp1(cross_point+1:num_bit);
%        offspring(1) = [temp1(:,[1:cross_point]), temp2(:, [cross_point+1:num_bit])];
%        offspring(2) = [temp2(:,[1:cross_point]), temp1(:, [cross_point+1:num_bit])];
    end
    
    %% apply mutation.  
    if rand(1) <  crossover_prob
        for j=1:num_parents   
             % Select the bits for mutation
             bit_index = randi([1 4]);
             % flip it
             offspring(:,bit_index) = ~ offspring(:, bit_index);

        end
    end
    
    % Evaluation fitness of the new population (old population + new offspring)
    % Note: my implementation is not efficient
    temp_pop = [pop; offspring];   
    fitness = cal_fitness(temp_pop);
    
    % Sort the individuals in the population according to their fitness values
    [fitness, sorted_idx] = sort(fitness, 'descend');
    % Replace the worst individuals, or select the top num_ind individuals from the new population  
    pop = temp_pop(sorted_idx(1:num_ind),:);

    
    % Termination condiction 
    t=t+1;
    if(t>max_iter)
        termination_flag = true;
    end
    
end    
   
best_solution = pop(1, :);
[fitness, total_profit, total_cons_vio]  = cal_fitness(pop);
end







