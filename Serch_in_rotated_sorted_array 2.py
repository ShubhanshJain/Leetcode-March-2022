class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target: return True
            if (nums[l] == nums[mid]) and (nums[r] == nums[mid]): l, r = l+1, r-1
            elif nums[l] <= nums[mid]:
                if (nums[l] <= target) and (nums[mid] > target): r = mid-1
                else: l = mid + 1
            else:
                if (nums[mid] < target) and (nums[r] >= target): l = mid + 1
                else: r = mid-1
        return False