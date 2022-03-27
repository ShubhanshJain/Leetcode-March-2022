class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        tmp = []
        for i, m in enumerate(mat):     # number of soliders, citizen
            cond = (sum(m),i)
            tmp.append(cond)
            
        tmp.sort()
        return [i[1] for i in tmp[:k]]