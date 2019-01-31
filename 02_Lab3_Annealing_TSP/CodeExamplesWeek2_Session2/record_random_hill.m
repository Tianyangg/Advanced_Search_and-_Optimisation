function [distance,route] = record_random_hill(iteration, input)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
distance = zeros(1, iteration);
route = zeros(iteration, length(input));

for i = 1:iteration
    [distance(i),route(i,:)] = simple_hill_climbing_two_opt(input);

end

distance1 = distance
plot(distance)

