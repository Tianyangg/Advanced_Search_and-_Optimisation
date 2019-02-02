function accept = acceptance_function(solution_energy,neighbour_energy, Temperature)
% return the rate of acceptance

% math for this function
% exp( (solutionEnergy - neighbourEnergy) / temperature )
accept =  exp( (solution_energy - neighbour_energy) / Temperature );

end

