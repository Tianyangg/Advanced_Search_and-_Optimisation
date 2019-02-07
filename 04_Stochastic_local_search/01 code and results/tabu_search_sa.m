function [best_distance,best_route] = tabu_search_sa(inputcities, stop_temperature)
% Overview:
% initial temperature and create a random solution
% begin to loop until it's cool or solution is 7013
    % select a neighbour by using 2-opt 
    % check if the swap is inside the tabulist
    % in: discard this i j and move to another i j
    % update tabulist
    % and decide if we move to that neighbour
    % decrease the temperature
    
% initial tabu list and tabu counter
global tabulist;
global tabu_counter;
tabulist =  zeros(50, 2);
tabu_counter  = 1;

num_cities = length(inputcities);
terminate = false;
% initial temp and ra=te, linear cool
temperature = 1000;
cooling_rate =  0.997;
% intial route

old_route = randperm(num_cities);
cities = inputcities(:, old_route);
old_distance = geographical_distance(cities);

best_route = old_route;
best_distance = old_distance;
results(1) = old_distance;
iteration_count = 1;

while temperature > stop_temperature && best_distance >= 7016 && ~terminate
    [new_route, swapi, swapj] = tabu_two_opt(old_route, tabulist);
    cities = inputcities(:, new_route);
    new_distance = geographical_distance(cities);
    accept_rate = acceptance_function(old_distance, new_distance, temperature);
    if accept_rate > rand()
        % accept the result
        old_route = new_route;
        old_distance = new_distance;
        % update tabulist
    tabulist(tabu_counter, 1) = swapi;
    tabulist(tabu_counter, 2) = swapj;

    if tabu_counter == 50
        tabu_counter = 1;
    else
        tabu_counter = tabu_counter + 1;
    end
    
    end
    
    % if it's a best result?
    if new_distance < best_distance
       best_route = new_route;
       best_distance = new_distance;
    end
    
    %cool down
    temperature = temperature*cooling_rate;
    
    iteration_count = iteration_count + 1;
    results(iteration_count) = old_distance;
    % plot solution
    plot(results(1:iteration_count),'r--');xlabel('iteration'); ylabel('f(x)');
    text(0.5,0.95,['Best = ', num2str(best_distance)],'Units','normalized');
    drawnow;
end


end
