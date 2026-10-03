class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        k=0
        for i in range(len(nums)):
            if (target-nums[i]) in hash:
                return [hash[target-nums[i]],i]
            else:
                hash[nums[i]]=i



        