class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd_indices = [nums[i] for i in range(1, len(nums), 2)]
        even_indices = [nums[i] for i in range(0, len(nums), 2)]
        odd_indices.sort(reverse=True)
        even_indices.sort()
        result = nums[:]
        result[1::2] = odd_indices 
        result[0::2] = even_indices 
        return result    
