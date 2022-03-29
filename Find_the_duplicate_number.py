class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
                
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow        
    
    
    
    # time complexity- O(n) 
    # space complexity- O(1)  
    # The problem is sloved via using Floyd's algorithm. To learn more about this alorithm, refer - https://www.programiz.com/dsa/floyd-warshall-algorithm