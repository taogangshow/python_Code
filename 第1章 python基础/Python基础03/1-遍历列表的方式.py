print("---while遍历---")
nums = [11,22,33,44,55]
i = 0
while i<5:
    print(nums[i])
    i+=1
print("while遍历不用数下表的方式")
nums = [11,22,33,44,55]
nums_lenght = len(nums)
i = 0
while i<nums_lenght:
    print(nums[i])
    i+=1
print("---for遍历:不用控制元素的个数以及下表---")
for num in nums:
    print(num)
