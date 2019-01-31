function [average, deviation, best_solution, intermediate_distance, intermediate_route] = monte_carlo(cities, max_iteration)
%
global iterations;
iterations = 1;
num_cities = length(cities);
% generate random permutation[]
index = randperm(num_cities);
optimal_route = index;
input_cities = cities(:, index);
optimal_distance = geographical_distance(input_cities);

results = zeros(max_iteration,1);
results(1) = optimal_distance;
plot(results);

% show the solution and distance of 1th, 500th and 1000th code
intermediate_route = zeros(num_cities,3); %[[route1], [route_500], [route_1000]]
intermediate_distance = zeros(1,3);%[distance_1, distance_590, distance_1000]

ctr = 1;
while iterations <= max_iteration
    temp = randperm(num_cities);
    new_cities = cities(:, temp);
    current_distance = geographical_distance(new_cities);
    % accept?
    if current_distance < optimal_distance
       optimal_route = temp;
       optimal_distance = current_distance;
    end
    
    if (iterations == 1 || iterations == 500 || iterations == 1000)
        intermediate_route(1:num_cities,ctr) = optimal_route;
        intermediate_distance(1,ctr) = optimal_distance;
        ctr = ctr + 1
        
    end
    
    iterations = iterations + 1;
    results(iterations) = current_distance;
    
    plot(results(1:iterations),'r--');xlabel('iteration'); ylabel('f(x)');
    text(0.5,0.95,['Best = ', num2str(optimal_distance)],'Units','normalized');
    drawnow;
end

best_solution = optimal_distance;
average = mean(results);
deviation = std(results);

end

