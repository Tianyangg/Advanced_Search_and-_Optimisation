function [p1, p2] = fbased_selection(p, A, c)
% select parents based on fitness
% calculate the fitness
for i = 1:size(p, 1)
    new_fit(i) = 1/fitness(c, p(i,:));
end 

sum_fit = sum(new_fit);
% select parents(i) with certain rate
for i = 1:size(p, 1)
    if i == size(p, 1)
        p1 = p(i,:);
        break;
    end
    if rand() < new_fit(i)/sum_fit
        p1 = p(i,:);
        break;        
    end
end

for i = 1:size(p, 1)
    if i == size(p, 1)
        p2 = p(i,:);
        break;
    end
    if rand()< new_fit(i)/sum_fit
        p2 = p(i,:);
        break;        
    end
end
while isequal(p1, p2)
    %disp('hey u have same parents')    
    for i = 1:size(p, 1)
    if i == size(p, 1)
        p2 = p(i,:);
        break;
    end
    if rand()< new_fit(i)/sum_fit
        p2 = p(i,:);
        break;        
    end
    end

end


end

