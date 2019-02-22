function offspring = crossover(pop, offsize)
% mutation and crossover to generate offspring
bit_length = size(pop, 2);
for i = 1:offsize
    % select parents
    size(pop, 1)
    index = randi([1 size(pop, 1)], 1, 2);
    p1 = pop(index(1), :);
    p2 = pop(index(2), :);
    % crossover:
    for j = 1: bit_length
        if(rand() < 0.5)
            temp(j) = p1(j);
        else
            temp(j) = p2(j);
        end
    end
    offspring(i,:) = temp;
end

end