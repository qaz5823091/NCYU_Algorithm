def binarySearchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if target > nums[middle]:
                left = middle + 1
            elif target == nums[middle]:
                return middle
            else:
                right = middle - 1

        return left
