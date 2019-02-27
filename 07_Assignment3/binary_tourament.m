function [p, i] = binary_tourament(pop, A, c)
% pop is the population 
% c is the cost column 
index = randi([1 size(pop, 1)], 1, 2);
p1 = pop(index(1), :);
p2 = pop(index(2), :);
if fitness(c, p1)> fitness(c, p2)
    p = p1;
    i = index(1);
else
    p = p2; 
    i = index(2);
end
% f1 = feasible(p1, A);
% f2 = feasible(p2, A);
% if (f1 && f2)
%     if(fitness(c, p1) < fitness(c, p2))
%         p = p1;
%         i = index(1);
%     else
%         p = p2;
%         i = index(2);
%     end
% elseif (f1 && f2)
%     if f1
%         p = p1;
%         i = index(1);
%     else
%         p = p2;
%         i = index(2);
%     end        
% else
%     if penalty(A, p1) < penalty(A, p2)
%         p = p1;
%         i = index(1);
%     else
%         p = p2;
%         i = index(2);
%     end
% end

end
