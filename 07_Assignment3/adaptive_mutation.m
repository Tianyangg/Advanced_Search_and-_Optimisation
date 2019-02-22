function new_off = adaptive_mutation(offspring, A, N)
% hyperparameters
e = 0.5;
M = 5;
% perform adaptive mutation
bit_length = size(offspring, 2);
for i = 1:size(offspring, 1)
    individual = offspring(i,:)
    % calculate how many violation
    temp = A(:, individual==1);
    res = size(find(sum(temp, 2) - 1 == 0));
    if (res >= e*N)
        index = randi([1 bit_length], 1, M);
        individual(index) = 1;
    end
    new_off(i,:) = individual;
end
end

