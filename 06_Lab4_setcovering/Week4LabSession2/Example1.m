clear all
con_matrix = [0 0 0 0 1 1 1;
              1 1 0 0 0 0 0;
              0 0 1 1 0 0 0;
              1 0 0 0 0 0 1;
              0 1 0 1 0 1 0]

column_cost = [560 335 420 470 545 660 490];

[min_cost, soltion] = StochasticSetCover(con_matrix, column_cost)


