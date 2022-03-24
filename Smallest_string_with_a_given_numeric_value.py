class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        if n*26 == k:       # if we have all 'z'
            return 'z'*n
        k -= n      # left over letters
        nz = k // 25        # estimating number of 'z'
        na = n - nz - 1     # estimate number of 'a'
        
        return na*'a'+chr(ord('a')+k%25)+nz*'z'     # number of 'a' + number of elements in middle + number of 'z'