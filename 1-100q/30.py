from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        if not s or not words:
            return []

        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        words = Counter(words)

        res = []
        for i in range(0, one_word): # word起始点设置的不同
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()

            while right + one_word <= n: # 经典双指针（滑动窗口）和哈希表的配合
                w = s[right:right + one_word] # 仔细看，两个while下面的四行代码极其类似
                right += one_word
                cur_Counter[w] += 1
                cur_cnt += 1
                while cur_Counter[w] > words[w]:
                    left_w = s[left:left+one_word]
                    left += one_word
                    cur_Counter[left_w] -= 1
                    cur_cnt -= 1
                    
                if cur_cnt == word_num:
                    res.append(left)
        return res
