class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        result = 0

        for num in num_set:
            i = 1
            while num + 1 in num_set:
                i += 1
                num = num + 1
            if i >= result:
                result = i

        return result 
        