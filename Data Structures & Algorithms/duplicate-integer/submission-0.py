class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash={}
        for i in nums:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
            if hash[i]>1:
                return True
        return False
        