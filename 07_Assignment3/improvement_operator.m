function [outputArg1,outputArg2] = improvement_operator(S, A)
% improvement
% S set of columns in a solution
% U set of uncovered rows
% w_j number of cols that cover row i
alpha = {};
beta = {};
[rows, cols] = size(A);
for i = 1:rows
    alpha{i} = find(A(i,:)==1);
end
for j = 1:cols
    beta{j} = find(A(:,j)==1);
end

w_i = size(intersect(alpha{i}, S))
T = S;
% Drop procecure


end

