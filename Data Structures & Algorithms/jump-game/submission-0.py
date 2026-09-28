class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Get the goal - end of arr
        goal = len(nums) - 1
        
        # Going backwards from the goal
        for i in range(len(nums) - 2, -1, -1):
            # If the value at current index is greater or equal to the distance from that index
            # to the goal, we can move there and change the goal
            if nums[i] >= goal - i:
                goal = i

        return goal == 0
            
            # Otherwise we continue

