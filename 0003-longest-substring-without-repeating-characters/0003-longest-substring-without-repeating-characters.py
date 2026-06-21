class Solution(object):
    def lengthOfLongestSubstring(self, s):
        #s라는 문자가 주어짐. 
        seen = set() #중복을 허용하지 않는 자료구조 
        left = 0
        longest = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            longest = max(longest, right - left + 1)

        return longest