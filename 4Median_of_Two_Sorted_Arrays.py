import time

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if nums1 or nums2:
            summ = nums1 + nums2
            summ.sort()
            order = len(summ) // 2
            if (len(summ) % 2) == 0:
                return (summ[order-1] + summ[order])/2
            elif (len(summ) % 2) == 1:
                return summ[order]
        
Solution = Solution()  

### First one
inputs1 = [1, 3]
inputs2 = [2]

start = time.time()
result = Solution.findMedianSortedArrays(inputs1, inputs2)
print(result)

print("Time :", time.time() - start)

### Second 
inputs3 = [1, 2]
inputs4 = [3, 4]

start = time.time()
result = Solution.findMedianSortedArrays(inputs3, inputs4)
print(result)

print("Time :", time.time() - start)

### Third
inputs3 = [1, 2]
inputs4 = []

start = time.time()
result = Solution.findMedianSortedArrays(inputs3, inputs4)
print(result)

print("Time :", time.time() - start)

### Fourth
inputs5 = [6, 8, 1, 2]
inputs6 = [3, 6, 6, 9, 4, 2]

start = time.time()
result = Solution.findMedianSortedArrays(inputs5, inputs6)
print(result)

print("Time :", time.time() - start)