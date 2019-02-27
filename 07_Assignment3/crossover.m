function offspring = crossover(pop, offsize, mat, cost, g)
% mutation and crossover to generate offspring
bit_length = size(pop, 2);
for i = 1:offsize
    % select parents
    %size(pop, 1)
%     index = randi([1 size(pop, 1)], 1, 2);
%     p1 = pop(index(1), :);
%     p2 = pop(index(2), :);
    %%
    % ADD HERE
    [best(i), fea, re] = findmin(pop, mat, cost);
    if (~isempty(fea)) && (size(fea, 1) ~= 1)
        %[p11, p22] = fbased_selection(pop, mat, cost);
        
        if rand() < 0.7
            [p11, p22] = fbased_selection(pop, mat, cost);
        else
            [p11, p22] = parent_selection(pop, mat, cost);
        end
    %%
    else
    [p11, p22] = parent_selection(pop, mat, cost);
    %[p11, p22] = fbased_selection(pop, mat, cost);
    end
    
    p1 = adaptive_mutation(p11, mat, g);
    p2 = adaptive_mutation(p22, mat, g);
    
    % another crossovertime
    cross_num = 10;
    cross_point = randi([1 bit_length], 1, cross_num);
    cross_point = sort(cross_point);
    flag = 1;
    t = zeros(1, length(p1));
    t(1:cross_point(1)) = p1(1:cross_point(1));
    t(cross_point(cross_num):end) = p2(cross_point(cross_num):end);
    for ind = 2: cross_num-1
        if flag
           t(cross_point(ind):cross_point(ind+1)) = p2(cross_point(ind):cross_point(ind+1));
           flag = ~flag;
        else
           t(cross_point(ind):cross_point(ind+1)) = p1(cross_point(ind):cross_point(ind+1));
           flag = ~flag;
        end
    end
%     if ismember(t,pop,'rows')
%         disp('existing element generated in crossover');
%         i = i-1;
%     else
        offspring(i,:) = t;
%    end
     
end

end