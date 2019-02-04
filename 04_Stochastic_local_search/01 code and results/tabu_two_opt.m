function [newroute, i, j] = tabu_two_opt(route, tabu_list)
% implemented the two-opt algorithm
% step 0: genertate two random numbers 2 to length not the same

i = 0;
j = 0;
numcities = length(route - 1);
while i == j || isequal(ismember([i, j], tabu_list), 1) || isequal(ismember([j, i], tabu_list), 1)
    temp = randi([2, numcities], 1, 2);
    i = temp(1);
    j = temp(2);
end

% Step 1: take $route[1]$ to $route[i-1]$ and add them in order to
% $newroute$ 
    newroute = zeros(1,length(route));
    newroute(1:i-1) = route(1:i-1);
% Step 2: take $route[i]$ to $route[k]$ and add them in reverse order to
% $newroute$ 
    newroute(i:j) = fliplr(route(i:j));% Hint: type help fliplr

% Step 3: take $route[k+1]$ to end and add them in order to new $newroute$
 
    newroute(j+1:length(route)) = route(j+1:length(route));


end

