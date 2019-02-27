function p = Stochatic_ranking(P_j, lambda, N, pop, a_matrix, col_cost)
% implementation of stochastic ranking 
%   parameter P_j: the probability of comparing when infeasible
%   parameter lamda: number of ranked elements
%   return the array

% I{j} should be an indivivual
% j is the index
A = a_matrix;
I = [1:lambda];
%p = pop;
for i = 1:N
    swap_count = 0;
    for j = 2: N-1
    %for j = 1: N-1
    %for j = 1:lambda-1
        u=rand();
        if ((penalty(A, pop(I(j),:)) == 0) && (penalty(A, pop(I(j+1),:)) == 0)) || (u < P_j)
            if(fitness(col_cost, pop(I(j),:))) > fitness(col_cost, pop(I(j+1),:))
                I([j, j+1]) = I([j+1, j]);
                swap_count = swap_count + 1;                
            end
        else
            if(penalty(A, pop(I(j),:)) > penalty(A, pop(I(j+1),:)))
                I([j, j+1]) = I([j+1, j]);
                swap_count = swap_count + 1;
            end
        end
    end
    %disp(swap_count)
    if swap_count == 0
        break;
    end
    
    
end
p = pop(I,:);




end

