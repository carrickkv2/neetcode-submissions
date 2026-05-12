class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        diff_dict = {}
        
        for index, num in enumerate(numbers):

            diff = target - num

            if diff in diff_dict:
                return [diff_dict[diff] + 1, index + 1]

            diff_dict[num] = index