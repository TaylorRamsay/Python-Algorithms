

def search(self, nums: list[int], target: int) -> int:
    begin = 0
    end = len(nums) - 1
    index = -1
    while (begin <= end) and (index == -1):
        mid = (begin+end)//2
        if nums[mid] == target:
            index = mid
        else:
            if nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1
    return index