from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []

        for idx_1, loop_1 in enumerate(nums):
            for idx_2, loop_2 in enumerate(nums):
                if idx_1 != idx_2 and (target == loop_1 + loop_2):
                    res.append(idx_1)
                    res.append(idx_2)

                    return res


solution = Solution()
answer = solution.twoSum([2, 7, 11, 15], 9)
print(answer)
