class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(res, tmp, candidates, remain, index):
            if remain < 0:
                return
            if remain == 0:
                res.append(tmp.copy())
                return
            for i in range(index, n):
                if i > index and candidates[i] == candidates[i - 1]: # skip duplicates
                    continue
                tmp.append(candidates[i])
                backtrack(res, tmp, candidates, remain - candidates[i], i + 1) # not i because we cannot reuse same elements
                tmp.pop()

        res = []
        tmp = []
        n = len(candidates)
        candidates.sort() # sort is necessary
        backtrack(res, tmp, candidates, target, 0)
        return res
