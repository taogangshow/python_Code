nums = [11,22,33,44,55]
for temp in nums:
    print(temp)
else:
    print("============")
#不管执行不执行for循环都会打印print("===========")
nums = []
for temp in nums:
    print(temp)
else:
    print("============")
#想要不执行print("===========")就需要加入break

nums = [11,22,33,44,55]
for temp in nums:
    print(temp)
    break
else:
    print("============")
