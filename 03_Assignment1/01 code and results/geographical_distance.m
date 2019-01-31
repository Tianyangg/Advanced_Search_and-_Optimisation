function d = geographical_distance(input_cities)
% input 2*22 matrix of coordinates
% calculate the geographical distance
d = 0;
for n = 1 : length(input_cities)
    % circle
    if n == length(input_cities)
        d = d + ceil(sphere_distance(input_cities(:,n), input_cities(:,1)));
        %d = d + ceil(sqrt(sum((input_cities(:,n) - input_cities(:,1)).^2)/10));
    else    
        %d = d + ceil(sqrt(sum((input_cities(:,n) - input_cities(:,n+1)).^2)/10));
        d = d + ceil(sphere_distance(input_cities(:,n), input_cities(:,n+1)));
    end

end

