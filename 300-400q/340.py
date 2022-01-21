class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        left = 0
        right = 0
        # window = {}
        window = collections.defaultdict(int)
        ans = 0
        while right < len(s):
            c = s[right]
            # window[c] = window.get(c, 0) + 1
            window[c] += 1
            right += 1
            
            while len(window) > k:
                d = s[left]
                window[d] -= 1
                if window[d] == 0:
                    del window[d]
                left += 1

            ans = max(ans, right-left)
        return ans
