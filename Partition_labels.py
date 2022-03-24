class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}      #   hashmap to intialize every charater to last index in string 's'
        
        for i, c in enumerate(s):       #   enumerate allows us to iterate indexes and characters at the same time.
            lastIndex[c] = i
            
        res = []        #     
        size,end = 0,0
        for i,c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])    # update the last index
            
            if i == end:        # to stop partitioning
                res.append(size)
                size = 0
        return res 