function d = distance(city1, city2)
city1 = converRAtL(city1);
city2 = converRAtL(city2);
RRR = 6378.388;
q1 = cos( city1(2) - city2(2));
q2 = cos( city1(1) - city2(1));
q3 = cos( city1(1) + city2(1));
d = fix( RRR * acos( 0.5*((1.0+q1)*q2 - (1.0-q1)*q3) ) + 1.0);
end

