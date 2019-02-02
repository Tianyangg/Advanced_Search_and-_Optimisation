function f = visulize_cities(inputcities)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
%inputcities1 = horzcat(inputcities, inputcities(:,1))
plot(inputcities(1,:), inputcities(2,:), 'Marker','*')

start_city = [inputcities(1,1) inputcities(1,end)];
end_city = [inputcities(2,1) inputcities(2,end)];
%y_limit = [min(inputcities(:))-10, max(inputcities(:))+10];
%x_limit = [min(inputcities(:))-10, max(inputcities(:))+10];
%axis([y_limit,x_limit])
temp_3 = line(start_city,end_city);
set(temp_3,'color','b');

end

