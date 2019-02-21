function [fitness, totl_cost, Violations] = calculatefitness(x, c, a)

% Follow Code example 3 to write your code
totl_cost = [];
Violations  = [];
penalty = 10000*Violations;

fitness = totl_cost + penalty;

