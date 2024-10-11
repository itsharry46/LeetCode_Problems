class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited_elements = {}
        i, result = 0, 0

        for j in range(len(s)):
            if s[j] in visited_elements:
                i = max(visited_elements[s[j]], i)

            visited_elements[s[j]] = j + 1
            result = max(result, j - i + 1)

        return result


solution = Solution()

input_value = input('Please enter the string: ')
answer = solution.lengthOfLongestSubstring(input_value)
print(answer)