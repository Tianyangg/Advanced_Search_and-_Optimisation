function rows = cover_rows(S, A)
% return the rows covered by S
selected = A(:, S==1);
rows = find(sum(selected, 2) >= 1);
end

