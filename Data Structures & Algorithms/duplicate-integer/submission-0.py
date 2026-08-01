class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        r = set({})

        for num in nums:
            if num in r:
                return True
            else:
                r.add(num)
        
        return False