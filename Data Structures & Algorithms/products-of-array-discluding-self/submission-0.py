class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [1]
        # right products array
        rigt_prod_list = [1]
        rigt_prod_rung = 1
        for idx in range(len(nums)-2,-1,-1):
            rigt_prod_rung = rigt_prod_rung*nums[idx+1]
            # print(rigt_prod_rung)
            rigt_prod_list.append(rigt_prod_rung)
        rigt_prod_list = rigt_prod_list[::-1]
        # print(rigt_prod_list)

        # o through array left to right multiplying by right side
        ret_val = [rigt_prod_list[0]]
        prod_rung = 1
        for idx in range(1,len(nums)):
            prod_rung = prod_rung*nums[idx-1]
            ret_val.append(prod_rung*rigt_prod_list[idx])
        
        return ret_val
