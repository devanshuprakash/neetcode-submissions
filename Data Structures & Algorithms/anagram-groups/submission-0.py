class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash={}
        for i in strs:
            ss="".join(sorted(i))
            if ss in hash:
                hash[ss].append(i)
            else:
                hash[ss]=[i]
        ans=[]
        for i in hash:
            ans.append(hash[i])
        return ans
        