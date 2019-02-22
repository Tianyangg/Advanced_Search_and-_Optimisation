function violation = penalty(a_matrix, xx)
% penalty function h = (ax - 1)^2
[rows cols] = size(a_matrix);
%xx = zeros(cols, 1);
%xx(x) = 1;
h = (a_matrix*xx' - 1)'*(a_matrix*xx' - 1);
[a, b] = size(h);

violation = sum(h);

end

