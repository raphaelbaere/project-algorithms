def find_duplicate(nums):
    if len(nums) <= 1:
        return False
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

    currentNumber = nums[0]
    for i in range(1, len(nums)):
        if isinstance(nums[i], str) or nums[i] < 0 or not nums[i]:
            return False
        elif nums[i] == currentNumber:
            return currentNumber
        currentNumber = nums[i]

        if i == len(nums) - 1:
            return False
        

print(find_duplicate([1, 2, 2, 3, 4]))