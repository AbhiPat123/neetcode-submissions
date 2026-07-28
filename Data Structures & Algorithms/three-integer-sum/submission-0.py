class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        ret_list = []
        for idx, num3 in enumerate(nums):
            # if nums3 itself is > 0 then sum can never be 0 in sorted array
            if num3 > 0:
                break

            # if the current num (idx  1 onwards is same as before skip it)
            if idx>0 and num3 == nums[idx-1]:
                continue

            itr1 = idx+1
            itr2 = len(nums)-1
            target_nums3 = -1*num3
            while itr1 < itr2:
                two_sum = nums[itr1] + nums[itr2]
                if two_sum == target_nums3:
                    ret_list.append([num3, nums[itr1], nums[itr2]])
                    itr1 += 1
                    itr2 -= 1

                    # inner quick skips if same numbers
                    while itr1<itr2 and nums[itr1] == nums[itr1-1]:
                        itr1 += 1                    
                    while itr1<itr2 and nums[itr2] == nums[itr2+1]:
                        itr2 -= 1
                elif two_sum < target_nums3:
                    itr1 += 1
                else:
                    itr2 -= 1
        return ret_list


