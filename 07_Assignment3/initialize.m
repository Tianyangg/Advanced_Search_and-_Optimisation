function S = initialize(A, num_pop)
% initilisation of the population
%   parameters N:number of constrains   M:number of flight legs
%   A:constrain matrix
%   return the population:: cell array
%   population{i} = [x1, x2, x3...] are the indexes of the selected cols in
%   A which cor to the flight leg num

% initialize \alpha and \beta
alpha = {};
beta = {};
[rows, cols] = size(A);
for i = 1:rows
    alpha{i} = find(A(i,:)==1);
end
for j = 1:cols
    beta{j} = find(A(:,j)==1);
end
%[beta, alpha] = find(A==1);
% initialize S_k
% initialize S cell array
I = [1:rows];
S = {};

for k = 1:num_pop
    S_k = [];
    U = I;
    while ~isempty(U)
        % randomly select a row
        i = datasample(U, 1);
        % select j
        temp=alpha{i};
        while (1)
            j = datasample(temp, 1);
            if isempty(intersect(beta{j}, setdiff(I, U)))
                S_k = [S_k, j];
                U = setdiff(U, intersect(i, beta{j}));
                break;
            end
            
            temp = setdiff(temp, j);
            if isempty(temp)
                U = setdiff(U, intersect(i, beta{j}));
                break;
            end
        end
    S{k} = S_k;
    end
    
end
end

