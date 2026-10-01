class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash={}
        for i in nums:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        ans=dict(sorted(hash.items(), key=lambda item: item[1],reverse=True))
        kk=[]

        for i in ans:
            if k>0:
                kk.append(i)
                k-=1
            else:
                break
        return kk

                
        





        