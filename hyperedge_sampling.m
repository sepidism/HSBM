function [edges, IDX] = hyperedge_sampling(numV, p_intra, p_inter)
%
IDX = zeros(1, numV);
IDX(1:floor(numV/2)) = 1;
%
alloc = 1024;
offset = 1;
edges = zeros(3, alloc);
for id1 = 1 : numV
    for id2 = (id1+1) : numV
        for id3 = (id2 + 1) : numV
            if IDX(id1) == IDX(id2) && IDX(id2) == IDX(id3)
                if rand(1,1) < p_intra
                    if offset > alloc
                        edges = [edges, zeros(3, alloc)];
                        alloc = alloc*2;
                    end
                    edges(1, offset) = id1;
                    edges(2, offset) = id2;
                    edges(3, offset) = id3;
                    offset = offset + 1;
                end
            else
                if rand(1,1) < p_inter
                    if offset > alloc
                        edges = [edges, zeros(3, alloc)];
                        alloc = alloc*2;
                    end
                    edges(1, offset) = id1;
                    edges(2, offset) = id2;
                    edges(3, offset) = id3;
                    offset = offset + 1;
                end
            end
        end
    end
end
edges = edges(:, 1: (offset-1));
