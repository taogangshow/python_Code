def test():
    a = 1
    b = 2
    c = 3
   #第一种
   #d = [a,b,c]
   #return d

   #第二种
   #return [a,b,c]

   #第三种
   return a,b,c
nums = test()
print(nums)
