class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        res = 0
        
        # in following cases we will return 0:
        #1. if startvalue = target and if startvalue > target

        while target > startValue:
            res += 1
            if target % 2 == 0:
                target /=2      # divide AND
            else:
                target += 1
        return int(res + (startValue - target))      