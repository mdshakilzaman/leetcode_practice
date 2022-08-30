class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Brute force: run a loop with every element. time complexity: O(n)
        binary search: it has to be O(logn)
        '''
        l, r = 0, len(nums)-1
        
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]: # this is the condition we need to add for rotated array.
                if nums[l] <= target <= nums[mid]: 
                    r = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return -1
                