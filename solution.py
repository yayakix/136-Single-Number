class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # loop
        # mapS.get(currValS, 0) + 1
        dict = {}
        for x in range(len(nums)):
            if nums[x] in dict:
                dict[nums[x]] = dict[nums[x]] + 1
            else:
                dict[nums[x]] = 1
        for key, value in dict.items():
            if 1 == value:
                return key
