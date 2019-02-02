function f = plotcities(inputcities)
% plotcities
% plotcities(inputcities) plots the location of cities and the the symmetric route. 
% 
% shg makes the current figure visible and raises it above all other figures on the screen. 
shg


% Plot blue '*' as cities on Figure temp_1
temp_1  = plot(inputcities(1,:),inputcities(2,:),'b*');
% Set the figure non erasable 
%set(temp_1,'erasemode','none');
% Plot route using red lines 
temp_2 = line(inputcities(1,:),inputcities(2,:),'Marker','*');
set(temp_2,'color','b');
city_inx = [1:length(inputcities)]';
temp_name = num2str(city_inx); 
city_name = cellstr(temp_name);
dx = 0.1; dy = 0.1; % displacement so the text does not overlay the data points
text(inputcities(1,:)+dx, inputcities(2,:)+dy, city_name);

% Don't forget to go back to the origin city
start_city = [inputcities(1,1) inputcities(1,end)];
end_city = [inputcities(2,1) inputcities(2,end)];
% y_limit = [min(inputcities(:))-10, max(inputcities(:))+10];
% x_limit = [min(inputcities(:))-10, max(inputcities(:))+10];
% axis([y_limit,x_limit])
temp_3 = line(start_city,end_city);
set(temp_3,'color','b');

dist = geographical_distance(inputcities);
distance_print = sprintf(...
     '1000th iteration Roundtrip length  % 4.6f km' ...
     ,dist);
title(distance_print,'fontweight','bold');
drawnow;
