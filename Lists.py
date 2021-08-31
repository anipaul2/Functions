#remove function
nums = [1,2,3,4]
print(nums)
nums.remove(3)
print(nums)
nums.pop()
print(nums)
nums.pop(0)
print(nums)

#extend function
nums.extend([3,4])
print(nums)
nums.extend([])
print(nums)
#insert function

nums.insert(0,1)
print(nums)
nums.insert(2, "Two and a half")
print(nums)
#Here is the final nums list where four numbers and one string is stored.
