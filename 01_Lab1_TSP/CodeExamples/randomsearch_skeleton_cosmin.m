function [total_distance, cities] = randomsearch_skeleton_cosmin(inputcities,max_iter)
% randomsearch

% Randomised search algorithm for TSP problem
%The input arguments are
% inputcities         - The cordinates for n cities are represented as 2
%                       rows and n columns and is passed as an argument for
%                       the randomised search algorithm.
% max_iter           - max_iter is the stopping criteria  

global iterations;
% Initialize the iteration number.
iterations = 1;
 
num_cities = length(inputcities);

% Objective function: the total distance for the routes.
previous_distance = distance(inputcities);
results = zeros(max_iter,1);
results(1) = previous_distance;
cities = results;
plot(results);
while iterations < max_iter
    % You need to write code to generate a random solution
    temp = randperm(num_cities - 1);
    temp = [temp, temp(1)];
    %perm = randperm(num_cities - 2);
    %perm = perm + 1;
    %temp = cat(2, 1, perm, 1);
 
    temp_cities = inputcities(:,temp);
	
	% Evaluate the solution
    current_distance = distance(temp_cities);
	
	% You need to write code to save the best solution
    if current_distance < previous_distance
        previous_distance = current_distance;
        cities = temp_cities;
    end
	
	% Update interation
    iterations = iterations + 1;
    results(iterations) = current_distance;
    
    plot(results(1:iterations),'r--');xlabel('iteration'); ylabel('f(x)');
    text(0.5,0.95,['Best = ', num2str(current_distance)],'Units','normalized');
    drawnow;
    
end

total_distance = previous_distance;
cities = cities;