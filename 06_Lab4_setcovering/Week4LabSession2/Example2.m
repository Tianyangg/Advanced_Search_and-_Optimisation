clear all
%% Try the B727 problem
[matrix_a, column_cost] = ReadInData('b727.dat');

[total_cost, x] = StochasticSetCover(matrix_a, column_cost);
%[total_cost, x] = SimpleGASetPartition(matrix_a, column_cost, 1000);
