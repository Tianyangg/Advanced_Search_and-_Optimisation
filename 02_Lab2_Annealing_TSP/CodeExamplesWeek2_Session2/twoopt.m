%% Swap two cities
function newroute = twoopt(route, i, k)
% Step 1: take $route[1]$ to $route[i-1]$ and add them in order to
% $newroute$ 
    newroute = zeros(1,length(route));
    newroute(1:i-1) = route(1:i-1);
% Step 2: take $route[i]$ to $route[k]$ and add them in reverse order to
% $newroute$ 
    newroute(i:k) = fliplr(route(i:k));
% Hint: type help fliplr

% Step 3: take $route[k+1]$ to end and add them in order to new $newroute$
 
    newroute(k+1:length(route)) = route(k+1:length(route));

end