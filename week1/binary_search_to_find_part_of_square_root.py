def findSquareRootByInteger(number) -> int:
	if number == 1:
		return 1
	if number < 1:
		return -1

	left, right = 1, number
	answer = -1
	while left <= right:
		middle = (left + right) // 2
		square = middle * middle
		if number < square:
			answer = middle
			right = middle - 1
		else:
			left = middle + 1

	return answer - 1
