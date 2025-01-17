class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k = k+1
            return k
        


# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
# 示例 1:
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
# 示例 2:
# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释: 
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
# 说明:
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的 原地 算法。
    def rotate(self, nums, k):
        n = len(nums)
        k = k%n
        def swap(i, r):
            while(i<r):
                nums[i], nums[r] = nums[r], nums[i]
                i = i + 1
                r = r - 1
        swap(0, n - k - 1)
        swap(n - k, n - 1)
        swap(0, n - 1)

