function population = Stochatic_ranking(P_j, lambda, N, pop, a_matrix, col_cost)
% implementation of stochastic ranking 
%   parameter P_j: the probability of comparing when infeasible
%   parameter lamda: number of ranked elements
%   return the array

% I{j} should be an indivivual
% j is the index
A = a_matrix;
I = [1:lambda];
population = pop;
for i = 1:N
    swap_count = 0;
    for j = 1:lambda-1
        u=rand();
        if ((penalty(A, population(I(j),:)) == 0) && (penalty(A, population(I(j+1),:)) == 0)) || (u < P_j)
            if(fitness(col_cost, population(I(j),:))) > fitness(col_cost, population(I(j+1),:))
                I([j, j+1]) = I([j+1, j]);
                swap_count = swap_count + 1;
                population([j, j+1]) = population([j+1, j]);
            end
        else
            if(penalty(A, population(I(j),:)) < penalty(A, population(I(j+1),:)))
                I([j, j+1]) = I([j+1, j]);
                population([j, j+1]) = population([j+1, j]);
                swap_count = swap_count + 1;
            end
        end
    end
    
    if swap_count == 0
        break;
    end
    
end


end

