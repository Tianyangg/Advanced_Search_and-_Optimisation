function temp = temperature(initial,i,i_max)
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
temp = i*initial*(1 - i/i_max);
end


% temperature(t0, k, kmax) = k*t0 * (1 - k/kmax)