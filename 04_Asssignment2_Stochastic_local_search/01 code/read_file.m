function cities = read_file(file_name)
% read the file
fileID = fopen(file_name, 'r');
%formatSpec = '%d %f %f';
%sizeA = [3 Inf];
A = cell2mat(textscan(fileID,'%7.2f %7.2f %7.2f', 'HeaderLines', 7))';
cities = A(2:3,:)
%save('cities');
end

