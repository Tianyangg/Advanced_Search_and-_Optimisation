
function lalong = converRAtL(city)
PI = 3.141592;
lalong = [];
deg = fix(city(1));
min = city(1) - deg;
lalong(1) = PI * (deg + 5.0 * min / 3.0 ) / 180.0; 
deg = fix( city(2) );
min = city(2) - deg;
lalong(2) = PI * (deg + 5.0 * min / 3.0 ) / 180.0;
end
