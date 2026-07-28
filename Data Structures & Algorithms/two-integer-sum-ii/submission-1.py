class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        itr1 = 0
        itr2 = len(numbers)-1
        while itr1 < itr2:
            if numbers[itr1] + numbers[itr2] == target:
                return [itr1+1,itr2+1]
            elif numbers[itr1] + numbers[itr2] < target:
                itr1 += 1
            else:
                itr2 -= 1