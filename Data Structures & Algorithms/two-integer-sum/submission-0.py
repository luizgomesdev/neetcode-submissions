class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        res = {}

        for idx, num in enumerate(nums):
            x = target - num

            pair_idx = res.get(x)
            if pair_idx is not None:
                return [pair_idx, idx]
            else:
                res[num] = idx
