function d = alldis(cities)
d = 0;
for i = 1 : length(cities)
    if i <  length(cities)
        d = d + distance(cities(i,:),cities(i+1,:));
        %disp([num2str(i),': ',num2str(d)])
    else
        d = d + distance(cities(i,:), cities(1,:));
        %disp([num2str(i),': ',num2str(d)])
end

end