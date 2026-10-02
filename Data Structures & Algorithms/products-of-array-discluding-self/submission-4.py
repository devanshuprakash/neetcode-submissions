class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        k=0
        for i in nums:
            if i !=0:
                p*=i
            else:
                k+=1
        ans=[]
        if (k==0):
            for i in nums:
                ans.append(int(p/i))
        else:
            if k==1:
                for i in nums:
                    if i==0:
                        ans.append(p)
                    else:
                        ans.append(0)
            else:
                for i in nums:
                    ans.append(0)
            
        return ans