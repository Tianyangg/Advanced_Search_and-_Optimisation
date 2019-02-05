function [avg, sd, b_solution, inter_distance, inter_route] = main()
% call this function and the output is 1000 iterations
% read file
c = read_file('ulysses22.tsp');

for i = 1:30 % 30 independent runs
    % call monte_carlo with 1000 iterations
    [avg(i), sd(i), b_solution(i,:), inter_distance(i,:), inter_route(i,:,:)] = monte_carlo(c, 1000);
    
end



end

