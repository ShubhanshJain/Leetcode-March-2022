class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()       # sort the array of persons according to their weights
        i,j = 0, len(people) - 1    # heaviest person is [i] and lightest person is [j]
        boats = 0       # initial boats count
        
        while i <= j:
            if people[i] + people[j] <= limit:      # if sum of weights of heaviest person[i] and lightest person[j] is greater than limit 
                i = i+1
            j -= 1
            boats += 1
            
        return boats   