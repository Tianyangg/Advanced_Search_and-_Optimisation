function [fitness, total_profit, total_cons_vio]  = cal_fitness(pop)
% the dimension <3 will not work
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
