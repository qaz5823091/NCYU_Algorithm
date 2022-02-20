def search(nums, target) -> int:
	left, right = 0, len(nums) - 1
	answer = -1

	while left <= right:
		middle = (left + right) // 2
		if target > nums[middle]:
			left = middle + 1
		elif target == nums[middle]:
			answer = middle
			right = middle - 1
		else:
			right = middle - 1

	return answer
