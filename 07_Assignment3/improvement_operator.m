function S1 = improvement_operator(S1, A, cost_col)
% improvement
% S1: binary strings
% S set of columns in a solution
% U set of uncovered rows
% w_j number of cols that cover row i
S = find(S1 == 1);
alpha = {};
beta = {};
[rows, cols] = size(A)
for i = 1:rows
    alpha{i} = find(A(i,:)==1);
end
for j = 1:cols
    beta{j} = find(A(:,j)==1);
end

for i = 1:rows
    %intersect(alpha{i}, S)
    w(i) = length(intersect(alpha{i}, S));
end
I = [1:rows];
%w(I) = size(intersect(alpha{I}, S));
T = S;
% Drop procecure
while ~isempty(T)
    j = datasample(T, 1)
    T = setdiff(T, j);
    %for all i in beta{j}
    temp = beta{j};
    for counter = 1:length(temp)
        if w(counter)>2
            S = setdiff(S, j);
            w(counter) = w(counter) - 1;
        end
    end
end

% ADD
U = find(w==0)
V = U;
while ~isempty(V)
    i = datasample(V, 1);
    V = setdiff(V, i);
    for search = 1:length(alpha{i})
        j = alpha{i}(search);
        %zhen zi ji
        j2 = [];
        if (isempty(setdiff(beta{j}, U))) && ~isequal(beta{j}, U)
            j2 = [j2, j];            
        end
       
    end
    % now you have all the js that satisfy the condition,
    % minimize the cost if j2 is not emty, otherwise j doesnot exist
    if ~isempty(j2)
        cost = cost_col(j2)./size(beta{j2});
        [m, index] = min(cost);
        j = j2(index);
        S = union(S, j)
        for i1 = 1:length(beta{j})
            w(i1) = w(i1) + 1; 
        end
        U = setdiff(U, beta{j});
        V = setdiff(V, beta{j});
    end
     
end

S1(S) = 1;
U = find(w==0)
end

