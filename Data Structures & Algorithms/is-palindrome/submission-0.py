class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs=[]
        for i in s:
            if 65 <= ord(i) <=90:
                cs.append(i.lower())
            elif 97 <= ord(i) <=122:
                cs.append(i)
            elif 48<= ord(i) <= 57:
                cs.append(i)
        return ("").join(list(cs))==("").join(list(cs)[::-1])
        