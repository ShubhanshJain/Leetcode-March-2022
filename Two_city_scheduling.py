# We need to follow brute force approach as we want half people to visit city 'a' and other half to visit 'b'. 
# Out of all possibilites we need to choose minimum cost of flying.
# Afterwards we can shift our solution to greedy approach in order to minimize time and space complexity.

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []       # duffenece between flying cost of cities c1 and c2
        for c1, c2 in costs:
            diff.append([c2-c1, c1, c2])
        diff.sort()
        res = 0     # set initial cost of flying
        for i in range(len(diff)):
            if i < len(diff) // 2:      # half to city c1 and another half to city c2
                res += diff[i][2]
            else:
                res += diff[i][1]
        return res