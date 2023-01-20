

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



class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1):
            return 1
        first = 1
        last = n
        while first <= last:
            mid = (first+last)//2
            if isBadVersion(mid) == False:
                first = mid+1
            else:
                last = mid-1
                result = mid
        return result


def sortedSquares(self, nums: list[int]) -> list[int]:
    res = [0] * len(nums)
    writeCount = len(nums) - 1
    leftPointer = 0
    rightPointer = len(nums) - 1
    leftSquare = nums[leftPointer]**2
    rightSquare = nums[rightPointer]**2

    while writeCount >= 0:
        if leftSquare > rightSquare:
            res[writeCount] = leftSquare
            leftPointer += 1
            leftSquare = nums[leftPointer]**2
        else:
            res[writeCount] = rightSquare
            rightPointer -= 1
            rightSquare = nums[rightPointer]**2
        writeCount -= 1
    return res

def sortedSquares(self, nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        nums[i] *= nums[i]
    nums.sort()
    return nums