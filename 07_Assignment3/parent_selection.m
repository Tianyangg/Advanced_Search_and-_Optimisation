function [p1, p2] = parent_selection(p, A, c)
% Matching selection
% Select the parents to improve the feasibility 
% witout undermining solution quality

%p1 = p(1,:) % best one

% binary tournament selection
[p1, index] = binary_tourament(p, A, c);
%p1 = p(1,:);
%[p2, index] = binary_tourament(p, A, c);
% while isequal(p1, p2)
%     [p2, index] = binary_tourament(p, A, c);
% end
if feasible(p1, A)
    % if the first parent is feasible, use binary again
    while(1)
        p2 = binary_tourament([p(1:index-1,:);p(index+1:end,:)], A, c);
%         if isequal(p1, p2)
%             disp('p1, p2 same');
%         end
        if ~isequal(p1, p2)
            break;
            %disp('p1, p2 same');
        end
    end
else
    % select the best compatibility
    %diff = setdiff(p, p1);
    diff = p;
    compatibility = zeros(1, size(diff, 1));
    R_p1 = cover_rows(p1, A);
    for i = 1:size(diff, 1)
        %Si = diff(i,:);
        R_s = cover_rows(diff(i,:), A);
        compatibility(i)= length(union(R_p1, R_s)) - length(intersect(R_p1, R_s));
    end
    [m, ~] = max(compatibility);
    % should select a random when multiple max
    maxes = find(compatibility == m);
    index = datasample(maxes, 1);
    p2 = diff(index, :);    
end

end

