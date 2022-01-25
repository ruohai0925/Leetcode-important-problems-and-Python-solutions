# 这里有一个非常非常通用的模板,传入backtrack的变量都包括记录结果的res，tmp for path，原数组，目标值，以及一个index
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(res, tmp, candidates, remain, index):
            if remain < 0:
                return
            if remain == 0:
                res.append(tmp.copy())
                return
            for i in range(index, n):
                tmp.append(candidates[i])
                backtrack(res, tmp, candidates, remain - candidates[i], i) # not i + 1 because we can reuse same elements
                tmp.pop()

        res = []
        tmp = []
        n = len(candidates)
        # candidates.sort() # 可以不用sort
        backtrack(res, tmp, candidates, target, 0)
        return res
