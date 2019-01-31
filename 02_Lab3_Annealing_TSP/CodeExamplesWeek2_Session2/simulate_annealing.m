function [bestdistance,best_tour] = simulate_annealing(inputcities, iteration)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
num_cities = length(inputcities);
% intial route
best_tour = randperm(num_cities);
bestdistance = distance(best_tour);

for i = 1:iteration
    
end

end

