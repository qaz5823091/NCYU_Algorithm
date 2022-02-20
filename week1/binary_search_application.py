 def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        answer = -1
        while left <= right:
            middle = (left + right) // 2
            if isBadVersion(middle):
                answer = middle
                right = middle - 1
            else:
                left = middle + 1

        return answer
