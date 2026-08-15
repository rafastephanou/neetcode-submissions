class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bs(lo, hi):
            if lo > hi:
                return -1
            mid = (lo + hi) // 2
            
            if nums[mid] == target: 
                return mid


            if nums[mid] > target:
                return bs(lo, mid-1)
            
            if nums[mid] < target:
                return bs(mid+1, hi)

        return bs(0, len(nums)-1)