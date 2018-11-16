nums = [2,321321,21321,2321,23,421421212,1,2]
nums.sort()
print(nums)

infors = [{"name":"laowang","age":18},{"name":"zhangsan","age":19},{"name":"xiaoqiang","age":20}]
infors.sort(key=lambda x:x['name'])
print(infors)
