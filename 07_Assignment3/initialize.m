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
% initialize S1_k
% initialize S1 cell array
I = [1:rows];
S1 = {};

for k = 1:num_pop
    S1_k = [];
    U = I;
    while ~isempty(U)
        % randomly select a row
        i = datasample(U, 1);
        % select j
        temp=alpha{i};
        while (1)
            j = datasample(temp, 1);
            if isempty(intersect(beta{j}, setdiff(I, U)))
                S1_k = [S1_k, j];
                intersect(i, beta{j});
                %U = setdiff(U, intersect(i, beta{j}));
                U = setdiff(U, beta{j});
                break;
            end
            
            temp = setdiff(temp, j);
            if isempty(temp)
                U = setdiff(U, intersect(i, beta{j}));
                %U = setdiff(U, beta{j});
                break;
            end
        end
    S1{k} = S1_k;
    end
    
end

% binary representation

%initilize the matrix S (#poplation,#roundtrip)
S = zeros(num_pop, cols);
for i = 1:length(S1)
    % access the element
    S(i,S1{i}) = 1 ;
    
end
end

% test the difference of using intersect 
