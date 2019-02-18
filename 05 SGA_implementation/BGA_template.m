function [fitness, total_profit, total_cons_vio, best_solution] = BGA_template
% Solving project selection problme using Binary GA


% Generate 4 bits are enough for our problem: 4 projects
num_bit = 4;

% Parameters
crossover_prob = 0.85;
mutation_prob = 1/num_bit;
num_ind = 5;
max_iter = 100;
num_parents = floor(num_ind * 0.3);

% Generate initial solution
 

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
    offerspring = parents;
    
    
    
    %% apply crossover    
    for j=1:floor(num_parents/2)
        if rand(1) <  crossover_prob
            % Randomly select two individuals from parents
            
            % Randomly select a bit as cross point
             
            % Swap the bits beyond the cross point
 
        end
    end
    
    %% apply mutation.  
    for j=1:num_parents   
         % Select the bits for mutation
 
         % flip it
 
        end
    end
    
    % Evaluation fitness of the new population (old population + new offspring)
    % Note: my implementation is not efficient
    temp_pop = [pop; offerspring];   
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


function [fitness, total_profit, total_cons_vio]  = cal_fitness(pop)
profits = [0.2 0.3 0.5 0.1];
project_year_budets = [
    .5  .3  .2;
    1   .8  .2;
    1.5 1.5 .3;
    0.1 0.4 .1];
max_budgets = [3.1 2.5 0.4];

num_ind = length(pop);
total_profit = zeros(num_ind,1);
total_bugets = zeros(num_ind,3);
for i=1:num_ind
    solution = pop(i,:);
    total_profit(i,1) = solution * profits';
    total_bugets(i,:) = solution*project_year_budets;    
end

% We use a simple penalty function, i.e., penalise those 
% solutions that are infeasible (exceeded the budget)
% First find out which solutions are not feasible
contraint_violations = repmat(max_budgets,num_ind, 1) - total_bugets;
total_cons_vio = sum(contraint_violations<0, 2);
% Then penalise those solutions by reducing the fitness
fitness = total_profit -  total_cons_vio;
end





