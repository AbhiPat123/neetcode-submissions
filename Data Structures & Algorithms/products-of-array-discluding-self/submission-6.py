class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [1]
        # right products array
        ret_val = [1]
        rigt_prod_rung = 1
        for idx in range(len(nums)-2,-1,-1):
            rigt_prod_rung = rigt_prod_rung*nums[idx+1]
            # print(rigt_prod_rung)
            ret_val.append(rigt_prod_rung)
        ret_val = ret_val[::-1]
        # print(ret_val)

        # go through array left to right multiplying by right side
        prod_rung = 1
        for idx in range(1,len(nums)):
            prod_rung = prod_rung*nums[idx-1]
            ret_val[idx] = (prod_rung*ret_val[idx])
        
        return ret_val
