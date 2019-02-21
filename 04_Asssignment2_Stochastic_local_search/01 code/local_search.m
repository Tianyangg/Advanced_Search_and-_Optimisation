function [best_distance, best_route, results] = local_search(inputcities)
% local search method:
% random start
% generate a set of neighbour solutions
% select the best available one
%
% move to the best available solution
% search using two opt
% return the best solution

num_cities = length(inputcities);
num_cities = num_cities - 1;
% generate random permutation starts with city index 1
old_route = horzcat(1, randperm(num_cities) + 1);
old_cities = inputcities(:, old_route);
old_distance = geographical_distance(old_cities);


% store the current solution as the best solution
best_route = old_route;
best_distance = old_distance;
results(1) = old_distance;


neighbours = zeros(40, 22);
neighbour_distance = zeros(40,1);

% initialize tabulist
tabu_list = zeros(30, 22);
tabu_count = 1;


for i = 1:400
    % from current solution, generate a list of neighbours
    for j = 1:40
        neighbours(j,:) = two_opt(best_route);
        neighbour_distance(j) = geographical_distance(inputcities(:, neighbours(j,:)));
    end
    % pick the best current available solution
    for j = 1:40
        [M, I] = min(neighbour_distance);
        if ~ismember(neighbours(I,:), tabu_list, 'rows')
            current_route = neighbours(I,:);
            %current_city = inputcities(:, current_route);
            current_distance = M;
            break;
        end
        neighbour_distance(I) = max(neighbour_distance);
    end
    
    if current_distance < best_distance
        % update tabulist
        tabu_list(tabu_count, :) = current_route;
        best_route = current_route;
        best_distance = current_distance;
        tabu_count = tabu_count + 1;
    end
    
    if tabu_count == 15
        tabu_count = 1;
    end
    results(i) = best_distance;
    
%     if current_distance == 7016
%         break;
%     end
    
    
%     % plot solution
    plot(results(1:i));xlabel('iteration'); ylabel('f(x)');
    text(0.5,0.95,['Best = ', num2str(best_distance)],'Units','normalized');
    drawnow;
    
    
end



end

