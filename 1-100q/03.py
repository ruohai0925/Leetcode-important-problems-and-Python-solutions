class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        n = len(s)
        left = 0
        substring = collections.defaultdict(int)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len+=1
            while s[i] in substring:
                # Two ways to delete key in a dict
                # del substring[s[left]] 
                substring.pop(s[left])
                cur_len-=1
                left+=1
            if cur_len>max_len: max_len=cur_len
            substring[s[i]]+=1
            # substring[s[i]].add(1), append(1), all wrong

        return max_len
