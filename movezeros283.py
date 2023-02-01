nums = [0, 1, 0, 3, 12]

previous = 0
for i in range(0,len(nums)):
    if nums[i] !=0:
        hold = nums[previous]
        nums[previous] = nums[i]
        nums[i] = hold
        previous+=1

print(nums)

