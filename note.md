3번 

이 코드는 슬라이딩 윈도우(Sliding Window) + Set을 사용한 정답 코드야. 

핵심은 중복이 없는 구간(window)을 유지하면서 오른쪽으로 한 칸씩 확장하는 것이야.

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()      # 현재 윈도우 안에 있는 문자들
        left = 0          # 윈도우의 시작 위치
        longest = 0       # 가장 긴 길이 저장

        for right in range(len(s)):   # right가 오른쪽으로 이동

            # 현재 문자가 이미 있으면 중복이므로
            # 중복이 없어질 때까지 left를 오른쪽으로 이동
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # 현재 문자 추가
            seen.add(s[right])

            # 현재 윈도우 길이 계산
            longest = max(longest, right - left + 1)

        return longest
```
