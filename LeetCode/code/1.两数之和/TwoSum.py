from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
                return []
arr = []
input_str = input("输入数组元素（空格分隔开，回车结束）:")
elements = input_str.split()
for element in elements:
    arr.append(int(element))

target = int(input("请输入目标值："))
s=Solution()
result=s.twoSum(arr,target)
if result:
    print("找到两个数的索引为：",result)
else:
    print("未找到两个数")