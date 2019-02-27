function S2 = improvement_operator_2(S1, A, cost_col)
% improvement
% S1: binary strings
% S set of columns in a solution
% U set of uncovered rows
% w_j number of cols that cover row i
S = find(S1 == 1);
alpha = {};
beta = {};
[rows, cols] = size(A);
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

%I = [1:rows];
%w(I) = size(intersect(alpha{I}, S));
T = S;
%disp(w);

% Drop
while ~isempty(T)
    j = datasample(T, 1);
    T = setdiff(T, j);
    %for all i in beta{j}
    temp = beta{j};
    if ~isempty(find(w(beta{j}) >= 2))
        S = setdiff(S, j);
        for counter = 1:length(temp)
            w(beta{j}(counter)) = w(beta{j}(counter)) - 1;
        end
    end
    
end

% ADD
U = find(w==0);
V = U;
while ~isempty(V)
    i = datasample(V, 1);
    V = setdiff(V, i);
    j2 = [];
    for search = 1:length(alpha{i})
        j = alpha{i}(search);
        %zhen zi ji
        %j2 = [];
        %if (isempty(setdiff(beta{j}, U))) 
        if all(ismember(beta{j}, U))==1
        %if ~isempty(intersect(beta{j}, U))
            %j2(end) = j
            j2 = [j2, j];            
        end
       % disp(j2);
    end
   
    % now you have all the js that satisfy the condition,
    % minimize the cost if j2 is not empty, otherwise j does not exist
    cost = [];
    if ~isempty(j2)
        %cost = cost_col(j2)./size(beta{j2});
        for i = 1: size(j2,2)
            %size(beta{j2(i)})
            cost(i) = cost_col(j2(i))/length(beta{j2(i)});
        end
        [m, index] = min(cost);
        j = j2(index);
        S = union(S, j);
        %cost
        w(beta{j})= w(beta{j}) + 1;
%         for i1 = 1:length(beta{j})            
%             w(beta{j}(i1)) = w(beta{j}(i1)) + 1; 
%         end
        U = setdiff(U, beta{j});
        V = setdiff(V, beta{j});
    end
end
S2 = zeros(size(S1));
S2(S) = 1;
S = find(S1 == 1);
for i = 1:rows
    %intersect(alpha{i}, S)
     w2(i) = size(intersect(alpha{i}, S), 2);
end

end

