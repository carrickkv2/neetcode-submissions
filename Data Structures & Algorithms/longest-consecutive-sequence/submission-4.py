class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        result = 0

        for num in num_set:
            i = 1
            while num + i in num_set:
                i += 1
            if i >= result:
                result = i

        return result 
        