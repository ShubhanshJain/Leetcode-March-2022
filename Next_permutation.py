class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
         # find first decreasing element
        i = len(nums) - 2
        while i > -1:
            if nums[i] < nums[i + 1]:                
                break
            i -= 1
            
        # find number just larger than first decreasing element
        j = i
        min_large = sys.maxsize
        for k in range(i, len(nums)):
            
            if nums[k] > nums[i]:
                min(min_large, nums[k]) 
                j = k
                
        # swap
        temp = nums[j]
        nums[j] = nums[i]
        nums[i] = temp
                
        # sort all elements after the first decrease element position
        nums[i + 1:] = sorted(nums[i + 1:])

        #Time complexity - N
        #Space Complexity - 1
        