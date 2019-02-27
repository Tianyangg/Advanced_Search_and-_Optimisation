function new_off = adaptive_mutation(off, A, N)

% % hyperparameters

%mutate individual

% perform adaptive mutation
bit_length = size(off, 2);
individual = off;
% mutation rate
rate = (5/bit_length);

for i = 1:bit_length
    if rand() <= rate
        individual(i) = ~individual(i);
    end
end 
new_off = individual;
% %individual = off(i,:);
% % calculate how many violation
% temp = A(:, individual == 1);
% res = length(find(sum(temp, 2) - 1 ~= 0 ));
% 
% %if (res >= e*N)
% if(1)
%     index = randi([1 bit_length], 1, M);
%     individual(index) = ~individual(index);
%     %mut = mu + 1;
% end
% new_off = individual;

end

