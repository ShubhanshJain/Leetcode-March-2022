class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        if len(tops) <= 1:      # means that entire row has only one element or is empty
            return 0
    
        def helper(target, tops, bottoms):  # function to keep track of swaps
            count = 0           # initial count

            for indx in range(len(tops)):       # iterating index in range of lenght og given dominos
                a, b = tops[indx], bottoms[indx]        # initializing a & b
                if target == a:
                    continue
                else:
                    if b == target:
                        count += 1
                    else:           # when we don't have required tile in either a or b
                        count = float("inf")        # count changed to positive infinity
                        break           # break the loop as their is no answer
            return count        # retrun the final count

        # calling the function in all possible ways-
        res = min(helper(tops[0], tops, bottoms), helper(tops[0], bottoms, tops), helper(bottoms[0], tops, bottoms), helper(bottoms[0], bottoms, tops))
        
        # if everything in resultant has positive infinity than we must retrun -1
        return res if res != float("inf") else -1