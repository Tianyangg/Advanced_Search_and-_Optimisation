clear all;
[matrix_a, column_cost] = ReadInData('b727.dat');
p = initialize(matrix_a, 100);
[rows, cols] = size(matrix_a);
Stochatic_ranking(0.5, rows, cols, p, matrix_a, column_cost)