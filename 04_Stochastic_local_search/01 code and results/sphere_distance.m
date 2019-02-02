function s_distance = sphere_distance(x,y)

R = 6378.388;

PI = 3.141592;

x_deg = fix(x); % degree in integer
x_min = abs(fix((x - x_deg)*100)); % min in integer
y_deg = fix(y);
y_min = abs(fix((y - y_deg)*100));

% x_deg = round(x);
% x_min = abs(fix((x - x_deg)*100));
% y_deg = round(y);
% y_min = abs(fix((y - y_deg)*100));

longitute_x = dms2degrees([x_deg(1), x_min(1), 0]);
latitiude_x = dms2degrees([x_deg(2), x_min(2), 0]);
longitute_y = dms2degrees([y_deg(1), y_min(1), 0]);
latitiude_y = dms2degrees([y_deg(2), y_min(2), 0]);

s_distance = distance('gc', [longitute_x, latitiude_x], [longitute_y, latitiude_y], [R, 0]);

end

% x_deg = fix(x);
% x_min = x - x_deg;
% y_deg = fix(y);
% y_min = y - y_deg;
% 
% rad_x = PI * (x_deg + 5.0 * x_min / 3.0 ) / 180.0; % x = [lonigitude latitude]
% rad_y = PI * (y_deg + 5.0 * y_min / 3.0 ) / 180.0;
% 
% q1 = cos( rad_x(1) - rad_y(1) );
% q2 = cos( rad_x(2) - rad_y(2) );
% q3 = cos( rad_x(2) + rad_y(2) );
% s_distance=  R * acos( 0.5*((1.0+q1)*q2 - (1.0-q1)*q3) ) + 1.0;

% rad_x(1) = deg2rad(dms2degrees([x_deg(1), x_min(1), 0]));
% rad_x(2) = deg2rad(dms2degrees([x_deg(2), x_min(2), 0]));
% 
% rad_y(1) = deg2rad(dms2degrees([y_deg(1), y_min(1), 0]));
% rad_y(2) = deg2rad(dms2degrees([y_deg(2), y_min(2), 0]));
% 
% to degree
%DeltaS = acos(cos(rad_x(2))*cos(rad_y(2))*cos(rad_x(1)-rad_y(1))+sin(rad_x(2))*sin(rad_y(2)));
%s_distance = round(R*DeltaS);
