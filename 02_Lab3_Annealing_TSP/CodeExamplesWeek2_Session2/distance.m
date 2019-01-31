function d = distance(inputcities)

d = 0;
for n = 1 : length(inputcities)
    if n == length(inputcities)
        d = d + ceil(sqrt(sum((inputcities(:,n) - inputcities(:,1)).^2)/10));
    else    
        d = d + ceil(sqrt(sum((inputcities(:,n) - inputcities(:,n+1)).^2)/10));
    end
end

