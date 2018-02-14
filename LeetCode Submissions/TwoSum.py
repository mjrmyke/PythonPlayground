'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''
func twoSum(nums []int, target int) []int {
   var output []int
   for k1, _ :=  range nums{
    for k2, _ :=  range nums{
            if k1 != k2{
                if nums[k1]+nums[k2] == target{
                    return append(output, k1, k2)
                }
            }
        }
    }
    return output
}