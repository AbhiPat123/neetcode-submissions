class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        itr1 = 0
        itr2 = len(heights) - 1
        while itr1<itr2:
            cur_area = min(heights[itr1],heights[itr2]) * (itr2-itr1)
            if cur_area > max_area:
                max_area = cur_area

            if heights[itr1] <= heights[itr2]:
                cur_height = heights[itr1]
                while itr1<itr2 and cur_height >= heights[itr1]:
                    itr1 += 1
            else:
                cur_height = heights[itr2]
                while itr1<itr2 and cur_height >= heights[itr2]:
                    itr2 -= 1

        return max_area
