def func(nums,x):
    for num in nums:
        if num==x:
            return True
    return False
a=func(nums=[1,5,8,3],x=float(input("Enter a number:")))
print(a)